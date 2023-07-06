# Next, design a program that creates a Car object then calls the accelerate method five times. After each call to the accelerate method,
# get the current speed of the car and display it. Then call the brake method five times. After each call to the brake method, 
# get the current speed of the car and display it.
from Car import Car

# create a car 
car1 = Car(2023, 'Bugatti')
# accelerate the car 5 times and display the current speed of the car
for i in range(5):
    car1.acceleration()
    print("The current speed of the car is: ", car1.get_speed())
# brake the cake 5 times and display the current speed of the car
for i in range(5):
    car1.brake()
    print("The current speed of the car is: ", car1.get_speed())