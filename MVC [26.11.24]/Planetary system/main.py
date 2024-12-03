from controller import ControllerPlanets

def main():
    controller = ControllerPlanets()
    
    while True:
        controller.view.display_menu()
        choice = controller.view.get_input('Выберите действие: ')

        if choice == '5':
            break

        elif choice == '1':
            print(list(controller.planets.keys()))
            details = controller.view.get_input('Хотите просмотреть характеристики планеты? y/n: ')
            if details == 'y':
                name = controller.view.get_input('Введите имя планеты: ')
                if name in controller.planets:
                    planet = controller.planets[name]
                    print(f'Радиус орбиты: {planet.radius}')
                    print(f'Скорость вращения: {planet.speed}')
                    print(f'Масса планеты: {planet.mass}')
                else:
                    controller.view.show_message(f'Планета "{name}" не найдена')

        elif choice == '2':
            name = controller.view.get_input('Введите имя планеты: ')
            controller.add_planet(name)

            try:
                radius = float(controller.view.get_input('Введите радиус орбиты: '))
                controller.planets[name].set_radius(radius)
            except ValueError:
                controller.view.show_message('Некорректный ввод радиуса')

            try:
                speed = float(controller.view.get_input('Введите скорость вращения: '))
                controller.planets[name].set_speed(speed)
            except ValueError:
                controller.view.show_message('Некорректный ввод скорости')

            try:
                mass = float(controller.view.get_input('Введите массу планеты: '))
                controller.planets[name].set_mass(mass)
            except ValueError:
                controller.view.show_message('Некорректный ввод массы')

        elif choice == '3':
            name = controller.view.get_input('Введите имя планеты: ')
            controller.remove_planet(name)

        elif choice == '4':
            name = controller.view.get_input('Введите имя планеты: ')

            try:
                number_of_steps = int(controller.view.get_input('Введите количество шагов симуляции: '))
                time_step = float(controller.view.get_input('Введите временной шаг: '))
                controller.run_simulation(name, number_of_steps, time_step)
            except ValueError:
                controller.view.show_message('Некорректный ввод числа шагов или временного шага')

        else:
            controller.view.show_message('Неверный выбор')

if __name__ == '__main__':
    main()