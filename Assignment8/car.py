import random

class Car:
    def __init__(self, reg_number, max_speed):
        self.reg = reg_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours


#RACE CLASS
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\n=== {self.name} ===")
        print(f"{'Car':<10} {'Speed':<10} {'Distance':<10}")

        for car in self.cars:
            print(f"{car.reg:<10} {car.speed:<10} {car.distance:<10}")

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False


if __name__ == "__main__":
    cars = []

    for i in range(10):
        reg = f"ABC-{i+1}"
        max_speed = random.randint(100, 200)
        cars.append(Car(reg, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0

    while not race.race_finished():
        hours += 1
        race.hour_passes()

        if hours % 10 == 0:
            race.print_status()


    race.print_status()