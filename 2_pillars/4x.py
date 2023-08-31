"""
Implement a Car class that extends __init__ method of Vehicle with parameter num_doors
Override get_details() method and include num_doors in return value
Create Car instance and get_details()
"""


class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def get_details(self) -> str:
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    ...
