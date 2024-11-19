# class variable

class Car:
    CarCount = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.CarCount += 1
    

safari = Car('Tata', "Safari")
safari1 = Car('Tata', 'Nexon')
safari1 = Car('Tata', 'Nexon')
safari1 = Car('Tata', 'Nexon')

print(safari.CarCount)