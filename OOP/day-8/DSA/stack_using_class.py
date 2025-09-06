class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        # use list.pop() — simpler and clearer
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class CountingStack(Stack):
    def __init__(self):
        super().__init__()      # <-- IMPORTANT: initializes self.stack
        self.__count = 0        # name-mangled "private" variable

    def pop(self):
        # Call parent pop(), let it raise if empty.
        val = super().pop()
        self.__count += 1       # only increment after a successful pop
        return val

    def get_count(self):
        return self.__count

cs = CountingStack()
cs.push(10)
cs.push(20)

print("Before popping:", cs.stack)    # => [10, 20]
print("Popped:", cs.pop())            # => 20
print("After popping:", cs.stack)     # => [10]
print("Pop count:", cs.get_count())   # => 1
