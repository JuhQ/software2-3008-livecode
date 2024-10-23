class Car:
    def __init__(self, registration_number, maxSpeed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
        self.tires = 4
        self.transmission_type = ""

    def set_transmission_type(self, type):
        self.transmission_type = type

    def get_transmission_type(self):
        return self.transmission_type

    def accelerate_simpler(self, speed):
        if speed > self.max_speed:
            speed = self.maxSpeed
        elif speed < 0:
            speed = 0

        self.current_speed = speed

    def accelerate_my_solution(self, speed):
        if speed > self.max_speed:
            self.current_speed = self.maxSpeed
        elif speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = speed

    def increase_speed_by(self, speed):
        self.current_speed += speed

car = Car("ABC-123", 142)
car2 = Car("XYZ-987", 500)

def car_debug(car):
    print(f"Transmission type: {car.transmission_type} or {car.get_transmission_type()}")
    print(f"Reg number: {car.registration_number}")
    print(f"Max speed: {car.max_speed}")
    print(f"Current speed: {car.current_speed}")
    print(f"Travelled distance: {car.travelled_distance}")
    print("------------------------------------------")

car.accelerate(50)
car.accelerate(60)
car.accelerate(70)
car.accelerate(170)
car.accelerate(-200)
car_debug(car)
print("--------")


car.accelerate_my_solution(50)
car.accelerate_my_solution(60)
car.accelerate_my_solution(70)
car.accelerate_my_solution(170)
#car.accelerate_my_solution(-200)
car.set_transmission_type("Automatic")
car_debug(car)

car_debug(car2)
