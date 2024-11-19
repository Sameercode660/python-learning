class Car:
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.model = usermodel

my_car = Car("Toyota", "Corolla");

print(my_car.__brand)
print(my_car.model)