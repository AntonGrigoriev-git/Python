from model import Planets
from view import ConsoleView
from math import cos, sin


class ControllerPlanets:
    def __init__(self):
        self.planets = {}
        self.view = ConsoleView()

    def show_planets(self):
        for planet in self.planets:
            print(planet)

    def add_planet(self, name):
        if name not in self.planets:
            self.planets[name] = Planets(name)
        else:
            self.view.show_message(f'Планета "{name}" уже существует')

    def remove_planet(self, name):
        if name in self.planets:
            del self.planets[name]
        else:
            self.view.show_message(f'Планета "{name}" не найдена')

    def run_simulation(self, name, number_of_steps, time_step):
        if name not in self.planets:
            self.view.show_message(f'Планета "{name}" не найдена')
            return
        
        planet = self.planets[name]

        try:
            angular_velocity = planet.speed / planet.radius
        except ZeroDivisionError:
            self.view.show_message('Радиус орбиты не может быть нулевым')
            return

        for step in range(1, number_of_steps + 1):
            angle = angular_velocity * step * time_step
            x = planet.radius * cos(angle)
            y = planet.radius * sin(angle)
            self.view.show_message(f'Шаг {step}: Планета "{name}" на позиции x={x:.2f}, y={y:.2f}')