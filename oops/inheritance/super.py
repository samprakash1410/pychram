class emp:
    def __init__(self,id,name):
        self.id = id
        self.name=name 

class fun(emp):
    def __init__(self,name,id,email):
        super().__init__(id,name)
        self.email=email  

obj = fun(101,"Nikhila","nikky20@gmail.com")
print(obj.id,obj.name,obj.email)