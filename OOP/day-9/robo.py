class Waiter:
    def waiter(self):
        print("im Waiter")

class Singer:
    def sing(self):
        print("im Singer")

class Cook:
    def cook(self):
        print("im cooking")

class Robo(Waiter , Singer , Cook):
    pass

robo = Robo() 

robo.cook()
robo.sing()
robo.waiter()