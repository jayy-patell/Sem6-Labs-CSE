class Maths:
    def __init__(self,x,n):
        self.x=x
        self.n=n
    def pow(self):
        if n==1:
            return x
        self.n = n-1
        return x*pow(self)

if __name__ == '__main__':
    x = int(input("Enter the Base"))
    n = int(input("Enter the power"))
    print("The value is "+str(Maths.pow(x,n)))
