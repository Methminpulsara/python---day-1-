# from typing import List
#
# student_name : List[str] = ["methmin", "pulsar", "pupla "]
#
# student_name_iterator = iter(student_name)
#
# try:
#     print(student_name_iterator.__next__())
# except StopIteration as e :
#     print(e)


# class CountDown:
#
#     def __init__(self , num : int):
#         self.num = num
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.num = self.num -1
#         if self.num == 0:
#             raise StopIteration
#
#         return self.num
#
# for number in CountDown(10):
#     print(number)


class NumberGenerator:
    def __init__(self, num: int):
        self.num = num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.num:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


for number in NumberGenerator(10):
    print(number)
