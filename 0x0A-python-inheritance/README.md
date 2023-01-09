# Python - Inheritance
Inheritance is the mechanism that allows to create a hierachy of classes that share a set of properties, methods by deriving a class from another class.



It is the ability of one class to derive properties from another class

Certainly! Inheritance is a way to create a new class that is a modified version of an existing class. The new class is called the derived class, and the existing class is the base class. The derived class inherits (i.e., takes over) the attributes and behaviors of the base class, and can also have additional attributes and behaviors of its own.

Syntax:

```
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Some generic animal sound")

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")  # Call superclass's __init__ method
        self.breed = breed
        self.toy = toy
        
    def play(self):
        print(f"{self.name} plays with {self.toy}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")  # Call superclass's __init__ method
        self.breed = breed
        
    def make_sound(self):
        print("Woof!")
```
