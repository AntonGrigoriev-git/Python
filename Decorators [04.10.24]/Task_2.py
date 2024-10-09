"""A decorator for converting the result."""


def to_string(func):
    def wrapper():
        result = func()
        return str(result) if not isinstance(result, str) else result
    return wrapper


@to_string
def get_number():
    return 42


@to_string
def get_text():
    return "Hello, World!"

print(type(get_number()))
print(type(get_text()))