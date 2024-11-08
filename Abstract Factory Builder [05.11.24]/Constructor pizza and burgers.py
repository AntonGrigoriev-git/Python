class Pizza:
    def __init__(self):
        self.dough = None
        self.size = None
        self.sauce = None
        self.filling = None

    def display(self):
           print('Pizza Configuration:')
           print(f'  Dough: {self.dough}')
           print(f'  Size: {self.size}')
           print(f'  Sauce: {self.sauce}')
           print(f'  Filling: {self.filling}')


class Burger:
    def __init__(self):
        self.bun_type = None
        self.cutlet = None
        self.additives = None

    def display(self):
           print('Burger Configuration:')
           print(f'  Bun Type: {self.bun_type}')
           print(f'  Cutlet: {self.cutlet}')
           print(f'  Additives: {self.additives}')


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self, dough: str = 'thin'):
        self.pizza.dough = dough
        return self

    def build_size(self, size: str = 'average'):
        self.pizza.size = size
        return self

    def build_sauce(self, sauce: str = 'tomato'):
        self.pizza.sauce = sauce
        return self

    def build_filling(self, filling: str = 'mozzarella'):
        self.pizza.filling = filling
        return self

    def get_pizza(self):
           return self.pizza
    

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def build_bun_type(self, bun_type: str = 'classic'):
        self.burger.bun_type = bun_type
        return self

    def build_cutlet(self, cutlet: str = 'beef'):
        self.burger.cutlet = cutlet
        return self

    def build_additives(self, additives: str = 'cheese'):
        self.burger.additives = additives
        return self

    def get_burger(self):
           return self.burger


class Director:
    def construct_standard_pizza(self) -> Pizza:
        builder = PizzaBuilder()
        builder.build_dough()\
            .build_size()\
            .build_sauce()\
            .build_filling()
        return builder.get_pizza()

    def construct_custom_pizza(self, dough, size, sauce, filling) -> Pizza:
        builder = PizzaBuilder()
        builder.build_dough(dough)\
            .build_size(size)\
            .build_sauce(sauce)\
            .build_filling(filling)
        return builder.get_pizza()

    def construct_standard_burger(self) -> Burger:
        builder = BurgerBuilder()
        builder.build_bun_type()\
            .build_cutlet()\
            .build_additives()
        return builder.get_burger()

    def construct_custom_burger(self, bun_type, cutlet, additives) -> Burger:
        builder = BurgerBuilder()
        builder.build_bun_type(bun_type)\
            .build_cutlet(cutlet)\
            .build_additives(additives)
        return builder.get_burger()


def main():
    director = Director()

    choice = input('Хотите создать стандартный или пользовательский продукт? (standard/custom): ').strip().lower()

    if choice == 'standard':
        product = input('Что создать? pizza/burger: ').strip().lower()

        if product == 'pizza':
            pizza = director.construct_standard_pizza()
            pizza.display()

        elif product == 'burger':
            burger = director.construct_standard_burger()
            burger.display()
        else:
            print('Неизвестный продукт.')
            
    elif choice == 'custom':
        product = input('Что создать? pizza/burger: ').strip().lower()

        if product == 'pizza':
            dough = input('Выберите тесто (thin/thick): ').strip().lower()
            size = input('Выберите размер (little/average/big): ').strip().lower()
            sauce = input('Выберите соус (tomato/creamy): ').strip().lower()
            filling = input('Выберите начинку (mozzarella/pepperoni/mushrooms): ').strip().lower()
            pizza = director.construct_custom_pizza(dough, size, sauce, filling)
            pizza.display()

        elif product == 'burger':
            bun_type = input('Выберите тип булочки (classic/rye/gluten-free): ').strip().lower()
            cutlet = input('Выберите котлету (beef/chicken/vegetable): ').strip().lower()
            additives = input('Выберите добавки (cheese/bacon/salad/tomatoes): ').strip().lower()
            burger = director.construct_custom_burger(bun_type, cutlet, additives)
            burger.display()
        else:
            print('Неизвестный продукт.')
    else:
        print('Неверный выбор.')

main()