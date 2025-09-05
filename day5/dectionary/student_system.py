students = {}

def add_student(student_id , name , age , address , contact):
    if student_id in students:
        print("Student Id in the System")
    else:
        student = {
            "name" : name,
            "age" :  age,
            "address" : address,
            "contact" : contact
        }
        students[student_id] = student

        print(students)

def update_student(student_id , new_name):
    if student_id in students:
        students[student_id]["name"] = new_name
        print(students[student_id])
    else:
        print("Student Not in the System ")

def add_marks(student_id):
    if student_id in students:
       maths = int(input("Enter Your Maths Marks : "))
       science = int(input("Enter Your Maths Marks : "))

       students[student_id]["marks"] = {
           "maths" : maths,
           "science" : science
       }
       print(f"Marks Added sussesfully ! for {students[student_id]} ")


while True:
    print("""
    Student Management System
    =========================
    press 1 To add Student 
    press 2 to update Student Name
    press 3 to add marks
    """)
    choise = int(input("Enter your choise :  "))
    if choise == 1 :
        user_inputs = []
        for filed in ["student ID" , "name" , "age"  , "address" , "contact"]:
            user_input = input(f"Enter your {filed} : ")
            user_inputs.append(user_input)
        student_id , name , age , address , contact = user_inputs

        add_student(student_id , name , age , address , contact)

    if choise == 2 :
        student_id = input("Enter your id : ")
        name = input("Enter Your Name : ")

        update_student(student_id , name)

    if choise == 3 :
        student_id = input("Enter Your Id : ")
        if student_id in students:
            add_marks(student_id)
        else:
            print("Student not in the system ! ")