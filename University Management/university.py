
def menu():                                                     # print the menu to the console
    print('University Registrar System'
        '\n=============================='
        '\n1. Print courses info'
        '\n2. Search for a course'
        '\n3. Add new course'
        '\n4. Remove a course'
        '\n5. Update a course'
        '\n6. Register a student in a course'
        '\n7. Drop a student from a course'
        '\n8. Exit'
        '\n===============================')
    while True:
        opt = input('\nEnter your choice: ').strip()            # strip() to remove whitespaces from start and end
        try:
            opt = int(opt)                                      # try converting to number
            if 1 <= opt <= 8:                                   # check if valid number
                return opt
            print('Incorrect option entered! Try again')        # number outside range
        except ValueError:
            print('Incorrect option entered! Try again')        # letter entered
                    

def course_info(courses):
    header = ['CRN', 'Code', 'Sec No.', 'Name', 'Instructor', 'Size', 'Available']
    print(f'\n{header[0]:7} {header[1]:8} {header[2]:8} {header[3]:50} {header[4]:20} {header[5]:6} {header[6]:10}')

    for course in courses:                                      # print each course in an aligned manner
        print(f'{course[0]:<7} {course[1]:8} {course[2]:<8} {course[3]:50} {course[4]:20} {course[5]:<6} {course[5] - course[6]:<10}')


def search_course(courses):
    print('\n\t1. By Course Number\n\t2. By Course Code\n\t3. By Course Name')      # print search menu
    opt = input('Enter your choice: ').strip()
    result = []

    if opt == '1':
        crn = input('Enter course CRN: ')

        for course in courses:
            if str(course[0]) == crn:                                               # if crn number found
                result.append(course)                                               # append course to resulting array

    elif opt == '2':
        code = input('Enter course Code: ')

        for course in courses:
            if course[1].lower() == code.lower():                                   # course code found
                result.append(course)

    elif opt == '3':
        name = input('Enter course name or part of it: ')

        for course in courses:
            if name.lower() in course[3].lower():                                   # name exists in course name
                result.append(course)

    else:
        print('Incorrect Option!')                                                  # invalid menu option
        return
    
    if len(result) > 0:                                                             # 1 or more resulting courses
        course_info(result)
    else:
        print('Course does not exist!')                                             # no courses found


def add_course(courses):

    while True:
        crn = input('Enter course CRN: ').strip()
        found = False
        if len(crn) != 5:                                                           # must have 5 digits
            print('Course number must be 5 digits')
            continue

        try:
            crn = int(crn)                                                          # try converting to number
        except ValueError:
            print('Course Number must be a valid number')                           # letter entered
            continue

        for course in courses:
            if course[0] == crn:                                                    # course number already exists
                found = True
                print('Serial Number already exists')
                break
        
        if not found:
            break
    
    print()
    while True:
        code = input('Enter course code: ').strip()
        if code != '':                                                              # course code is not empty
            break
        print('Course Code must not be empty')

    print()
    while True:
        try:
            sec = int(input('Enter Section Number: '))                      
            if sec > 0:                                                             # section number must be positive
                break
            print('Section Number must be positive and non-empty')                  # section number invalid
        except ValueError:
            print('Section Number must be positive and non-empty')                  # letter entered

    print()
    while True:
        name = input('Enter course name: ').strip()
        if name != '':                                                              # name is not empty
            break
        print('Course name must not be empty')

    print()
    while True:
        inst = input('Enter Instructor name: ').strip()
        if inst != '':                                                              # instructor name not empty
            break
        print('Instructor name must not be empty')

    print()
    while True:
        try:
            size = int(input('Enter Section Size: '))
            if size > 0:                                                            # section size must be positive
                break
            print('Section Size must be positive and non-empty')                    # invalid size
        except ValueError:
            print('Section Size must be positive and non-empty')                    # letter entered

    print('Course has been added successfully!!!')
    courses.append([crn, code, sec, name, inst, size, 0])                           # add course to existing courses


def remove_course(courses):
    try:
        crn = int(input('Enter course CRN: ').strip())
    except ValueError:
        print('Invalid CRN entered!')
        return

    index = 0
    for course in courses:
        if course[0] == crn:                                                        # if course number found
            course_info([course])                                                   # print course details

            if course[6] > 0:                                                       # course must have 0 registered students
                print('This course has registered students! Cannot be removed')
                break

            opt = input('Are you sure you want to remove this course [Y/N]? ').strip()
            if opt.lower() == 'y':
                courses.pop(index)                                                  # remove course from existing courses
                print('Course has been removed successfully :)')
                break
        index += 1
    else:
        print('Course does not exist!')                                             # no course found with entered CRN


def update_course(courses):
    try:
        crn = int(input('Enter course CRN: ').strip())
    except ValueError:
        print('Invalid CRN entered!')
        return

    index = 0
    for course in courses:
        if course[0] == crn:                                                        # if course found
            break
        index+=1
    else:
        print('Course does not exist')
        return

    print('\n\t1. Course Name\n\t2. Instructor\' Name\n\t3. Section size')          # print update menu
    opt = input('What would you like to update? ').strip()

    if opt == '1':
        while True:
            name = input('Enter course name: ').strip()
            if name != '':                                                          # course name must not be empty 
                break
            print('Course name must not be empty')
        course[index][3] = name                                                     # change course name for found CRN
        

    elif opt == '2':
        while True:
            inst = input('Enter Instructor name: ').strip()
            if inst != '':                                                          # instructor name must not be empty
                break
            print('Instructor name must not be empty')
        course[index][4] = inst                                                     # update instructor name

    elif opt == '3':
        while True:
            try:
                size = int(input('Enter Section Size: '))
                if size > 0:                                                        # section size must be positive
                    break
                print('Section Size must be positive and non-empty')
            except ValueError:
                print('Section Size must be positive and non-empty')
                
        courses[index][5] = size                                                    # update section size
        
    else:
        print('Incorrect Option!')                                                  # invalid menu option
        return
    
    print('Course has been updated successfully')


def register_student(courses, students):
    try:
        crn = int(input('Enter course CRN: ').strip())
    except ValueError:
        print('Invalid CRN entered!')
        return

    for course in courses:
        if course[0] == crn:                                                        # if course found

            if course[5] - course[6] == 0:                                          # no available space
                print('This course is full! Cannot register student')
                break
            
            course[6] += 1                                                          # increment registered students
            std_id = input('Enter Student\'s ID: ')
            std_name = input('Enter Student\'s name: ')

            found = False
            for student in students:
                if student[0] == crn and student[1] == std_id:                      # student already registered in course 
                    print(f'Student {student[1]} is already registered in this course')
                    found = True
                    break
            
            if found:                                                               # do not register if already exists
                break

            students.append([course[0], std_id, std_name])                          # add new student to already existing students
            print(f'Student {std_id}, {std_name} has been registered in {course[3]} Successfully!')
            break
    else:
        print('Course does not exist!')


def drop_student(courses, students):
    try:
        crn = int(input('Enter course CRN: ').strip())
    except ValueError:
        print('Invalid CRN entered!')
        return

    std_id = input('Enter Student\'s ID: ')
    index = 0

    for student in students:

        if student[0] == crn and student[1] == std_id:                              # if student found
            for course in courses:

                if course[0] == student[0]:                                         # if course found
                    opt = input('Are you sure you want to drop this student from this course [Y/N]? ').strip()
                    if opt.lower() == 'y':
                        course[6] -= 1                                              # decrement registered students
                        students.pop(index)                                         # remove student from existing students
                        print(f'Student {student[1]}, {student[2]} has been dropped from {course[3]} Successfully!')
                        break
            break
        index += 1
    else:
        print('Course does not exist or student is not registered in that course!')


def output_to_file(courses, students):

    file = open("coursesInfo.txt", "w")                         # open course file for writing (erasing previous data)
    for course in courses:
        curr = 0
        for item in course:
            file.write(str(item))                               # write each course detail, comma separated
            if curr != 6:                                       # do not write comma at end
                file.write(',')     
            curr += 1
        file.write('\n')                                        # write to next line
    file.close()                                                # close file

    file = open("registeredStudents.txt", "w")                  # open students file
    for student in students:
        curr = 0
        for item in course:                                     # write each students details to file
            file.write(str(item))                           
            if curr != 2:   
                file.write(',')
            curr += 1
        file.write('\n')
    file.close()
    

def read_files():
    courses = []                                                # list of courses
    students = []                                               # list of students
    correct = True                                              # data must be in correct format

    try:
        file = open("coursesInfo.txt")                          # open course file
        for line in file:
            course = line.strip().split(',')                    # split line by comma
            if len(course) != 7:                                # must have 7 items
                correct = False                                 # incorrect format
            course[0] = int(course[0])                          # course number is integer
            course[2] = int(course[2])                          # section number is integer
            course[5] = int(course[5])                          # section size is integer
            course[6] = int(course[6])                          # number of registered to students is integer
            courses.append(course)                              # add course to list
        file.close()

        file = open("registeredStudents.txt")                   # open student file
        for line in file:
            student = line.strip().split(',')
            if len(student) != 3:                               # must have 3 items
                correct = False                                 # incorrect format
            student[0] = int(student[0])                        # course number is integer
            students.append(student)                            # add student to list of students
        file.close()

    except (ValueError, IndexError):                            # incorrect data / format
        correct = False
    except FileNotFoundError:                                   # file does not exist
        return courses, students, correct                       # return empty lists
    
    return courses, students, correct                           # return list of courses and students


def main():

    courses, students, correct = read_files()                   # get course and student list

    if not correct:
        print('File in Incorrect format')                       # cannot perform further processing if data in incorrect format
        return

    while True:
        opt = menu()                                            # print and get menu option

        if opt == 1:                                            # display course information
            course_info(courses)

        elif opt == 2:                                          # search for courses
            search_course(courses)

        elif opt == 3:                                          # add a new course
            add_course(courses)

        elif opt == 4:                                          # remove a course
            remove_course(courses)

        elif opt == 5:                                          # update a course
            update_course(courses)

        elif opt == 6:                                          # register a new student
            register_student(courses, students)

        elif opt == 7:                                          # drop an existing student
            drop_student(courses, students)

        else:                                                   # exit menu
            print('\nProgram Finished!\n')
            break 
        print()
    
    output_to_file(courses, students)                           # output updated data to files after program finishes

if __name__ == "__main__":
    main()