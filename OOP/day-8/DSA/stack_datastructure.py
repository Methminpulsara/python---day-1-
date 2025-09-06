stack = []
stack2 = []

def push(value):
    return stack.append(value)

def pop():

    if is_empty() :
        return "Cant remove Elements !"
    value = stack[-1]
    del stack[-1]
    return value

def is_empty():
    return len(stack) == 0

push(1)
push(2)


print(stack)