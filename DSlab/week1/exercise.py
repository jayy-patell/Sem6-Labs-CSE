#1
# h = int(input("Enter height: "))
# b = int(input("Enter base: "))
# print("Area: ", (h*b))


#2
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# temp = num1
# num1 = num2
# num2 = temp
# print("First number: ", num1)
# print("Second number: ", num2)


#3
# num = int(input("Enter number: "))
# if(num%2==0):
#     print("Even")
# else:
#     print("Odd")


#4
# a= int(input('Enter number:'))
# b= int(input('Enter number:'))
# c= int(input('Enter number:'))
# largest=0
# if a>b and a>c:
# 	largest=a
# elif b>a and b>c:
# 	largest=b
# else:
# 	largest=c
# print(largest)


#5
# tup = (1,3,5,7,9,2,4,6,8,10)
# print(tup[:len(tup)//2])
# print(tup[len(tup)//2:])


#6
# tup = (12, 7, 38, 56, 78 )
# eve=[]

# for i in tup:
#     if(i%2==0):
#         eve.append(i)
# eve = tuple(eve)
# print(eve)


#7
# arr = [1,2,3,0,-1,-2,-2]
# pos=0
# neg=0
# for i in arr:
# 	if i>0:
# 		pos+=1
# 	elif i<0:
# 		neg+=1
#		print(i)
# print(pos)
# print(neg)


#8
arr = [1,2,3,0,-1,-2,-2]

for i in arr:
    if(i%2==0):
        arr.remove(i)
print(arr)

