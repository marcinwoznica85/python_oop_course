"""
Reduce unnecessary coupling between Car and SkodaFabiaEngine
"""


class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.engine = SkodaFabiaEngine()

    def start(self) -> None:
        print(
            f"Starting {self.make} {self.model} powerful engine {self.engine.engine_size}"
        )

    def stop(self) -> None:
        print(f"Stopping {self.make} {self.model}")

    def honk(self) -> None:
        print(f"{self.make} {self.model} says honk honk!")


class SkodaFabiaEngine:
    def __init__(self) -> None:
        self.engine_size = 1.4
        self.engine_power = 60


car = Car(make="Skoda", model="Fabia", year=2001)
car.start()
