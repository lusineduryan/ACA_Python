class Animal:
    def __init__(self,name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

rex = Dog("Rex", "black")
print(rex.color)
rex.bark()


class Wolf(Dog):
    def bark(self):
        print("Auuu")
        super().bark()

husky = Wolf("Max", "grey")
husky.bark()
