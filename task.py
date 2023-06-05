import re


def check_apostrophe(name: str):
    return name.startswith("'") or name.endswith("'") or name.startswith('-') or name.endswith(
        '-') or "-'" in name or "'-" in name or '--' in name or "''" in name
    #     pattern = r"^(\'|\-|(\-\'|\'\-)|--|'')|\b(\'|\-|(\-\'|\'\-)|--|'')\b"


def check_ascii(word: str):
    pattern = r'^[A-Za-z\' -]+$'
    return bool(re.search(pattern, word))


def check_email(address):
    pattern = r'^[a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]*\.[a-zA-Z0-9]{1,}$'
    return bool(re.search(pattern, address))


def check_length(word):
    return len(word) > 1


def statistics():
    most_popular = "n/a"
    least_popular = "n/a"
    highest_activity = "n/a"
    lowest_activity = "n/a"
    easiest_course = "n/a"
    hardest_course = "n/a"

    print("Most popular:", most_popular)
    print("Least popular:", least_popular)
    print("Highest activity:", highest_activity)
    print("Lowest activity:", lowest_activity)
    print("Easiest course:", easiest_course)
    print("Hardest course:", hardest_course)

    while True:
        course_input = input()
        if course_input == "back":
            break
        if course_input in course_counter().keys():
            print(f"{course_input}")
            print(f"id{'':<10}points{'':<5}completed")
            for stu in all_students:
                if stu[course_input] > 0:
                    print(
                        f"{stu['student id']}{'':<7}{stu[course_input]}{'':<9}{round((stu[course_input] / 600) * 100, 1)}%")


def course_counter():
    python_enrollment = sum((lambda students: 1 if student['Python'] > 0 else 0)(student) for student in all_students)
    dsa_enrollment = sum((lambda students: 1 if student['DSA'] > 0 else 0)(student) for student in all_students)
    databases_enrollment = sum(
        (lambda students: 1 if student['Databases'] > 0 else 0)(student) for student in all_students)
    flask_enrollment = sum((lambda students: 1 if student['Flask'] > 0 else 0)(student) for student in all_students)

    courses = {'Python': python_enrollment, 'DSA': dsa_enrollment, 'Databases': databases_enrollment,
               'Flask': flask_enrollment}
    return courses


print("Learning progress tracker")
students_id = []
all_students = []
while True:
    new_students = []
    user_input = input()
    if user_input == "exit":
        print("Bye!")
        break
    elif user_input == 'back':
        print("Enter 'exit' to exit the program")
    elif user_input == "list":
        print("Students:")
        if len(students_id) > 0:
            for ids in students_id:
                print(ids)
        else:
            print("No students found")
    elif user_input == "add points":
        print("Enter an id and points or 'back' to return")
        while True:
            points_input = input()
            if points_input == "back":
                break
            points_input_parts = points_input.split()
            if len(points_input_parts) == 5:
                st_id = 0
                python = 0
                dsa = 0
                databases = 0
                flask = 0
                if points_input_parts[0].isdigit():
                    st_id = int(points_input_parts[0])
                else:
                    print("Incorrect points format")
                if points_input_parts[1].isdigit():
                    python = int(points_input_parts[1])
                else:
                    print("Incorrect points format")
                if points_input_parts[2].isdigit():
                    dsa = int(points_input_parts[2])
                else:
                    print("Incorrect points format")
                if points_input_parts[3].isdigit():
                    databases = int(points_input_parts[3])
                else:
                    print("Incorrect points format")
                if points_input_parts[4].isdigit():
                    flask = int(points_input_parts[4])
                else:
                    print("Incorrect points format")
                if st_id not in students_id:
                    print(f"No student is found for id={points_input_parts[0]}")
                elif len(points_input_parts) != 5 or python < 0 or dsa < 0 or databases < 0 or flask < 0:
                    print("Incorrect points format")
                else:
                    student_found = False
                    for student in all_students:
                        if student['student id'] == st_id:
                            student['Python'] += python
                            student['DSA'] += dsa
                            student['Databases'] += databases
                            student['Flask'] += flask
                            print("Points updated")
                            student_found = True
                            break

                    if not student_found:
                        student_points = {'student id': st_id, 'Python': python, 'DSA': dsa, "Databases": databases,
                                          'Flask': flask}

                        all_students.append(student_points)
                        print("Points updated")
            else:
                print("Incorrect points format")
    elif user_input == "statistics":
        print("Type the name of a course to see details or 'back' to quit")
        statistics()
    elif user_input == "find":
        print("Enter an id or 'back' to return:")
        while True:
            find_input = input()
            if find_input == "back":
                break
            if find_input.isdigit():
                find_id = int(find_input)
                for s in all_students:
                    if s['student id'] == find_id:
                        print(
                            f"{s['student id']} points: Python={s['Python']}; DSA={s['DSA']}; Databases={s['Databases']}; "
                            f"Flask={s['Flask']}")
                else:
                    print(f"No student is found for id={find_input}.")
            else:
                print(f"No student is found for id={find_input}.")

    elif user_input.strip() == "":
        print("No input.")
    elif user_input == "add students":
        print("Enter student credentials or 'back' to return")

        while True:
            student = {}
            student_credentials = input()
            if student_credentials == 'back':
                print(f"Total {len(new_students)} students have been added")
                break
            parts = student_credentials.split()
            if len(parts) < 3:
                print("Incorrect credentials")
            if len(parts) > 2:
                first_name = parts[0]
                last_name = " ".join(parts[1:-1])
                email = parts[-1]
                errors_found = False
                if check_apostrophe(first_name) or not check_length(first_name) or not check_ascii(first_name):
                    print("Incorrect first name")
                    errors_found = True
                if check_apostrophe(last_name) or not check_length(last_name) or not check_ascii(last_name):
                    print("Incorrect last name")
                    errors_found = True
                if not check_email(email):
                    print("Incorrect email")
                    errors_found = True
                if not errors_found:
                    for st in new_students:
                        if email == st['email']:
                            print("This email is already taken.")
                            break
                    else:
                        student = {'first_name': first_name, 'last_name': last_name, 'email': email}
                        student_id = (first_name + last_name + email).__hash__() % 100000
                        students_id.append(abs(student_id))
                        new_students.append(student)
                        print("The student has been added.")
    else:
        print("Error: unknown command!")
