import numpy as np

def ramp_x(x, _):
    return x

def ramp_y(_, y):
    return y

def f_sum_x_y(x, y):
    return x + y

def bilinear_interpolate(alpha, beta, f_00, f_01, f_10, f_11):
    return ((1 - alpha) * (1 - beta) * f_00) + ((1 - alpha) * beta * f_01) + (alpha * (1 - beta) * f_10) + (alpha * beta * f_11)

def gaussian(x0, y0, sigma, const = 1):
    ''' returns a function that computes a gaussian shape blob, centered at (x0,y0)
    with spread sigma and scaled by an optional height const with default value 1.
    '''
    def g(x,y):
        return const * np.exp(-((x-x0)*(x-x0) + (y-y0)*(y-y0))/(2*np.pi*sigma*sigma))
    return g

def egg_carton(x, y, k = 2, NX = 32, NY = 32):
    '''
    returns an egg carton function that has 4 cycles per 32 pixels in each of x and y directions.
    '''
    return ( np.sin(2*k*np.pi*x/NX ) + np.sin( 2*k*np.pi*y/NY ) )

def roll(arr, shift, axis):
    rolled_array = np.zeros(arr.shape, dtype=arr.dtype)
    if axis == 1:
        rolled_array[:, :shift] = arr[:, -shift:]
        rolled_array[:, shift:] = arr[:, :-shift]
    else:
        rolled_array[:shift, :] = arr[-shift:, :]
        rolled_array[shift:, :] = arr[:-shift, :]
    return rolled_array

class Terrain:
    def __init__(self, func, n_rows=5, n_cols=5):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.col_mesh, self.row_mesh = np.meshgrid(np.arange(n_cols), np.arange(n_rows))
        self.elevation = func(self.col_mesh, self.row_mesh)
        self.gradient = None
        self.extrema = None

    def add(self, other, operator='+'):
        if self.elevation.shape != other.elevation.shape:
            raise AssertionError("Terrain shapes do not match.")
        if operator == '+':
            self.elevation += other.elevation
        elif operator == '-':
            self.elevation -= other.elevation
        else:
            raise AssertionError("Invalid operator. Use '+' or '-'.")

    def threshold_elevation(self, threshold):
        return self.elevation > threshold

    def compute_gradient(self):
        self.gradient = np.zeros((2,) + self.elevation.shape)
        self.gradient[0] = (roll(self.elevation, shift=-1, axis=1) - roll(self.elevation, shift=1, axis=1)) / 2.0
        self.gradient[1] = (roll(self.elevation, shift=-1, axis=0) - roll(self.elevation, shift=1, axis=0)) / 2.0

    def threshold_magnitude_gradient(self, threshold):
        magnitude = np.power(np.sum(self.gradient**2, axis=0), 0.5)
        return magnitude > threshold

    def max_elevation(self):
        shifted_up = roll(self.elevation, shift=-1, axis=0)
        shifted_down = roll(self.elevation, shift=1, axis=0)
        shifted_left = roll(self.elevation, shift=-1, axis=1)
        shifted_right = roll(self.elevation, shift=1, axis=1)

        max_values = np.max(np.array([shifted_up, shifted_down, shifted_left, shifted_right]), axis=0)
        return self.elevation > max_values

    def min_elevation(self):
        # Get the elevation values at positions to the immediate left, right, above, and below
        shifted_up = roll(self.elevation, shift=-1, axis=0)
        shifted_down = roll(self.elevation, shift=1, axis=0)
        shifted_left = roll(self.elevation, shift=-1, axis=1)
        shifted_right = roll(self.elevation, shift=1, axis=1)

        # Check if the elevation is strictly less than its neighbors
        result = self.elevation < shifted_left
        result = np.logical_and(result, self.elevation < shifted_right)
        result = np.logical_and(result, self.elevation < shifted_up)
        result = np.logical_and(result, self.elevation < shifted_down)

        return result

    def compute_extrema(self):
        self.extrema = {}
        max_positions = self.max_elevation()
        for i in range(len(max_positions)):
            for j in range(len(max_positions[i])):
                if max_positions[i][j]:
                    self.extrema[(j, i)] = 'max'

        min_positions = self.min_elevation()
        for i in range(len(min_positions)):
            for j in range(len(min_positions[i])):
                if min_positions[i][j]:
                    self.extrema[(j, i)] = 'min'

    def interpolate_gradient(self, x, y):
        self.compute_gradient()
        j, i = int(x % self.n_cols), int(y % self.n_rows)

        # Get the gradient values at the four corners
        gradient_00 = self.gradient[:, i, j]
        gradient_01 = self.gradient[:, i, (j + 1) % self.n_rows]
        gradient_10 = self.gradient[:, (i + 1) % self.n_cols, j]
        gradient_11 = self.gradient[:, (i + 1) % self.n_cols, (j + 1) % self.n_rows]

        # Calculate alpha and beta
        alpha, beta = y - i, x - j

        # Interpolate the gradient components
        interpolated_x, interpolated_y = bilinear_interpolate(alpha, beta, gradient_00[0], gradient_01[0],
                                                                   gradient_10[0], gradient_11[0]), \
                                         bilinear_interpolate(alpha, beta, gradient_00[1], gradient_01[1],
                                                                   gradient_10[1], gradient_11[1])

        return interpolated_x, interpolated_y

    def interpolate_elevation(self, x, y):
        i, j = int(y % self.n_rows), int(x % self.n_cols)
        f_00 = self.elevation[i, j]
        f_01 = self.elevation[i, (j + 1) % self.n_cols]
        f_10 = self.elevation[(i + 1) % self.n_rows, j]
        f_11 = self.elevation[(i + 1) % self.n_rows, (j + 1) % self.n_cols]
        alpha, beta = y % 1, x % 1  # Ensure that alpha and beta are between 0 and 1
        return bilinear_interpolate(alpha, beta, f_00, f_01, f_10, f_11)


# #working
print("\nfor init test\n**************")
t = Terrain(ramp_x, 2, 3)
print(t.elevation)
print(t.row_mesh)
print(t.col_mesh)

# #working
print("\nfor add test\n**************")
t = Terrain(ramp_x, 2, 5)
t2 = Terrain(ramp_y, 2, 5)
print(t.elevation)
print(t2.elevation)
t.add(t2)
print(t.elevation)
t2.add(t, '-')
print(t2.elevation)

# #working
print("\nfor threshold_elevation test\n**************")
t = Terrain(ramp_x, 2, 5)
print(t.elevation)
print(t.threshold_elevation(2))

# #working
print("\nfor compute_gradient test\n**************")
t = Terrain(ramp_x, 4, 5)
t.compute_gradient()
print(t.gradient)
t = Terrain(ramp_y, 4, 5)
t.compute_gradient()
print(t.gradient)

#working
print("\nfor threshold_magnitude_gradient test\n**************")
t = Terrain(f_sum_x_y, 5, 5)
print(t.elevation)
t.compute_gradient()
print(t.gradient)
print(t.threshold_magnitude_gradient(1.8))

# #working
print("\nfor max_elevation test\n**************")
t = Terrain(f_sum_x_y, 3, 4)
print(t.max_elevation())

#working
print("\nfor min_elevation test\n**************")
t = Terrain(f_sum_x_y, 3, 4)
print(t.min_elevation())

#working
print("\nfor compute_extrema test\n**************")
t = Terrain(egg_carton, 32, 32)
t.compute_extrema()
print(t.extrema == {(4, 4): 'max', (20, 4): 'max', (4, 20): 'max', (20, 20): 'max',
                       (12, 12): 'min', (28, 12): 'min', (12, 28): 'min', (28, 28): 'min'})
g = gaussian(15, 20, 4)
t = Terrain(g, 64, 64)
t.compute_extrema()
print(t.extrema == {(15, 20): 'max', (63, 63): 'min'})

# #working
print("\nfor interpolate_elevation test\n**************")
t = Terrain(ramp_y, 5, 5)
print(t.interpolate_elevation(3.75, 2.25))

# #working
print("\nfor interpolate_gradient test\n**************")
t = Terrain(ramp_x, 6, 6)
print(t.interpolate_gradient(2.75, 3.25))
t = Terrain(ramp_y, 6, 6)
print(t.interpolate_gradient(2.75, 3.25))

# #working
print("\nfor bilinear_interpolate test\n**************")
t = Terrain(ramp_x)
print(bilinear_interpolate(.25, 0, 1, 2, 3, 4))
print(bilinear_interpolate(0, .25, 1, 2, 3, 4))
print(bilinear_interpolate(1, .75, 1, 2, 3, 4))
print(bilinear_interpolate(.5, .75, 1, 2, 3, 4))