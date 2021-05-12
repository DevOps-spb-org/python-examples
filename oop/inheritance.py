class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


class Employee(Person):
    def details(self, company):
        # print(self.__name, "работает в компании", company) # так нельзя, self.__name - приватный атрибут
        print(self.name, "работает в компании", company)


tom = Employee("Tom", 23)

tom.details("Google")
tom.age = 36
tom.display_info()
