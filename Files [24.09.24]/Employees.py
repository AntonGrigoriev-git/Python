

def add_data(name, surname, age, profession, description):
    with open('employees.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname}: {age} years old. Profession: {profession}. Description: {description}.\n')


def edit_data(target_surname, new_data):
    with open('employees.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        parts = line.split()
        if parts[1].replace(':', '') == target_surname:
            if 'new_name' in new_data:
                parts[0] = new_data['new_name']
            if 'new_surname' in new_data:
                parts[1] = new_data['new_surname'] + ':'
            if 'new_age' in new_data:
                parts[2] = new_data['new_age']
            if 'new_profession' in new_data:
                parts[6] = new_data['new_profession'] + '.'
            if 'new_description' in new_data:
                new_description_text = new_data['new_description'] + '.'
                parts = parts[:8] + [new_description_text]
            updated_line = ' '.join(parts)
            updated_lines.append(updated_line + '\n')
        else:
            updated_lines.append(line)

    with open('employees.txt', 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)



def delete_employee(target_surname):
    with open('employees.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open('employees.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            if target_surname not in line:
                file.write(line)


def search_employee(target_surname):
    with open('employees.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    employees = []
    for line in lines:
        surname = line.split()[1].replace(':', '')
        if surname == target_surname:
            employees.append(line.strip())
    
    return employees if employees else None



def show_info(target_age=None, target_initial=None):
    with open('employees.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            parts = line.split()
            age = parts[2]
            surname = parts[1].replace(':', '')
            if (target_age is not None and age == target_age) or\
               (target_initial is not None and surname.startswith(target_initial)):
                print(' '.join(parts))


def main():
    while True:
        print('1. Добавить сотрудника')
        print('2. Редактировать сотрудника')
        print('3. Удалить сотрудника')
        print('4. Найти сотрудника по фамилии')
        print('5. Показать всех сотрудников по возрасту или начальной букве фамилии')
        print('0. Выйти')
        choice = input('Введите номер действия: ')

        if choice == '1':
                name = input('Введите имя: ')
                surname = input('Введите фамилию: ')
                age = input('Введите возраст: ')
                profession = input('Введите профессию: ')
                description = input('Добавьте описание: ')
                add_data(name, surname, age, profession, description)

        elif choice == '2':
            target_surname = input('Введите фамилию сотрудника для редактирования: ')
            if search_employee(target_surname):

                changes = {}
                print('---------------------------------------------------------------')
                print('Какие данные вы хотите изменить? (введите номера через запятую)')
                print('1. Имя')
                print('2. Фамилия')
                print('3. Возраст')
                print('4. Профессия')
                print('5. Описание')

                choices = input('Ваш выбор: ').split(',')
                for choice in choices:
                    if choice.strip() == '1':
                        changes['new_name'] = input('Введите новое имя: ')
                    elif choice.strip() == '2':
                        changes['new_surname'] = input('Введите новую фамилию: ')
                    elif choice.strip() == '3':
                        changes['new_age'] = input('Введите новый возраст: ')
                    elif choice.strip() == '4':
                        changes['new_profession'] = input('Введите новую профессию: ')
                    elif choice.strip() == '5':
                        changes['new_description'] = input('Введите новое описание: ')

                edit_data(target_surname, changes)
            else:
                print('--------------------------------------------------')
                print('Введенная фамилия сотрудника в списке отсутствует.')

        elif choice == '3':
            target_surname = input('Введите фамилию сотрудника для удаления: ')
            if search_employee(target_surname):
                delete_employee(target_surname)
            else:
                print('--------------------------------------------------')
                print('Введенная фамилия сотрудника в списке отсутствует.')

        elif choice == '4':
            target_surname = input('Введите фамилию сотрудника для поиска: ')
            employee_info = search_employee(target_surname)
            if employee_info:
                print('--------------------------------------------------')
                for employee in employee_info:
                    print(employee)
            else:
                print('--------------------------------------------------')
                print('Введенная фамилия сотрудника в списке отсутствует.')

        elif choice == '5':
            choice = input('Вы хотите найти информацию по возрасту(1) или по начальной букве фамилии(0)? (1 | 0): ')
            if choice == '1':
                target_age = input('Ведите возраст: ')
                print('--------------------------------------------------')
                show_info(target_age=target_age)
            elif choice == '0':
                target_initial = input('Введите начальную букву фамилии: ')
                print('--------------------------------------------------')
                show_info(target_initial=target_initial)
            else:
                print('--------------')
                print('Неверный ввод.')

        elif choice == '0':
            break

        else:
            print('--------------------------------')
            print('Неверный ввод, попробуйте снова.')

main()