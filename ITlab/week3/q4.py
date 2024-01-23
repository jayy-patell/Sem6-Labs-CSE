arr = list(input("Enter string ").split(' '))
for i in range(len(arr) - 1):
    for j in range(len(arr) - 1- i):
        if (arr[j] > arr[j + 1]):
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
new_str=' '.join(arr)
print("sorted: "+new_str)

