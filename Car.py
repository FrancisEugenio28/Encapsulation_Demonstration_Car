# create a class called car
class Car:
# create a constructor with data attributes of year model, make, and assign speed at constant 0
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
# create a method for acceleration
    def acceleration(self):
        self.__speed += 5
# create a method for brake
    def brake(self):
        self.__speed -= 5
# return speed
    def get_speed(self):
        return self.__speed

car1 = Car(2022, "Suzuki")
car1.acceleration()
print("Current speed: ", car1.get_speed())