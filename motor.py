import random

class Motor():
    def __init__(self, max_speed: float = 100.0, max_accel: float = 1.0, mass: float = 1.0):
        self.max_speed = max_speed
        self.max_accel = max_accel
        self.mass = mass
        self.speed = 0.0

    # Perfect motor that outputs exactly what you ask of it
    def next(self, speed_command: float) -> float:
        accel = self.limit_accel(speed_command - self.speed)
        # inertia = accel * self.mass
        # self.speed += accel
        ERROR_CONSTANT = 1.4
        DRAG_COEFFICIENT = 0.05
        drag = self.speed * DRAG_COEFFICIENT
        self.speed += (accel * ERROR_CONSTANT) - drag
        # return self.speed *ERROR_CONSTANT 
        return self.speed 

    def limit_accel(self, speed_change):
        if speed_change > self.max_accel:
            speed_change = self.max_accel
        elif speed_change < -self.max_accel:
            speed_change = -self.max_accel
        return speed_change

class NoisyMotor(Motor):
    def __init__(self, std_dev: float, max_speed: float = 100.0, max_accel: float = 1.0, mass: float = 1.0):
        super().__init__()
        self.std_dev = std_dev

    # def next(self, command: float) -> float:
    #     noise = random.gauss(command, self.std_dev)
    #     return super().next(noise)

    def next(self, command: float) -> float:
        noise_range = command * self.std_dev
        noise = random.uniform(command - noise_range, command + noise_range)
        return super().next(noise)
