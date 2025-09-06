class Stack:


    #THIS IS CONSTRUCTOR

    def __init__(self):
        self.stack = []

    def push(self , element ):
        return self.stack.append(element)

    def pop(self):
        if not self.is_emplty():
            value = self.stack[-1]
            del self.stack[-1]
            return value


    def is_emplty(self):
        if len(self.stack) == 0 :
            raise Exception("Stack is Empty")


st_1 = Stack()
st_2 = Stack()


st_1.push("Stack 1")
st_1.push("removed 1")
st_2.push("Stack 2")
st_2.push("removed 2")

print(f"Stack 1 -  {st_1.stack}")
print(f"Stack 2 -  {st_2.stack}")


print(f"{st_1.pop() , st_2.pop()}")

print("After Remove")

print(f"Stack 1 -  {st_1.stack}")
print(f"Stack 2 -  {st_2.stack}")

