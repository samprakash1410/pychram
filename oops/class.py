class Dog:
    """A simple class to represent a dog."""
    
    species = "Canis familiaris"

    def __init__(self, name, age):
        """Initializes the dog's name and age (instance attributes)."""
        self.name = name  
        self.age = age   

    def bark(self):
        """A method that makes the dog bark."""
        return f"{self.name} says woof!"


dog1 = Dog("Dexter", 9)
dog2 = Dog("Panipuri", 5)


print(f"{dog1.name} is {dog1.age} years old.")
print(dog2.bark())
