
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

