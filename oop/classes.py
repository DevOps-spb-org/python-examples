class Person:

    # конструктор
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self.name, "deleted from memory")

    def display_info(self):
        print("Hi, my name is", self.name)


class Auto:

    # конструктор
    def __init__(self, name):
        self.name = name

    def move(self, speed):
        print(self.name, "едет со скоростью", speed, "км/ч")
