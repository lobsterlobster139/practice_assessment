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
    for i in students:
        if i['e_credits'] >= 50:
            print(f"{i['name']} is eligible for Excellence endorsement ({i['e_credits']} excellence credits)")
        elif i['m_credits'] >= 50:
            print(f"{i['name']} is eligible for Merit endorsement ({i['m_credits']} merit credits)")

def students_in_year():
    target_year = int(input("What year would you like to view?: "))
    students_in_year = False
    print(f"Students in Year {target_year}:\n")
    for i in students:
        if i['year'] == target_year:
            students_in_year = True
            print(i['name'])
    if students_in_year == False:
        print(f"There are no students in Year {target_year}.")
 

def add_credits():
    pass

def add_student():
    pass

def main_menu():
    while True:
        choice = input("""What would you like to do? 
                       \na: Print a summary of all students 
                       \nb: Print a list of all students who have passed NCEA Level 1
                       \nc: Print a list of all students eligible for endorsement
                       \nd: Print a list of all students in a specificied year group
                        \n> """).lower()
        if choice == "a":
            summary()
        elif choice == "b":
            can_pass_ncea()
        elif choice == "c":
            can_be_endorsed()
        elif choice == "d":
            students_in_year()
        else:
            print("That isn't an option. Please re-input the corresponding letter.")

main_menu()