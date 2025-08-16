currunt_year = int(input("Enter current year : "))
birth_year = int(input("Enter your Birth year : "))

def cal_age(currunt_year, birth_year):
    age = currunt_year - birth_year
    if age <= 13:
       return child(age)
    if age <= 20:
       return teen(age)
    if age <= 50:
       return adult(age)


def child(age):
    print("Child")

def teen(age):
    print("Teen")

def adult(age):
    print("Adult")

cal_age(currunt_year, birth_year)
