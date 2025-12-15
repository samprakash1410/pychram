from abc import ABC, abstractmethod

class Greeting():
    @abstractmethod
    def say_holla(self):
        pass  

class Speaking(Greeting):
    def say_holla(self):
        return "Holla!"

g = Speaking()
print(g.say_holla())
