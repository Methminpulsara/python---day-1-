class Car:

    def __init__(self , model , manufacture_year , color , fuel_type):
        self.model = model
        self.manufacture_year = manufacture_year
        self.color = color
        self.fuel_type = fuel_type

    def __str__(self): #Overriding Object class String method
        return f"Car Model {self.model} | Car Manufacture Year - {self.manufacture_year}"

    def __eq__(self,__value):
        return self.model == __value.model

    def compare(self , object2):
        return self.model == object2.model and self.color == object2.color

    def move_car(self):
        print(f"{self.model} is Moving")

    def stop(self):
        print(f"{self.model} stop ! ")
    def open_doors(self):
        print(f"{self.model} is opening doors")

car_1 = Car("BMW", "2000", "Black", "Diesel")
car_2 = Car("Benz", "2010", "White", "Diesel")
car_3 = Car("BMW", "2005", "Black", "Petrol")

print(car_1.compare(car_2))  # False (different model and color)
print(car_1.compare(car_3))  # True (same model and same color)





car_1.move_car()
car_1.stop()
car_1.open_doors()
print("-----------------")

print("-----------------")


print(car_1.__str__())

# HOW TO CHECK Properties in the object
print(hasattr(car_1 , "model"))

print(car_1.__dict__.keys())

if "model" in car_1.__dict__.keys():
    print("yes model is in the tesla object")

