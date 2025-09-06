class ExampleClass:

    count = 0       #class variable

    def __init__(self):         #Constucter
        self.value = 1100       #instance variable
        ExampleClass.count += 1

    def set_prop(self):         #Adding a new instance property
        self.value2 = 120


test = ExampleClass()

test.set_prop()

print(test.value)

test2 = ExampleClass()
test3 = ExampleClass()
test4 = ExampleClass()
test5 = ExampleClass()

test2.set_prop()
print(test2.value2)

print(test.value)
print(test2.value2)
print(ExampleClass.count)