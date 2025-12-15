class studnet:
    def __init__(self,name="Prakash",marks=80):
        self._name=name
        self._marks=marks

s1 = studnet()
s2 = studnet("Dileep",90)

print ("Name:{} marks:{}".format(s1._name,s2._marks))
print ("Name:{} marks:{}".format(s2._name,s2._marks))
s1._name="Prakash"