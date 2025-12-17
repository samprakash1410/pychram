class A:
    def fun1(self):
        print("this is a public method")

    def fun2(self):
        print("this is a private method")

    def help(self):
        self.fun1()
        self.fun2()

obj =A()
obj.help()