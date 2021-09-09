class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def turn(self, direction):
        print(f"{self.model} turning {direction}")
        self.alert()

    def alert(self):
        print("alert")


class SportCar(Car):
    def beep(self):
        print("sports car beep")


my_car = SportCar("test_make", "test_model")

my_car.turn("left")
my_car.beep()