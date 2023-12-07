class Car:
    def __init__(self, brand, car_type, color):
        self.brand = brand
        self.type = car_type
        self.color = color

my_car = Car(brand="Toyota", car_type="Sedan", color="Blue")

print("Brand:", my_car.brand)
print("Type:", my_car.type)
print("Color:", my_car.color)
