student_1 = {
    'NSN' : 324124989,
    'name' : "Amelia Tcudzevich",
    'year' : 12,
    'a_credits' : 40,
    'm_credits' : 34,
    'e_credits' : 92
}

student_2 = {
    'NSN' : 441236969,
    'name' : "Audrey Austin",
    'year' : 12,
    'a_credits' : 90,
    'm_credits' : 10,
    'e_credits' : 3
}

students = [student_1, student_2]

def summary():
    for i in students:
        print(f"NSN: {i['NSN']}\nName: {i['name']} \nYear: {i['year']} \nTotal Credits: {i['a_credits'] + i['m_credits'] + i['e_credits']}\n\n")

def can_pass_ncea():
    for i in students:
        total_credits = i['a_credits'] + i['m_credits'] + i['e_credits']
        if total_credits >= 80:
            print(f"(NSN: {i['NSN']}) {i['name']} ({i['a_credits'] + i['m_credits'] + i['e_credits']} Total Credits)")

def can_be_endorsed():
    for i in students:
        if i['e_credits'] >= 50:
            print(f"(NSN: {i['NSN']}) {i['name']} is eligible for Excellence endorsement ({i['e_credits']} excellence credits)")
        elif i['m_credits'] >= 50:
            print(f"(NSN: {i['NSN']}) {i['name']} is eligible for Merit endorsement ({i['m_credits']} merit credits)")

def students_in_year():
    while True:
        try:
            target_year = int(input("What year would you like to view?: "))
            if target_year <= 13 and target_year >= 1:
                break
            else:
                print("Not a valid year group.")
        except ValueError:
            print("Please input only integers.")


    students_in_year = False
    print(f"Students in Year {target_year}:\n")
    for i in students:
        if i['year'] == target_year:
            students_in_year = True
            print(f"(NSN: {i['NSN']}) {i['name']}")
    if students_in_year == False:
        print(f"There are no students in Year {target_year}.")
 

def add_credits():
    student_found = False
    while True:
        try:
            student_NSN = int(input("Please search what student you would like to add credits to by NSN: "))
            break
        except ValueError:
            print("Please enter only integers.")

    for i in students:
        if i['NSN'] == student_NSN:
            student_found = True
            while True:
                try:
                    credits_added = int(input("Input how many credits you would like to add: "))
                    if credits_added < 0:
                        print("Invalid credit amount. Please try again.")
                    elif credits_added > 60:
                        print("Too many credits added at once. Please re-input.")
                    else:
                        break
                    
                except ValueError:
                    print("Please enter only integers.")
            while True:
                credits_type = input("Input what type of credits you would like to add (a,m,e): ")
                if credits_type == "a":
                    i['a_credits'] += credits_added
                    break
                elif credits_type == "m":
                    i['m_credits'] += credits_added
                    break
                elif credits_type == "e":
                    i['e_credits'] += credits_added
                    break
                else:
                    print("Not a valid type of credit. Please enter only 'a','m', or 'e'.")
    if student_found == False:
        print(f"No student found under NSN {student_NSN}")
        

def add_stu_input_validation(text):
    while True:
        try:
            num = int(input(text))
            if num >= 0:
                return num
            else:
                print("Invalid number.")
        except ValueError:
            print("Please input only integers.")




def add_student():
    nsn = add_stu_input_validation("Please input the NSN of the new student: ")
    name = input("Please input the first and last name of the new student: ")
    year = add_stu_input_validation("Please input the year group of the new student: ")
    a_credits = add_stu_input_validation("Please input how many achieved credits the student already has: ")
    m_credits = add_stu_input_validation("Please input how many merit credits the student already has: ")
    e_credits = add_stu_input_validation("Please input how many excellence credits the student already has: ")
    students.append({'NSN' : nsn, 'name' : name, 'year': year, 'a_credits' : a_credits, 'm_credits' : m_credits, 'e_credits' : e_credits})
    print("Student added!")


def main_menu():
    while True:
        choice = input("""What would you like to do?\n 
a: Print a summary of all students 
b: Print a list of all students who have passed NCEA Level 1
c: Print a list of all students eligible for endorsement
d: Print a list of all students in a specificied year group
e: Add credits to a student by their NSN number
f: Add a new student
g: Exit the program
                        \n> """).lower()
        if choice == "a":
            summary()
        elif choice == "b":
            can_pass_ncea()
        elif choice == "c":
            can_be_endorsed()
        elif choice == "d":
            students_in_year()
        elif choice == "e":
            add_credits()
        elif choice == "f":
            add_student()
        elif choice == "g":
            break
        else:
            print("That isn't an option. Please re-input the corresponding letter.")

main_menu()