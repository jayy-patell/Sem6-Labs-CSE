arr = [int(x) for x in input("Enter array: ").split(' ')]
# arr = list(map(int, input("Enter array: ").split(' ')))
arr.sort()
n = int(input("Search "))

start, mid, end = 0, 0, len(arr) - 1
mid = (start + end) // 2
while (start <= end):
    if (arr[mid] > n):
        end = mid - 1
    elif (arr[mid] < n):
        start = mid + 1
    else:
        print("Element found")
        break
    mid = (start + end) // 2
else:
    print("Element not found")