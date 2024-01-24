
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

