class Strings:
    def get_String(self):
        self.string = input("Enter the string")
    def print_String(self):
        for i in self.string:
            if (ord(i)>=97):
                print(chr(ord(i)-32),end="")
            else:
                print(i,end="")
        print()
    pass
if __name__=='__main__':
    string = Strings()
    string.get_String()
    string.print_String()
