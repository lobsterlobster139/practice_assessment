student_1 = {
    'name' : "Amelia Tcudzevich",
    'year' : 12,
    'a_credits' : 40,
    'm_credits' : 34,
    'e_credits' : 92
}

student_2 = {
    'name' : "Audrey Austin",
    'year' : 12,
    'a_credits' : 90,
    'm_credits' : 10,
    'e_credits' : 3
}

students = [student_1, student_2]

def summary():
    for i in students:
        print(f"Name: {i['name']} \nYear: {i['year']} \nTotal Credits: {i['a_credits'] + i['m_credits'] + i['e_credits']}\n\n")

def can_pass_ncea():
    for i in students:
        total_credits = i['a_credits'] + i['m_credits'] + i['e_credits']
        if total_credits >= 80:
            print(f"{i['name']} ({i['a_credits'] + i['m_credits'] + i['e_credits']} Total Credits)")

def can_be_endorsed():
    pass

def students_in_year():
    pass

def add_credits():
    pass

def add_student():
    pass

def main_menu():
    while True:
        choice = input("What would you like to do? \na: Print a summary of all students \nb: Print a list of all students who have passed NCEA Level 1\n>").lower()
        if choice == "a":
            summary()
        elif choice == "b":
            can_pass_ncea()
        else:
            print("That isn't an option. Please re-input the corresponding letter.")

main_menu()