class Calculator:

    def __init__(self,a,b):
        self.a= a
        self.b = b
        self.ans = None

    def add(self):
        self.ans = self.a + self.b
        return self.ans

    def mul(self):
        self.ans = self.a*self.b
        return self.ans

    def div(self):
        self.ans = round(self.a/self.b,2)
        return self.ans

    def sub(self):
        self.ans = self.a-self.b
        return self.ans


if __name__ == '__main__':

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    obj = Calculator(a,b)
    choice =1

    while choice!=0:

        print("Please select operation -\n" \
                "0. Exit\n" \
                "1. Add\n" \
                "2. Subtract\n" \
                "3. Multiply\n" \
                "4. Divide\n")

        choice=int(input("Enter choice: "))
        if choice==1:
            print("Result: ",obj.add())
        elif choice==2:
            print("Result: ",obj.sub())
        elif choice==3:
            print("Result: ",obj.mul())
        elif choice==4:
            print("Result: ",obj.div())
        elif choice==0:
            print("Exiting!")
        else:
            print("Invalid choice!!")
