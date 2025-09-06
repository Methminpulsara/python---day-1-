class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")

        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0

    def pop(self):

        val = super().pop()
        self.__count += 1
        return val

    def get_count(self):
        return self.__count

cs = CountingStack()

cs.push(1)
cs.push(1)
cs.push(1)
cs.push(1)
cs.push(1)
cs.push(1)
cs.push(1)
cs.push(1)

cs.pop()
cs.pop()
cs.pop()
cs.pop()

print(cs.get_count())
print(cs.stack)


class SumCalculate(CountingStack):

    def __init__(self):
        super().__init__()
        self.__sum_of_ele = 0

    def push(self, element):
        super().push(element)
        self.__sum_of_ele += element

    def pop(self):
        element = super().pop()
        if element is not None:
            self.__sum_of_ele -= element
        return element

    def get_sum(self):
        return self.__sum_of_ele


sc = SumCalculate()

sc.push(10)
sc.push(1)
sc.push(1)
sc.push(1)
sc.push(1)

sc.pop()
sc.pop()
sc.pop()

print(f"Poping count -  {sc.get_count()}")
print(f"After Remove - {sc.stack}")
print(f"After Calculating sum {sc.get_sum()}")
