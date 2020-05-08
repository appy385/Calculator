class Calculator:

    def __init__(self,a,b):
        self.a= a
        self.b = b
        self.ans = None

    def add(self):
        print("Addition of: ",self.a, "and ",self.b)
        self.ans = self.a + self.b
        return self.ans

    def mul(self):
        print("Multiplication of:",self.a, "and ",self.b)

        self.ans = self.a*self.b
        return self.ans

    def div(self):
        print("Division of:" ,self.a ,"and " ,self.b)
        self.ans = round(self.a/self.b,2)
        return self.ans

    def sub(self):
        print("Subtraction of:" ,self.a ,"from " ,self.b)
        self.ans = self.a-self.b
        return self.ans


if __name__ == '__main__':

    obj = Calculator(3,4)
    print(obj.add(),"\n")
    print(obj.sub(),"\n")
    print(obj.mul(),"\n")
    print(obj.div(),"\n")

    
