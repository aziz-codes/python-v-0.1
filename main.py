class Animal:
    def drink(self):
        print("animal is drinking")

class Person(Animal):
    def read(self):
        print("person is reading")

p = Person()


p.drink()