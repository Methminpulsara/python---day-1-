from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    name : str
    age : int
    contact : str
    course : str
    grades : List[int]

    def add_grade(self, grade:int) -> None:
        self.grades.append(grade)

    def get_avg(self) -> float:
        if len(self.grades) == 0 :
            return sum(self.grades) / len(self.grades)

student = Student("Methmin"  ,18 , "0719189399" , "It" , 10)

print(student)