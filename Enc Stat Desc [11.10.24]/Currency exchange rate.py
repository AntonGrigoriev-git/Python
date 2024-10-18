class CurrencyCodeDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Currency code must be a string")
        if not value.isupper() or len(value) != 3:
            raise ValueError("Currency code must be 3 uppercase letters")
        instance.__dict__[self.name] = value


class Currency:
    code = CurrencyCodeDescriptor('code')

    def __init__(self, code='USD'):
        self.code = code
        self.__rate = {'USD': 1}

    def __str__(self):
        rates = ', '.join(f"{code}: {rate}" for code, rate in self.__rate.items() if code != 'USD')
        return f"The exchange rate relative to the US dollar: {rates}"

    def get_rate(self, code):
        return self.__rate.get(code)

    def set_rate(self, code, rate):
        self.code = code

        if code in self.__rate:
            raise ValueError(f"Currency code '{code}' already exists.")

        if Currency.is_valid_rate(rate):
            self.__rate[code] = rate
        else:
            raise ValueError("Enter a valid currency code and a positive rate!")

    def get_all_currencies(self):
        return list(self.__rate.keys())

    @staticmethod
    def is_valid_rate(rate):
        return isinstance(rate, (int, float)) and rate > 0


class CurrencyConverter:
    def __init__(self, currency):
        self.currency = currency
        self.currencies_mapping = {}

    def menu(self):
        available_currencies = self.currency.get_all_currencies()
        # Присваиваем номер опции на код валюты
        self.currencies_mapping = {i + 1: code for i, code in enumerate(available_currencies)}

        for num, code in self.currencies_mapping.items():
            print(f"{num}. {code}")

        what = int(input("Select the currency to convert from: "))
        from_currency = self.currencies_mapping.get(what)
        where = int(input("Choose which currency to convert to: "))
        to_currency = self.currencies_mapping.get(where)
        amount = float(input(f"How much {from_currency} do you want to convert to {to_currency}: "))

        return what, where, amount

    def convert(self, what, where, amount):
        from_currency = self.currencies_mapping[what]
        to_currency = self.currencies_mapping[where]

        from_rate = self.currency.get_rate(from_currency)
        to_rate = self.currency.get_rate(to_currency)
            
        amount_in_usd = amount / from_rate
        converted_amount = amount_in_usd * to_rate

        return converted_amount


currency = Currency()
currency.set_rate('EUR', 0.91786)
currency.set_rate('RUB', 97.01)
currency.set_rate('CNY', 7.11)
print(currency)

converter = CurrencyConverter(currency)
try:
    what, where, amount = converter.menu()
    converted_amount = converter.convert(what, where, amount)
    print(f"Converted amount: {round(converted_amount, 2)} {converter.currencies_mapping[where]}")
except KeyError as e:
    print(f"Key '{e}' is missing from the dictionary")
except ValueError as e:
    print(f"Error: {e}")