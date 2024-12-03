class ConsoleView:
    @staticmethod
    def display_menu():
        print('1. Показать планеты')
        print('2. Добавить планету')
        print('3. Удалить планету')
        print('4. Запустить симуляцию')
        print('5. Выйти')

    @staticmethod
    def get_input(prompt):
        return input(prompt)
    
    @staticmethod
    def show_message(message):
        print(message)