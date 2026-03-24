import random

class Car:
    def __init__(self, registrationnumber, maximumspeed):
        self.registrationnumber = registrationnumber
        self.maximumspeed = maximumspeed
        self.currentspeed = 0
        self.travelleddistance = 0

    def accelerate(self, changeofspeed):
        self.currentspeed += changeofspeed
        if self.currentspeed > self.maximumspeed:
            self.currentspeed = self.maximumspeed
        if self.currentspeed < 0:
            self.currentspeed = 0

    def drive(self, numberofhours):
        self.travelleddistance += self.currentspeed * numberofhours

if __name__ == "__main__":
    car1 = Car("ABC-123", 142)

    print(car1.registrationnumber)
    print(car1.maximumspeed)
    print(car1.currentspeed)
    print(car1.travelleddistance)

    car1.accelerate(30)
    car1.accelerate(70)
    car1.accelerate(50)
    print("Current speed:", car1.currentspeed)

    car1.accelerate(-200)
    print("Final speed:", car1.currentspeed)

    car1.accelerate(60)
    car1.drive(1.5)

    print("Distance after driving:", car1.travelleddistance)

    cars = []

    for i in range(1, 11):
        max_speed = random.randint(150, 200)
        car = Car(f"ABC-{i}", max_speed)
        cars.append(car)

    race_on = True
    hours = 0

    while race_on:
        hours += 1

        for car in cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

            if car.travelleddistance >= 10000:
                race_on = False

    print("\n=== RACE RESULT ===")
    print(f"Race finished in {hours} hours\n")

    print(f"{'Car':<10}{'MaxSpeed':<10}{'Speed':<10}{'Distance':<15}")
    for car in cars:
        print(f"{car.registrationnumber:<10}{car.maximumspeed:<10}{car.currentspeed:<10}{car.travelleddistance:<15.2f}")
