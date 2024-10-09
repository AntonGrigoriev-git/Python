from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, role, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.role = role
        self.assigned_tasks = []
        
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def role(self):
        pass

    @role.setter
    @abstractmethod
    def role(self, value):
        pass

    @abstractmethod
    def work(self):
        pass

    def assign_task(self, task):
        """Назначает задачу сотруднику."""
        self.assigned_tasks.append(task)
        task.employee = self

    def complete_task(self, task):
        """Отмечает задачу как выполненную."""
        if task in self.assigned_tasks:
            task.status = 'Completed'
        else:
            print(f"Task '{task.title}' is not assigned to {self.name}.")

    def get_completed_tasks_count(self):
        """Возвращает количество выполненных задач."""
        return len([task for task in self.assigned_tasks if task.status == 'Completed'])

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.get_completed_tasks_count() == other.get_completed_tasks_count()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.get_completed_tasks_count() < other.get_completed_tasks_count()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.get_completed_tasks_count() > other.get_completed_tasks_count()
        return NotImplemented

    def __str__(self):
        return f"{self.name} ({self.role})"


class ProgrammingLanguages:
    def __init__(self, programming_languages=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if programming_languages is None:
            programming_languages = []
        self.programming_languages = programming_languages

    @property
    def programming_languages(self):
        return self._programming_languages.copy()
    
    @programming_languages.setter
    def programming_languages(self, languages):
        if not isinstance(languages, list):
            raise ValueError("Programming languages should be provided as a list.")
        self._programming_languages = languages

    def add_language(self, language):
        if language not in self._programming_languages:
            self._programming_languages.append(language)

    def remove_language(self, language):
        if language in self._programming_languages:
            self._programming_languages.remove(language)


class Developer(Employee, ProgrammingLanguages):
    def __init__(self, name, role, programming_languages=None, *args, **kwargs):
        super().__init__(
            name=name,
            role=role,
            programming_languages=programming_languages,
            *args, **kwargs
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def work(self):
        languages = ', '.join(self.programming_languages)
        return f"{self.role} {self.name} is programming in {languages}."


class Tester(Employee, ProgrammingLanguages):
    def __init__(self, name, role, programming_languages=None, *args, **kwargs):
        super().__init__(
            name=name,
            role=role,
            programming_languages=programming_languages,
            *args, **kwargs
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def work(self):
        languages = ', '.join(self.programming_languages)
        return f"{self.role} {self.name} is testing in {languages}."


class Manager(Employee):
    def __init__(self, team_size=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.team_size = team_size

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    @property
    def team_size(self):
        return self._team_size

    @team_size.setter
    def team_size(self, value):
        if not isinstance(value, int):
            raise TypeError("Team size must be an integer.")
        if value < 0:
            raise ValueError("Team size cannot be negative.")
        self._team_size = value

    def work(self):
        return f"{self.role} {self.name} is managing a team of {self.team_size} people."


class LeadDeveloper(Developer, Manager):
    def __init__(self, name, role, programming_languages=None, team_size=0, *args, **kwargs):
        super().__init__(
            name=name,
            role=role,
            programming_languages=programming_languages,
            team_size=team_size,
            *args, **kwargs
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def work(self):
        languages = ', '.join(self.programming_languages)
        return (
            f"{self.role} {self.name} is programming in {languages} "
            f"and managing a team of {self.team_size} people."
        )


class Task:
    def __init__(self, title, description, employee=None):
        self.title = title
        self.description = description
        self.employee = employee
        self.status = "In work"

        if self.employee:
            self.employee.assign_task(self)

    def __str__(self):
        assigned_to = self.employee.name if self.employee else "Not assigned"
        return (
            f"Title: {self.title}. Description: {self.description}. "
            f"Executor: {assigned_to}. Status: {self.status}."
        )


class Project:
    def __init__(self, title):
        self.title = title
        self.tasks = []
        self.employees = []

    def add_task(self, task):
        self.tasks.append(task)

    def add_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):
        return self.title

# Создаем сотрудников
developer = Developer(
    name="Tom",
    role="Software Engineer",
    programming_languages=["Python", "JavaScript"]
)

tester = Tester(
    name="Jerry",
    role="QA Engineer",
    programming_languages=["Python", "C++"]
)

manager = Manager(
    name="Kate",
    role="Project Manager",
    team_size=5
)

lead_developer = LeadDeveloper(
    name="Jack",
    role="Team Lead",
    programming_languages=["Python", "C++", "Java"],
    team_size=4
)

# Создаем задачи
# LeadDeveloper
task1_lead_developer = Task(
    title="Общение с заинтересованными сторонами",
    description="Провести встречи с ключевыми заинтересованными сторонами для сбора требований",
    employee=lead_developer
)
task2_lead_developer = Task(
    title="Стратегическое планирование проекта",
    description="Разработать план проекта и определить основные этапы",
    employee=lead_developer
)
task3_lead_developer = Task(
    title="Проектирование баз данных", 
    description="Определить структуру базы данных для хранения информации",
    employee=lead_developer
)

# Developer
task1_developer = Task(
    title="Разработка модуля отслеживания прогресса", 
    description="Создать инструмент для отслеживания задач",
    employee=developer
)
task2_developer = Task(
    title="Интеграция API календаря",
    description="Разработать функцию импорта и экспорта событий календаря",
    employee=developer
)
task3_developer = Task(
    title="Оптимизация кода",
    description="Улучшить производительность путём оптимизации существующего кода",
    employee=developer
)

# Tester
task1_tester = Task(
    title="Тестирование модуля отслеживания прогресса",
    description="Построить сценарии тестирования и провести функциональные тесты",
    employee=tester
)
task2_tester = Task(
    title="Проверка безопасности системы",
    description="Провести тестирование безопасности для выявления уязвимостей",
    employee=tester
)
task3_tester = Task(
    title="Регрессионное тестирование",
    description="Убедиться, что новые изменения не нарушают существующую функциональность",
    employee=tester
)

# Manager
task1_manager = Task(
    title="Управление планом проекта",
    description="Контроль выполнения плана и соблюдения сроков",
    employee=manager
)
task2_manager = Task(
    title="Мониторинг ресурсов",
    description="Координировать распределение ресурсов среди команды",
    employee=manager
)
task3_manager = Task(
    title="Финансовое управление",
    description="Составление бюджета проекта и отслеживание затрат",
    employee=manager
)

project_management_system = Project("Система управления проектами")

# Добавляем сотрудников в проект
project_management_system.add_employee(lead_developer)
project_management_system.add_employee(developer)
project_management_system.add_employee(tester)
project_management_system.add_employee(manager)

# Добавляем задачи в проект
project_management_system.add_task(task1_lead_developer)
project_management_system.add_task(task2_lead_developer)
project_management_system.add_task(task3_lead_developer)

project_management_system.add_task(task1_developer)
project_management_system.add_task(task2_developer)
project_management_system.add_task(task3_developer)

project_management_system.add_task(task1_tester)
project_management_system.add_task(task2_tester)
project_management_system.add_task(task3_tester)

project_management_system.add_task(task1_manager)
project_management_system.add_task(task2_manager)
project_management_system.add_task(task3_manager)

# Сотрудники выполнили задачи
lead_developer.complete_task(task1_lead_developer)
lead_developer.complete_task(task2_lead_developer)

developer.complete_task(task1_developer)
developer.complete_task(task2_developer)

tester.complete_task(task1_tester)

manager.complete_task(task3_manager)


# Сравниваем сотрудников по количеству выполненных задач
print(
    f"Has {developer.name} completed more tasks than {tester.name}? "
    f"{'Yes' if developer > tester else 'No'}"
)
print(
    f"Have {developer.name} and {tester.name} completed the same number of tasks? "
    f"{'Yes' if developer == tester else 'No'}"
)

# Выводим количество выполненных задач каждым сотрудником
for employee in project_management_system.employees:
    print(f"{employee.name} has completed {employee.get_completed_tasks_count()} task(s).")


# # Название проекта
# print(project_management_system)

# # Сотрудники выполняющие проект
# for employee in project_management_system.employees:
#     print(employee)

# # Информация по задачам
# for task in project_management_system.tasks:
#     print(task)


# # Добавление у удаление языков программирования
# print(lead_developer.work())
# lead_developer.add_language("C#")
# lead_developer.remove_language("Java")
# print(lead_developer.work())