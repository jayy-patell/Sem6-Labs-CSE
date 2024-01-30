class pairtargetsum:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
    def pairFinder(self):
        for i in range(0,len(self.arr)-1):
            if self.arr[i]+self.arr[i+1]==self.target:
                print(str(i+1)+" ,"+str(i+2))
                return
        print("pair not found")

if __name__ == '__main__':
    print("Enter the numbers in the array with space seperation")
    arr = [int(i) for i in input().split()]
    print("Enter the target sum")
    t = int(input())
    pts = pairtargetsum(arr,t)
    pts.pairFinder()
