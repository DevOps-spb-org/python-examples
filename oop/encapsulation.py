class Person:
    def __init__(self, name):
        self.__name = name  # устанавливаем имя
        self.__age = 1  # устанавливаем возраст

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


tom = Person("Tom")

tom.display_info()  # Имя: Tom  Возраст: 1
tom.age = -3486  # Недопустимый возраст
print(tom.age)  # 1
tom.age = 36
tom.display_info()  # Имя: Tom  Возраст: 36
