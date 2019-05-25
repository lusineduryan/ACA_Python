class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

    legs = 4

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

print(fido.legs)
print(Dog.legs)

