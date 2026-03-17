# PROJECT CLASS CAR:

class Car:

    def __init__(self, brand, model, year):
        self.model = model
        self.brand = brand
        self.year = year
        self.engine_on = False
        self.speed = 0

    def drive(self):
        self.engine_on = True
        print("The car is driving")

    def stop(self):
        self.engine_on = False
        self.speed = 0
        print("The car is stopped")

    def accelerate(self, amount):
        if self.engine_on:
            self.speed += amount
            print("The car is now going", self.speed)

        else:
            print("The car is already stopped")

    def show_status(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Year :", self.year)
        print("Engine On :", self.engine_on)
        print("Speed :", self.speed)

c1 = Car("Toyota", "Corolla", "2022")
c2 = Car("BMW", "M3", "2024")

c1.drive()
c1.accelerate(30)
c1.show_status()

print()

c2.drive()
c2.accelerate(50)
c2.show_status()
