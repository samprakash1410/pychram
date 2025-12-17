class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.2) + 37



human = Celsius()


human.temperature =24


print(human.temperature)


print(human.to_fahrenheit())