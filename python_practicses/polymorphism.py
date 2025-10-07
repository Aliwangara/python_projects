
# Create three classes:

# Animal (base class with a method sound())

# Dog (child class — overrides sound() → “Bark”)

# Cat (child class — overrides sound() → “Meow”)

class Animal:
    def sound(self):
        print("Animals have different sounds")

class Dog(Animal):
    def sound(self):
        print("A dog Barks")
class Cat(Animal):
    def sound(self):
        print("A cat meows")

animal_sounds = [Animal(),Dog(), Cat()]

for c in animal_sounds:
    c.sound()


