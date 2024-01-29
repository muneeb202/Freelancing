# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution


# returns the progression outcome according to pass and defer credits
# fail credits not required since they will always be 120 - pass - defer, 
# if input is valid, which is checked for in valid_input()
def outcome(pass_, defer):                                              
    if pass_ == 120:                                                        
        return "Progess"                                            # outcome will always be progress if pass is 120
    
    if pass_ == 100:
        return "Progress (module trailer)"                          # outcome will always be progress if pass is 100
    
    if pass_ == 60 or pass_ == 80:
        return "Module retriever"                                   # outcome will always be progress if pass is 80 or 100

    if pass_ == 40:                                                 # when pass credits are 40
        return "Exclude" if defer == 0 else "Module retriever"      # outcome = exclude if defer is 0, outcome = retreiver for rest defer values
    
    if pass_ == 20:                                                 # when pass credits are 20
        return "Exclude" if defer <= 20 else "Module retriever"     # outcome = exclude if defer is 0/20, outcome = retreiver for rest defer values
    
                                                                    # when pass credits are 0
    return "Exclude" if defer <= 40 else "Module retriever"         # outcome = exclude if defer is 0/20/40, outcome = retreiver for rest defer values


# takes input while checking for validity and stores in the dictionary
def valid_input(input_dict):
    while True:                                                     # until id is not valid
        student = input("Enter student id: ")   
        if student in input_dict:                                   # if id already exists in dictionary
            print("Student Id must be unique.\n")
        else:
            break                                                   # exit loop if unique id

    while True:                                                     # until pass credits are not valid
        try:
            pass_ = int(input("Enter your total PASS credits: "))   # try converting to integer
            if (0 <= pass_ <= 120) and pass_ % 20 == 0:             # if input in range 0 20 40 60 80 100 120, exit loop
                break
            print("Out of range.\n")                                # not a valid number
        except ValueError:                                          # input was not a number
            print("Integer required\n")

    while True:                                                     # until defer credits are not valid
        try:
            defer = int(input("Enter your total DEFER credits: "))  # try converting to integer
            if (0 <= defer <= 120) and defer % 20 == 0:             # if input in range 0 20 40 60 80 100 120, exit loop
                break
            print("Out of range.\n")                                # not a valid number
        except ValueError:                                          # input was not a number
            print("Integer required\n")

    while True:                                                     # until defer credits are not valid
        try:
            fail = int(input("Enter your total FAIL credits: "))    # try converting to integer
            if (0 <= fail <= 120) and fail % 20 == 0:               # if input in range 0 20 40 60 80 100 120, exit loop
                break   
            print("Out of range.\n")                                # not a valid number
        except ValueError:                                          # input was not a number
            print("Integer required\n")

    if pass_ + defer + fail == 120:                                 # if total credits are 120, save data to dictionary
        input_dict[student] = (pass_, defer, fail)          
    else:                                                           # if not, then repeat entire process again
        print("Total incorrect.\n")
        valid_input(input_dict)

# runs main loop for part 4
def part4():
    finish = False
    student_dict = {}

    while not finish:                                               # until user does not enter q
        valid_input(student_dict)                                   # take input and store in dictionary

        while not finish:                                           # until option entered is not correct
            opt = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").strip()

            if opt == "y":                                          # take input again
                break
            if opt == "q":                                          # finish main loop
                finish = True
            else:                                                   # y or n not entered, ask option again
                print('Invalid option')
        print()

    print("\nPart 4:")
    for student in student_dict:                                    # for each student id
        pass_, defer, fail = student_dict[student]                  # get values for the key (student id)
        print(f"{student} : {outcome(pass_, defer)} - {pass_}, {defer}, {fail}")        # print student details along with outcome
    

if __name__ == "__main__":
    part4()