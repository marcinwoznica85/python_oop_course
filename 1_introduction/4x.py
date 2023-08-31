"""
Write a class that will fit the usage shown below
"""


class Car:
    def __init__(self, brand: str, color: str) -> None:
        self.brand = brand
        self.color = color
        self.mileage = 0
    
    def print_mileage(self) -> None:
        print(self.mileage)

    def drive(self, kilometers: int) -> None:
        self.mileage += kilometers


car = Car(brand="Skoda", color="red")
car.print_mileage()  # should be 0
car.drive(kilometers=100)

print(f"My {car.brand} is {car.color} and drove for {car.mileage}")
