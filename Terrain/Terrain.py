import numpy as np

def ramp_x(x, y):
    return x

def ramp_y(x, y):
    return y

def f_sum_x_y(x, y):
    return x + y

def egg_carton(x, y):
    return np.sin(x) * np.sin(y)

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
        dx = np.gradient(self.elevation, axis=1)
        dy = np.gradient(self.elevation, axis=0)
        self.gradient = np.stack((dx, dy), axis=0)

    def threshold_magnitude_gradient(self, threshold):
        magnitude = np.linalg.norm(self.gradient, axis=0)
        return magnitude > threshold

    def max_elevation(self):
        shifted_up = np.roll(self.elevation, shift=-1, axis=0)
        shifted_down = np.roll(self.elevation, shift=1, axis=0)
        shifted_left = np.roll(self.elevation, shift=-1, axis=1)
        shifted_right = np.roll(self.elevation, shift=1, axis=1)

        max_values = np.maximum.reduce([shifted_up, shifted_down, shifted_left, shifted_right])
        return self.elevation > max_values

    def min_elevation(self):
        # Get the elevation values at positions to the immediate left, right, above, and below
        left = np.roll(self.elevation, shift=(0, 1), axis=(0, 1))
        right = np.roll(self.elevation, shift=(0, -1), axis=(0, 1))
        above = np.roll(self.elevation, shift=(1, 0), axis=(0, 1))
        below = np.roll(self.elevation, shift=(-1, 0), axis=(0, 1))

        # Check if the elevation is strictly less than its neighbors
        result = self.elevation < left
        result &= self.elevation < right
        result &= self.elevation < above
        result &= self.elevation < below

        return result

    def compute_extrema(self):
        self.extrema = {}
        max_positions = np.argwhere(self.max_elevation())
        min_positions = np.argwhere(self.min_elevation())
        # print(max_positions)
        # print(min_positions)
        for pos in max_positions:
            self.extrema[tuple(pos)] = 'max'
        for pos in min_positions:
            self.extrema[tuple(pos)] = 'min'

    def interpolate_gradient(self, x, y):
        i, j = int(x % self.n_cols), int(y % self.n_rows)

        # Get the gradient values at the four corners
        gradient_00 = self.gradient[:, i, j]
        gradient_01 = self.gradient[:, i, (j + 1) % self.n_rows]
        gradient_10 = self.gradient[:, (i + 1) % self.n_cols, j]
        gradient_11 = self.gradient[:, (i + 1) % self.n_cols, (j + 1) % self.n_rows]

        # Calculate alpha and beta
        alpha, beta = x - i, y - j

        # Interpolate the gradient components
        interpolated_x, interpolated_y = self.bilinear_interpolate(alpha, beta, gradient_00[0], gradient_01[0],
                                                                   gradient_10[0], gradient_11[0]), \
                                         self.bilinear_interpolate(alpha, beta, gradient_00[1], gradient_01[1],
                                                                   gradient_10[1], gradient_11[1])

        return interpolated_x, interpolated_y

    def interpolate_elevation(self, x, y):
        i, j = int(x % self.n_cols), int(y % self.n_rows)
        f_00 = self.elevation[i, j]
        f_01 = self.elevation[i, (j + 1) % self.n_rows]
        f_10 = self.elevation[(i + 1) % self.n_cols, j]
        f_11 = self.elevation[(i + 1) % self.n_cols, (j + 1) % self.n_rows]
        alpha, beta = x % 1, y % 1  # Ensure that alpha and beta are between 0 and 1
        return self.bilinear_interpolate(alpha, beta, f_00, f_01, f_10, f_11)

    @staticmethod
    def bilinear_interpolate(alpha, beta, f_00, f_01, f_10, f_11):
        return (1 - alpha) * (1 - beta) * f_00 + alpha * (1 - beta) * f_10 + (
                1 - alpha) * beta * f_01 + alpha * beta * f_11


#working
#for init test
# t = Terrain(ramp_x, 2, 3)
# print(t.elevation)
# print(t.row_mesh)
# print(t.col_mesh)

#working
#for add test
# t = Terrain(ramp_x, 2, 5)
# t2 = Terrain(ramp_y, 2, 5)
# print(t.elevation)
# print(t2.elevation)
# t.add(t2)
# print(t.elevation)
# t2.add(t, '-')
# print(t2.elevation)

#working
#for threshold_elevation test
# t = Terrain(ramp_x, 2, 5)
# print(t.elevation)
# print(t.threshold_elevation(2))

#working
#for compute_gradient test
# t = Terrain(ramp_x, 4, 5)
# t.compute_gradient()
# print(t.gradient)
# t = Terrain(ramp_y, 4, 5)
# t.compute_gradient()
# print(t.gradient)

#for threshold_magnitude_gradient test
# t = Terrain(f_sum_x_y, 5, 5)
# print(t.elevation)
# t.compute_gradient()
# print(t.gradient)
# print(t.threshold_magnitude_gradient(1.8))

#working
#for max_elevation
# t = Terrain(f_sum_x_y, 3, 4)
# print(t.max_elevation())

#working
#for min_elevation test
# t = Terrain(f_sum_x_y, 3, 4)
# print(t.min_elevation())

#for compute_extrema test
# t = Terrain(egg_carton, 32, 32)
# t.compute_extrema()
# print(t.extrema == {(4, 4): 'max', (20, 4): 'max', (4, 20): 'max', (20, 20): 'max',
#                        (12, 12): 'min', (28, 12): 'min', (12, 28): 'min', (28, 28): 'min'})
# g = gaussian(15, 20, 4)
# t = Terrain(g, 64, 64)
# t.compute_extrema()
# t.extrema == {(15, 20): 'max', (63, 63): 'min'}

#for interpolate_elevation test
# t = Terrain(ramp_y, 5, 5)
# print(t.interpolate_elevation(3.75, 2.25))

#working
# for interpolate_gradient test
# t = Terrain(ramp_x, 6, 6)
# t.compute_gradient()
# print(t.interpolate_gradient(2.75, 3.25))
# t = Terrain(ramp_y, 6, 6)
# t.compute_gradient()
# print(t.interpolate_gradient(2.75, 3.25))

#working
#for bilinear_interpolate test
# t = Terrain(ramp_x)
# print(t.bilinear_interpolate(.25, 0, 1, 2, 3, 4))
# print(t.bilinear_interpolate(0, .25, 1, 2, 3, 4))
# print(t.bilinear_interpolate(1, .75, 1, 2, 3, 4))
# print(t.bilinear_interpolate(.5, .75, 1, 2, 3, 4))