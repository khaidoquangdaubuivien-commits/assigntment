class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Going up to floor {self.current}")
        else:
            print("Already at the top floor")

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Going down to floor {self.current}")
        else:
            print("Already at the bottom floor")

    def go_to_floor(self, target):
        if target < self.bottom or target > self.top:
            print("Invalid floor")
            return

        print(f"\nGoing to floor {target}")

        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()


#class BUILDING
class Building:
    def __init__(self, bottom, top, num_of_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []

        for i in range(num_of_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, target):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print("Invalid elevator number")
            return

        print(f"\nRunning elevator {elevator_number} to floor {target}")
        self.elevators[elevator_number].go_to_floor(target)
# FIRE ALARM
    def fire_alarm(self):
        for i in range(len(self.elevators)):
            print(f"\nSending elevator {i} to bottom floor")
            self.elevators[i].go_to_floor(self.bottom)

if __name__ == "__main__":
    b = Building(1, 10, 3)

    b.run_elevator(0, 5)
    b.run_elevator(1, 8)
    b.run_elevator(2, 3)
    b.run_elevator(0, 1)



