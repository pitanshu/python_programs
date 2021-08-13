class numbers():
    num1=0
    num2=0

    def setvalue(self,no1,no2):
        self.num1=no1
        self.num2=no2

    def getvalue(self):
        print("Value of number 1 :{}  Value of number 2 : {}".format(self.num1,self.num2))

    def swap(self):
        self.num1=self.num1+self.num2
        self.num2=self.num1-self.num2
        self.num1=self.num1-self.num2

def line():
        print("--------------------------------------------------")


line()
obj=numbers()
no1=int(input("Enter the first integer number : "))
no2=int(input("Enter the second integer number : "))

line()
print("Setting the value to the class object")
obj.setvalue(no1,no2)
obj.getvalue()

line()
print("Swapping the values of the class objects ")
obj.swap()
print("values after swap")
obj.getvalue()
line()
