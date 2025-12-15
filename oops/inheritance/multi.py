class Father:
    def skill1(self):
        print("medical officer")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill1() 
c.skill2() 
