class InfoMeta(type):
    def __new__(cls, name, bases, dct):

        def info(self):
            class_name = self.__class__.__name__
            attrs = self.__dict__

            info_str = f"Class name: {class_name}\nAttributes:\n"
            for attr_name, value in attrs.items():
                info_str += f"  {attr_name}: {value}\n"
            
            return info_str
        
        dct['info'] = info

        return super().__new__(cls, name, bases, dct)
    
    def __init__(self, name, bases, dct):
        super().__init__(name, bases, dct)
    

class MyClass(metaclass=InfoMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class YourClass(metaclass=InfoMeta):
    def __init__(self, country, city):
        self.country = country
        self.city = city


class OurClass(metaclass=InfoMeta):
    def __init__(self, our_names, our_countries):
        self.our_names = our_names
        self.our_countries = our_countries


my_class = MyClass('Anton', 34)
your_class = YourClass('Russia', 'Novosibirsk')
our_class = OurClass('All elements', 'On the earth')

print(my_class.info())
print(your_class.info())
print(our_class.info())