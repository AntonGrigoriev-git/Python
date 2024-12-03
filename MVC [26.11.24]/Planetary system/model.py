class Planets:
    def __init__(self, name):
        self.name = name
        self.radius = 0.0
        self.speed = 0.0
        self.mass = 0.0

    def set_radius(self, radius):
        self.radius = float(radius)

    def set_speed(self, speed):
        self.speed = float(speed)

    def set_mass(self, mass):
        self.mass = float(mass)