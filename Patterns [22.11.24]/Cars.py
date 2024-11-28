from abc import ABC, abstractmethod

# --- Исключения ---
class AuthenticationError(Exception):
    pass

class PermissionError(Exception):
    pass

# --- Flyweight Pattern ---
class CarModelFlyweight:
    """
    Flyweight для модели автомобиля.
    Содержит общие данные для моделей с одинаковыми make, model и vehicle_type.
    """
    def __init__(self, make, model, vehicle_type='Sedan'):
        self.make = make
        self.model = model
        self.vehicle_type = vehicle_type

class CarModelFlyweightFactory:
    """
    Фабрика Flyweight, которая управляет созданием и предоставлением Flyweight объектов.
    """
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, make, model, vehicle_type='Sedan'):
        key = (make, model, vehicle_type)
        if key not in cls._flyweights:
            cls._flyweights[key] = CarModelFlyweight(make, model, vehicle_type)
            print(f"Создан новый Flyweight для модели: {make} {model} ({vehicle_type})")
        else:
            print(f"Используется существующий Flyweight для модели: {make} {model} ({vehicle_type})")
        return cls._flyweights[key]

# --- Adapter Pattern ---
# Target Interface
class ExternalService(ABC):
    @abstractmethod
    def get_location(self):
        pass

# Adaptee
class CarGPS:
    """
    Система GPS автомобиля с несовместимым интерфейсом.
    """
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_coordinates(self):
        return self.latitude, self.longitude

# Adapter
class GPSAdapter(ExternalService):
    """
    Адаптер, который адаптирует CarGPS к интерфейсу ExternalService.
    """
    def __init__(self, car_gps: CarGPS):
        self.car_gps = car_gps

    def get_location(self):
        latitude, longitude = self.car_gps.get_coordinates()
        return {
            'latitude': latitude,
            'longitude': longitude
        }

# --- Компоненты Транспорта ---
class TransportComponent(ABC):
    @abstractmethod
    def get_info(self, user):
        pass

class TransportLeaf(TransportComponent):
    def __init__(self, car):
        self.car = car

    def get_info(self, user):
        return self.car.get_info(user)

class TransportGroup(TransportComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, transport):
        self.children.append(transport)

    def remove(self, transport):
        self.children.remove(transport)

    def get_info(self, user):
        info = {'Group': self.name, 'Vehicles': []}
        for child in self.children:
            info['Vehicles'].append(child.get_info(user))
        return info

# --- Паттерн Декоратор ---
class PremiumCarDecorator(TransportComponent):
    def __init__(self, car, premium_features):
        self.car = car
        self.premium_features = premium_features

    def get_info(self, user):
        info = self.car.get_info(user)
        info['Premium Features'] = self.premium_features
        return info

    def __getattr__(self, name):
        """
        Делегирует доступ к атрибутам обёрнутого объекта `car`.
        """
        return getattr(self.car, name)

# --- Паттерн Proxy ---
class DriverComponent(ABC):
    @abstractmethod
    def get_details(self, user):
        pass

class Driver(DriverComponent):
    def __init__(self, name, rating, trips, license_number):
        self.name = name
        self.rating = rating
        self.trips = trips
        self.license_number = license_number

    def get_details(self, user):
        return {
            'Name': self.name,
            'Rating': self.rating,
            'Trips': self.trips,
            'License Number': self.license_number
        }

class DriverProxy(DriverComponent):
    def __init__(self, driver):
        self.driver = driver

    def get_details(self, user):
        if user is None:
            raise AuthenticationError("Пользователь не аутентифицирован.")
        if user.role != 'admin':
            raise PermissionError("Доступ запрещен. Необходима роль admin.")
        return self.driver.get_details(user)

# --- Класс Пользователя ---
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

# --- Класс автомобиля ---
class Car(TransportComponent):
    def __init__(self, license_plate, model, driver, gps_adapter):
        self.license_plate = license_plate
        self.model = model  # Flyweight объект
        self.driver = driver
        self.gps_adapter = gps_adapter

    def get_info(self, user):
        info = {
            'License Plate': self.license_plate,
            'Model': f"{self.model.make} {self.model.model} ({self.model.vehicle_type})",
            'Location': self.gps_adapter.get_location()
        }
        try:
            driver_details = self.driver.get_details(user)
            info['Driver'] = driver_details
        except (AuthenticationError, PermissionError) as e:
            info['Driver'] = str(e)
        return info

# --- Фасад для логистических операций ---
class LogisticsFacade:
    def __init__(self):
        self.trips = []

    def book_trip(self, start, end, car):
        trip = {
            'Start': start,
            'End': end,
            'Car': car.license_plate
        }
        self.trips.append(trip)
        print(f"Поездка забронирована: {trip}")

    def track_vehicle(self, car):
        location = car.gps_adapter.get_location()
        print(f"Отслеживание транспортного средства {car.license_plate} в локации {location}")

    def show_all_trips(self):
        print("Все поездки:")
        for trip in self.trips:
            print(trip)

# --- Основная функция ---
def main():
    # --- Flyweight Pattern ---
    # Создание Flyweight моделей для легковых автомобилей
    model_toyota = CarModelFlyweightFactory.get_flyweight('Toyota', 'Camry', 'Sedan')
    model_honda = CarModelFlyweightFactory.get_flyweight('Honda', 'Accord', 'Sedan')
    # Создание Flyweight моделей для минивэнов
    model_toyota_sienna = CarModelFlyweightFactory.get_flyweight('Toyota', 'Sienna', 'Minivan')
    model_honda_odyssey = CarModelFlyweightFactory.get_flyweight('Honda', 'Odyssey', 'Minivan')
    # Попытка создать ещё один объект той же модели, чтобы проверить Flyweight
    model_toyota_duplicate = CarModelFlyweightFactory.get_flyweight('Toyota', 'Camry', 'Sedan')

    print()  # Разделитель для читаемости вывода

    # --- Создание пользователей ---
    admin_user = User(username='Alice', role='admin')
    manager_user = User(username='Bob', role='manager')
    regular_user = User(username='Charlie', role='user')

    # --- Создание водителей ---
    driver1 = Driver('Alice', 4.8, 500, 'D1234567')
    driver_proxy1 = DriverProxy(driver1)

    driver2 = Driver('Bob', 4.5, 300, 'D7654321')
    driver_proxy2 = DriverProxy(driver2)

    # --- Функции для попытки получить детали водителя через прокси ---
    def attempt_get_details(driver_proxy, user):
        try:
            details = driver_proxy.get_details(user)
            print(f'Детали водителя для пользователя "{user.username}": {details}')
        except AuthenticationError as ae:
            print(f'AuthenticationError для пользователя "{user.username}": {ae}')
        except PermissionError as pe:
            print(f'PermissionError для пользователя "{user.username}": {pe}')

    def attempt_get_details_no_user(driver_proxy):
        try:
            details = driver_proxy.get_details(None)
            print(f'Детали водителя без аутентификации: {details}')
        except AuthenticationError as ae:
            print(f'AuthenticationError для неаутентифицированного пользователя: {ae}')
        except PermissionError as pe:
            print(f'PermissionError для неаутентифицированного пользователя: {pe}')

    # --- Попытки доступа к деталям водителей с разными пользователями ---
    print("---- Доступ к driver1 ----")
    attempt_get_details(driver_proxy1, admin_user)      # Должен получить детали
    attempt_get_details(driver_proxy1, manager_user)    # Должен получить PermissionError
    attempt_get_details(driver_proxy1, regular_user)    # Должен получить PermissionError
    attempt_get_details_no_user(driver_proxy1)          # Должен получить AuthenticationError

    print("\n---- Доступ к driver2 ----")
    attempt_get_details(driver_proxy2, admin_user)      # Должен получить детали
    attempt_get_details(driver_proxy2, manager_user)    # Должен получить PermissionError
    attempt_get_details(driver_proxy2, regular_user)    # Должен получить PermissionError
    attempt_get_details_no_user(driver_proxy2)          # Должен получить AuthenticationError
    
    print() # Разделитель для читаемости вывода

    # --- Создание GPS систем и адаптеров ---
    car_gps1 = CarGPS(55.01, 82.55)
    adapter_gps1 = GPSAdapter(car_gps1)

    car_gps2 = CarGPS(55.02, 82.56)
    adapter_gps2 = GPSAdapter(car_gps2)

    car_gps3 = CarGPS(55.03, 82.57)
    adapter_gps3 = GPSAdapter(car_gps3)

    car_gps4 = CarGPS(55.04, 82.58)
    adapter_gps4 = GPSAdapter(car_gps4)

    # --- Создание автомобилей ---
    # Легковые автомобили
    car1 = Car('ABC-123', model_toyota, driver_proxy1, adapter_gps1)
    car2 = Car('XYZ-789', model_honda, driver_proxy2, adapter_gps2)
    # Минивэны
    van1 = Car('MIN-001', model_toyota_sienna, driver_proxy1, adapter_gps3)
    van2 = Car('MIN-002', model_honda_odyssey, driver_proxy2, adapter_gps4)

    # --- Декорирование автомобиля премиум-функциями ---
    premium_car1 = PremiumCarDecorator(car1, ['Wi-Fi', 'Sunroof'])
    premium_van1 = PremiumCarDecorator(van1, ['Extra Seating', 'Entertainment System'])

    # --- Создание Composite групп ---
    all_cars = TransportGroup('All Cars')
    all_cars.add(TransportLeaf(car1))
    all_cars.add(TransportLeaf(car2))
    all_cars.add(TransportLeaf(van1))
    all_cars.add(TransportLeaf(van2))
    all_cars.add(TransportLeaf(premium_car1))  # + декорированный седан
    all_cars.add(TransportLeaf(premium_van1))  # + декорированный минивэн

    # --- Использование фасада ---
    facade = LogisticsFacade()
    facade.book_trip('Point A', 'Point B', car1)
    facade.book_trip('Point C', 'Point D', premium_car1)
    facade.book_trip('Point E', 'Point F', van1)
    facade.book_trip('Point G', 'Point H', premium_van1)
    facade.track_vehicle(car1)
    facade.track_vehicle(premium_car1)
    facade.track_vehicle(van1)
    facade.track_vehicle(premium_van1)
    facade.show_all_trips()

    # --- Информация о группах ---
    print('\nTransport Groups Info:')
    def print_info(info, indent=0):
        for key, value in info.items():
            print('  ' * indent + str(key))
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        print_info(item, indent + 1)
                    else:
                        print('  ' * (indent + 1) + str(item))
            elif isinstance(value, dict):
                print_info(value, indent + 1)
            else:
                print('  ' * (indent + 1) + str(value))

    info = all_cars.get_info(admin_user)
    print_info(info)

main()