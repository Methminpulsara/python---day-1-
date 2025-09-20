class A:
    print("form a method")

class B(A):
     def a_method(self):
         print("Overriding a method from class B")

     def b_method(self):
         print("from b method")

class C(A):

    def a_method(self):
        print("Overriding a method form class c")

    def c_method(self):
        print("from c method")

class D(C , B):
    def d_method(self):
        print("from d method")

d_obj  = D()
d_obj.a_method()