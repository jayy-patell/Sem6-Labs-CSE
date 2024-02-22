# l = [(12,22,32),(141,5,6),(97,80,99)]
# palin=[]

# def isPalin(num):
#     temp=num
#     rev=0
#     while(num>0):
#         d=num%10
#         rev=rev*10+d
#         num=num//10
#     if(temp==rev):
#         return True
#     else:
#         return False
    

# for i in l:
#     for j in i:
#         if(isPalin(j)):
#             palin.append(j)
# print(palin)


# print prime numbers from one number to another
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
pno=0

for num in range(num1,num2+1):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        pno+=1
        print(num,end=" ")
        