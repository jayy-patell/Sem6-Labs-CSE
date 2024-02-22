#number
num = 100000000
print(num)

#string
name = "Sid"
lname = "Srivastava"
print(name + " " + lname)
print(name, lname)
print(name * 3)
print( "My name is %s and weight is %d kg!" % ('Abay', 55))
print("My name is {} and weight is {} kg!".format('Abay', 55))
print("My name is {1} and weight is {0} kg!".format(55, 'Abay'))
print("My name is {name} and weight is {weight} kg!".format(name='Abay', weight=55))
print(f"My name is {name} and weight is {num} kg!")

#built-in functions
str = "this is string example wow!!!"
print(str.capitalize())
str.count('s')
str.find('example')
print(str.lower())
print (str.replace("is", "was"))
print (str.swapcase())
print (str.title())

#list
l = [1,2,3,4,5]
print(l)  # [1, 2, 3, 4, 5]
print(l[0])  # 1
print(l[1:3])  # [2, 3] last but one
print(l[2:])  # [3, 4, 5]
print(l[:3])  # [1, 2, 3]
print(l[-1])  # 5
print(l[-2:])  # [4, 5]
print(l[:-2])  # [1, 2, 3]
print(l[::2])  # [1, 3, 5]
print(l[::-1])  # [5, 4, 3, 2, 1]
l.append(6)
print(l)  # [1, 2, 3, 4, 5, 6]
l.insert(2, 7)
print(l)  # [1, 2, 7, 3, 4, 5, 6]
l.pop()
print(l)  # [1, 2, 7, 3, 4, 5]
l.pop(2)
print(l)  # [1, 2, 3, 4, 5]
l.remove(2)
print(l)  # [1, 3, 4, 5]
l.reverse()
print(l)  # [5, 4, 3, 1]
l.sort()
print(l)  # [1, 3, 4, 5]
l.clear()
print(l)  # []

#tuple
t = (1,2,3,4,5)
print(t)  # (1, 2, 3, 4, 5)

#dictionary
d = {"name": "Sid", "age": 20}
print(d)  # {'name': 'Sid', 'age': 20}
print(d["name"])  # Sid
print(d["age"])  # 20
d["name"] = "Siddharth"
print(d)  # {'name': 'Siddharth', 'age': 20}
d["city"] = "Delhi"
print(d)  # {'name': 'Siddharth', 'age': 20, 'city': 'Delhi'}
d.pop("city")
print(d)  # {'name': 'Siddharth', 'age': 20}
d.clear()
print(d)  # {}

#set
s = {1,2,3,4,5}
print(s)  # {1, 2, 3, 4, 5}

#queue
