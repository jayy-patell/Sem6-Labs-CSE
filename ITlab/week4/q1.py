class powerSetClass:
    '''This class is to find uniwue possible subsets'''
    def __init__(self, arr):
        self.arr = arr
    def powerSetGenerator(self):
        powerSet=[]
        for i in range(2**(len(self.arr))):
            subset = []
            for j in range(len(self.arr)):
                if((i & (1<<j))):
                    subset.append((self.arr[j]))
                if subset not in powerSet:
                    powerSet.append(subset)
        return powerSet

if __name__ == '__main__':
    print("Enter the numbers in the array with space seperation")
    arr = [i for i in input().split()]
    psc = powerSetClass(arr)
    powerSet = psc.powerSetGenerator()
    print(powerSet)
