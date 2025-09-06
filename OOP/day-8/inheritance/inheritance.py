class Vehicle:

    def __init__(self , model , manufacture_year , color , fuel_type):
        self.model = model
        self.manufacture_year = manufacture_year
        self.color = color
        self.fuel_type = fuel_type

    def go(self):
        print(f"{self.model} is moving")

    def stop(self):
        print(f" {self.model} is stopping! ")

# ========================================================================================# ========================================================================================

class LandVehicle(Vehicle):
    def __init__(self, model, manufacture_year, color, fuel_type , no_of_wheels):
        Vehicle.__init__(self, model, manufacture_year, color, fuel_type)
        self.no_of_wheels = no_of_wheels

    def chech_tyre_preassure(self):
        print(f"Checking tyre pressure")

land = LandVehicle("Bakooo", 2010  , "orange", "Petral" , 8)

print("Land Vehicle")
land.go()
land.stop()
land.chech_tyre_preassure()
print("-----------------------")

# ========================================================================================# ========================================================================================

class Car(LandVehicle):
    def __init__(self, model, manufacture_year, color, fuel_type, no_of_wheels , body_type):
        super().__init__(model, manufacture_year, color, fuel_type, no_of_wheels)
        self.body_type = body_type

    def check_body_type(self):
        print(f"{self.model} what is your body type ? ")

car = Car("Bmw"  , 2020 , "red" , "Diesel" , 4 , "I know")

car.go()
car.stop()
car.chech_tyre_preassure()

# ========================================================================================# ========================================================================================
