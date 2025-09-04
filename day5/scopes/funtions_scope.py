# first step ===================
def test_scope():
    print("I know you",x)

x = 100
#
# test_scope()

# Second step ===================

def test_scope2():
    z = 20
    print("z in the funtion" , z)

z = 100

# test_scope2()
# print("z in the global" , z)


# Third step change global scope variable in the funtion

def test_scope3():
    global z
    z=10
    print(z)

print(z)
test_scope3()