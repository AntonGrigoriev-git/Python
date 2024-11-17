from abc import ABC, abstractmethod

# Component
class RestaurantMenu(ABC):
    @abstractmethod
    def info(self, indent=0):
        pass


# Leaf
class Dish(RestaurantMenu):
    def __init__(self, name: str, description: str, price: int):
        self.name = name
        self.description = description
        self.price = price

    def info(self, indent=0):
        print(' ' * indent + f'{self.name}. Description: {self.description}. Price: {self.price} rub')


#Composite
class Menu(RestaurantMenu):
    def __init__(self, name: str):
        self.name = name
        self._submenu = []

    def add(self, component: RestaurantMenu):
        self._submenu.append(component)

    def remove(self, component: RestaurantMenu):
        self._submenu.remove(component)

    def info(self, indent=0):
        print(' ' * indent + f'{self.name}')
        for child in self._submenu:
            child.info(indent + 4)

name = Menu('The Stone Age')
submenu = Menu('Submenu')
dish = Menu('Dishes')

submenu1 = Dish('Meat products', 'Hot dishes', 500)
dish2 = Dish('Beef', 'Beef tenderloin', 300)
dish3 = Dish('Poultry', 'Duck leg', 200)

name.add(submenu)
submenu.add(submenu1)
name.add(dish)
dish.add(dish2)
dish.add(dish3)

name.info()