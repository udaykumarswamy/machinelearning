import numpy as np
'''
In this module we will be learning numpy basic
operations
'''
'''
we can store the multi dim array
'''
#1-dim array
oneDimentionalArray = np.array([1,2,3,4,5])
print('OneDimentionalArray')
print(oneDimentionalArray,'\n')

#2-dim array
twoDimentionalArray = np.array([[1,2,3,4,5],
                               [6,7,8,9,0]])
print('TwoDimentionalArray')
print(twoDimentionalArray,'\n')

#3-dim array
threeDimentianalArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('ThreeDimentionalArray')
print(threeDimentianalArray,'\n')

#to get the type of the data
print('type of the three dim array',type(threeDimentianalArray))

#get the number of elements in array
print('size of the three dim array:',np.size(threeDimentianalArray))

#to get the shape of the data, rows and columns
print('rows:',threeDimentianalArray.shape[0])
print('cols:',threeDimentianalArray.shape[1])

#to get the data type of the data
print('data type:',threeDimentianalArray.dtype)


'''
transpose() will convert the rows to cols 
and cols to rows
'''
print(threeDimentianalArray.transpose())

'''
empty(shape, dtype=float, order='C', *, like=None)
empty((rows,cols),dtype)
shape --> is tuple (rows , cols)
if we want to generate the empty array of random data or data with zero
dataType can be --> int , float , string and boolean
'''
randomEmptyArray = np.empty((3,4),dtype=int)
print('RandomEmptyArray')
print(randomEmptyArray)

'''
ones(shape, dtype=None, order='C', *, like=None) 
ones((rows,cols),dtype)
if we want to genrate the array of 1's
'''
onesArray = np.ones((2,3),dtype=int)
print('OnesArray')
print(onesArray)
#what if i pass only one value --> then it will consider that as column and dtype as float
print(np.ones(5))

'''
zeros(shape, dtype=None, order='C', *, like=None) 
zeros((rows,cols),dtype)
if we want to genrate the array of 0's
'''
zerosArray = np.zeros((2,3),dtype=int)
print('ZerosArray')
print(zerosArray)



'''
np.arange(start,stop,step)
start --> start of the range
stop --> end of range
step --> its not mandytory, default will be 1
will be mostly used in the assigning the axis 
in matplot lib
'''
arangeData = np.arange(0,20,2)
print('ArangeData')
print(arangeData)

'''
np.reshape(a,shape)
a --> array to be transformaed
shape --> (rows, cols)
this function will reshape the given array
'''
reshapedArray = np.reshape(arangeData,(2,5))
print('ReshapedArray')
print(reshapedArray)

'''
array.flatten()
This will flatten the multi dim array into 1-D array
-- copy of the orginal array , if you modify the array the value in orginal will not change
as it occupies memory its slower than ravel() , it is a method of ndarray object
'''
print('Falttened Array')
print(reshapedArray.flatten())

'''
array.ravel()
This will flatten the multi dim array into 1-D array
-- return the refernece of th orginal array , if you modify the array the value in orginal also will change
as it dose not occupies memory its faster than flatten() , it is a libray function
'''
print('Raveled Array')
print(np.ravel(reshapedArray))

'''
array slicing
'''
rdArray= np.arange(1,51,dtype=int)
randomArray = np.reshape(rdArray,(10,5))
print('Generated random array:')
print(randomArray,'\n')

#array[rows,colums] , 
print('1 row:',randomArray[0])
print('1 row 1 col:',randomArray[0,0])
print('2 to 4 the rows:\n',randomArray[2:5])
print('all rows 4 col:',randomArray[:,3])
print('all rows 2 to 4 the col:\n',randomArray[:,2:5])
print('all rows all cols:\n',randomArray[:,:])

'''
mathematical operations
in numpy
'''
a = np.arange(0,20).reshape(4,5)
b = np.arange(20,40).reshape(4,5)
print('array a:')
print(a)

print('array b:')
print(b)

#addition of array
c=a+b
print('added array by + operator')
print(c)

c = np.add(a,b)
print('added array by add() function')
print(c)

#subtraction of array
c = a-b
print('sub array by - operator:')
print(c)

c = np.subtract(a,b)
print('sub by subtract() function:')
print(c)

#multiplication of array
c = a * b
print('multiplication by * operator:')
print(c)

c = np.multiply(a,b)
print('multiplication by multiply() function:')
print(c)

#division of array
c = a/b

print('div of array by / operator:')
print(c)

c = np.divide(a,b)
print('div bu divide() function:')
print(c)

#log of array
c = np.log(a)
print('log of array a:')
print(c)

#dot operation of two array
'''
for this operation we should have the col of first array 
identical to row of second array
assume a(5,4) b should be b(4,5)
the result will be res(5,5)
'''
a  = a.reshape(5,4)
c= a@b
print('dot operation by @ operator')
print(c)
c = np.dot(a,b)
print('dot operation by dot() function:')
print(c)

#to get the min of array
min = a.min()
print('minimum :',min)

#max of the array
max = a.max()
print('maximum :',max)

#to get the index of the min
minPos = a.argmin()
print('max position:',minPos)

#to get the index of the max
maxPos = a.argmax()
print('max position:',maxPos)

#standard diviation of array
std = a.std()
print('standard diviation:',std)

#mean of the array
mean = a.mean()
print('mean of the array:', mean)



