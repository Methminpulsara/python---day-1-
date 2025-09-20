class Student():
    def __init__(self , name , age , contact , course):
        self.name = name
        self.age = age
        self.contact = contact
        self.course = course

    def study(self):
        print(f"{self.name} is Studying")

    def __str__(self):
        return f"name - {self.name} age - {self.age}"


student_1 = Student("Methmin" , 18 , "07191989399", "IT")
student_2 = Student("Methmin" , 18 , "07191989399", "IT")


# str method ek override klama memory ref eke nameeyi pennanne api dhla thiyen print eka (str) method ekt
print(student_1)

if student_1 == student_2:
    print("both objects are equal")
else :
    print("in object values are equal but not ===>>>>  EQUAL MEMORY REFERENCES")