student = {"name" :  "methmin" ,
            "age" : 18 ,
           "address" : "horana",
           "school" : "ds",
           "contact" :  ["07213114", "071231231" , "0712323111"]
           }

print(student.get("name"))

student["maried_status"] = "yes"

print(student)

student["name"] = "test"

print("after change name , student name = " , student["name"])


print(student["contact"][2])

student["contact"].append("0719189399")

print("after adding new phone number " , student["contact"])

student["contact"].pop(0)
print(f"After drop student contact ", student["contact"])