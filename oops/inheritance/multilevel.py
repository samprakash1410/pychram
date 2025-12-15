class grandparent:
    def legacy(self):
        print("this is my grandparent legacy")
class parent(grandparent):
    pass
class child(parent):
    pass
print("grandparent lagacy")