list1=[("b12d","8f8f"),("g1p5"),("f5p8")]
al=[]
num=[]

for tup in list1:
	for key in tup:
		for letter in key:
			if(letter>='0' and letter<='9'):
				num.append(letter)
			else:
				al.append(letter)

print(num)
print(al)