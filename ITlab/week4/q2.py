class Question:
    array = []
    target = 0
    def __init__(self,array,target):
        self.array = array
        self.target = target

    def find(self):
        tar = self.target
        for i in range (len(self.array)-1):
            j=i+1
            while j<len(self.array):
                if(self.array[i]+self.array[j] == tar):
                    return i,j
                j = j+1
        return 'No solution'

size = int(input("Enter no. of elements: "))
array = [int(x) for x in input("Enter elements: ").split(' ')]
target = int(input("target: "))
solver = Question(array,target)
print(solver.find())