
input_list = []

'''
returns the progession category along with progression outcome according to pass and defer credits
fail credits not required since they will always be 120 - pass - defer, 
if input is valid, which is checked for in valid_input()
progression category -> 0 : Progress, 1 : Trailer, 2 : Retriever, 3 : Exclude
'''
def outcome(pass_, defer):
    if pass_ == 120:
        return (0, "Progess")                                                   # outcome will always be progress if pass is 120
    
    if pass_ == 100:
        return (1, "Progress (module trailer)")                                 # outcome will always be progress if pass is 100
    
    if pass_ == 60 or pass_ == 80:
        return (2, "Module retriever")                                          # outcome will always be progress if pass is 80 or 100

    if pass_ == 40:                                                             # when pass credits are 40
        return (3, "Exclude") if defer == 0 else (2, "Module retriever")        # outcome = exclude if defer is 0, outcome = retreiver for rest defer values
    
    if pass_ == 20:                                                             # when pass credits are 20
        return (3, "Exclude") if defer <= 20 else (2, "Module retriever")       # outcome = exclude if defer is 0/20, outcome = retreiver for rest defer values
    
                                                                                # when pass credits are 0
    return (3, "Exclude") if defer <= 40 else (2, "Module retriever")           # outcome = exclude if defer is 0/20/40, outcome = retreiver for rest defer values


''' 
takes input while checking for validity and stores in the dictionary 
'''
def valid_input():
    while True:                                                                 # until pass credits are not valid
        try:
            pass_ = int(input("Enter your total PASS credits: "))               # try converting to integer
            if (0 <= pass_ <= 120) and pass_ % 20 == 0:                         # if input in range 0 20 40 60 80 100 120, exit loop
                break
            print("Out of range.\n")                                            # not a valid number
        except ValueError:                                                      # input was not a number
            print("Integer required\n")

    while True:                                                                 # until defer credits are not valid
        try:
            defer = int(input("Enter your total DEFER credits: "))              # try converting to integer
            if (0 <= defer <= 120) and defer % 20 == 0:                         # if input in range 0 20 40 60 80 100 120, exit loop
                break
            print("Out of range.\n")                                            # not a valid number
        except ValueError:                                                      # input was not a number
            print("Integer required\n")

    while True:                                                                 # until defer credits are not valid
        try:
            fail = int(input("Enter your total FAIL credits: "))                # try converting to integer
            if (0 <= fail <= 120) and fail % 20 == 0:                           # if input in range 0 20 40 60 80 100 120, exit loop
                break   
            print("Out of range.\n")                                            # not a valid number
        except ValueError:                                                      # input was not a number
            print("Integer required\n")

    if pass_ + defer + fail == 120:                                             # if total credits are 120, return credits      
        return pass_, defer, fail
    
    print("Total incorrect.\n")
    return valid_input()                                                        # if total incorrect, repeat entire input process again


''' 
prints the histogram for part 1
parameters are count of each progression category
'''
def histogram(progress, trailer, retriever, excluded):
    print("-" * 70)
    print(f"Histogram\nProgress {progress:<5} : " + ("*" * progress))               # :<n is for alignment, * x count prints * count number of times
    print(f"Trailer {trailer:<6} : " + ("*" * trailer))
    print(f"Retriever {retriever:<4} : " + ("*" * retriever))
    print(f"Excluded {excluded:<5} : " + ("*" * excluded))
    print(f"\n{progress + trailer + retriever + excluded} outcomes in total.")
    print("-" * 70)


