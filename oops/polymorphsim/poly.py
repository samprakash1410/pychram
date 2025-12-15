class Bird:
  def sound(self):
    return "Chrip"

class Dog:
  def sound(self):
    return "Bark"

def make_sound(animal):
  print(animal.sound())

# Create objects
bird = Bird()
dog = Dog()

# Same function call, different behaviors
make_sound(bird)  
make_sound(dog)   
