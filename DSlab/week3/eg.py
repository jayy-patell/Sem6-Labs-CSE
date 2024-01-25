import numpy as numpy

1. Array Creation
A = np.array([1,2,3])
A.dtype

A = np.array([(3,4,5),(1,2,3)])
B = np.zeros((2,4))
C = np.ones((2,3))

S = np.arange(10,35,5)
S = np.arange( 0, 2, 0.3 )

S1=np.linspace(0,2,9)

#usage of Random Number functions
import random
random.choice([1,2,3,4,5]), #this will pick one number from the list randomly
random.choice(‘python’), #will pick one character from the string randomly
random.randrange(25,50), #will pick one integer between 25 to 50
random.randrange(25,50,2), #will pick one integer between 25 to 50 with step size of 2
random.random(), #will pick a random number between 0 to 1
random.uniform(5,10), #will pick a floating point number between 5 to 10
random.shuffle([1,2,3,4,5]), #will shuffle the list elements
random.seed(10), #to get same random value during every execution

For 2-D array:
a = np.arange(15).reshape(3, 5)
a.shape
a.size
a.T # transposed to 5x3 matrix

For 3-D array:
c = np.arange(24).reshape(2,3,4) # 1st value indicates (no of planes) (3,4) is the dimension

Array operations:
C=A-B, B**2, 10*np.sin(A), A<35

Matrix operations:
A*B # elementwise product
A.dot(B) # matrix product
np.dot(A, B) # another matrix product

Axis operations:
b = np.arange(12).reshape(3,4)
b
array([[ 0, 1, 2, 3],
	[ 4, 5, 6, 7],
	[ 8, 9, 10, 11]])
b.sum(axis=0) #array([12, 15, 18, 21]) # sum of each column
b.sum(axis=1) #array([6, 22, 38]) # sum of each row

Indexing, Slicing, Iterating array:
a = np.arange(10)**3
a # array([ 0, 1, 8, 27, 64, 125, 216, 343, 512, 729])
a[2:5] # array([ 8, 27, 64])
a[0:6:2] # array([0,8,64,216])

b = np.array([[ 0, 1, 2, 3],
	[10, 11, 12, 13],
	[20, 21, 22, 23],
	[30, 31, 32, 33],
	[40, 41, 42, 43]])
b[2,3] #will fetch 23
b[0:5,1] or b[:5,1] or b[:,1] #will fetch [1,11,21,31,41]
b[−1,:] # will fetch last row
b[:,−1] # will fetch last col

for row in b:
	print (row) # will print every row

for element in b.flat:
print (element) # will show all elements of b in 1−D array

Changing the shape of matrix:
b.ravel()
B = b.reshape(4,5)

Stacking together arrays:
D1=np.vstack((A1,A2))
D2=np.hstack((A1,A2))

np.column_stack((a,b))
np.hstack((a[:,newaxis],b[:,newaxis]))

Indexing with array of indices:
a = np.arange(12)**2
i = np.array( [ 1,1,3,8,5 ] ) # an array of indices
a[i] #array([ 1, 1, 9, 64, 25]) # the elements of a at the positions i

j = np.array( [ [ 3, 4], [ 9, 7 ] ] ) # a bidimensional array of indices
a[j] # the same shape as j
array([[ 9, 16],
	[81, 49]])

Calculate sum of all elements in 2D matrix:
using for-loop(Mapping by value); 
a=np.array([(3,2,9),(1,6,7)])
s1=0
for row in a:
	for col in row:
		s1+=col
print(s1)

using for-loop(Mapping by index);
a=np.array([(3,2,9),(1,6,7)])
s=0
for i in range(a.shape[0]):
	for j in range(a.shape[1]):
		s+=a[i,j]
print(s)