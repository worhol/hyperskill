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


print("Learning progress tracker")
students_id = []
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
                        student_id = (first_name + last_name + email).__hash__()
                        students_id.append(student_id)
                        new_students.append(student)
                        print("The student has been added.")
    else:
        print("Error: unknown command!")
