import numpy as np
import matplotlib.pyplot as plt

'''
here we will be learning some advanced concepts in
numpy
'''
#lets get the pi value using pi 
pieValue = np.pi
print('pie value:',pieValue)

#round function will round the value to given value, in our case its 2
print('rounded value:',np.round(pieValue,2))

'''
getting the trignometric values using numpy
'''
#get the sin 90 deg
print('sin 90 deg:',np.sin(pieValue/2))

#get the sin 30 deg
print('sin 30 deg:',np.sin(pieValue/6))

#get the cos 90 deg
print('cos 90:',np.cos(pieValue/2))

#get the cos 30 deg
print('cos 30:',np.cos(pieValue/6))

#get the tan 90 deg
print('tan of 90:',np.tan(pieValue/2))

# tan 0
print('tan 0:',np.tan(0))


'''
now lets consider random 
function
'''
#random numbers in range of 1 - 10
someRandomNumbers = np.random.random((2,2))
print('random numbers in range of 1 - 10:\n',someRandomNumbers)

#random int numbers in range of 1 - 10
someRandomIntNumbers = np.random.randint(1,10)
print('random int numbers in range of 1 - 10:',someRandomIntNumbers)

#random array from 1 - 10 in 2-D array
randomArray = np.random.randint(1,10,(2,2))
print('random 2-D array:\n',randomArray)

#random array from 1 - 10 in 3-D array
randomThreeDArray = np.random.randint(1,10,(3,4,5))
print('random 3-D array:\n',randomThreeDArray)

#rand function
#this will generate the random float values
floatArray= np.random.rand(2,3)
print('random float array:\n',floatArray)

#randn
#this will generate the random numbers including - ve
negetiveArray = np.random.randn(2,4)
print('random negetive array:\n', negetiveArray)


'''
now lets play with some strings using np.char
'''
s1= 'hello my name is uday!'
s2= 'im learning numpy..'

#now concat the two string using np.char.add
concatedString = np.char.add(s1,s2)
print('concated string:', concatedString)

#now lets convert s1 to upper case
print('converted upper case:',np.char.upper(s1))

#now lets convert s2 to lower case
print('converted to lower case:',np.char.lower(s1))

#split the string with whitespaces
print('splitted s1:',np.char.split(s1))

#split the lines with newlines
s3 = "hello \n reader have a \n happy reading.."
print("split the new lines:",np.char.splitlines(s3))

#now lets replace some words with other
s4 = 'im doing bad now..'
print('replace bad with good.:',np.char.replace(s4,'bad','good'))

#using center function
print(np.char.center('this is good',100,'*'))



'''
now lets plot these into graph
'''
#sin curve
x_sin = np.arange(0,2*pieValue, 0.1)
y_sin = np.sin(x_sin)
plt.figure(figsize=(8,8))
plt.plot(x_sin,y_sin)
plt.title('sin curve')
plt.show()

#cos curve
x_cos = np.arange(0,2*pieValue, 0.1)
y_cos = np.cos(x_cos)
plt.figure(figsize=(8,8))
plt.plot(x_cos,y_cos)
plt.title('cos curve')
plt.show()

#tan curve
x_tan = np.arange(0,2*pieValue, 0.1)
y_tan = np.tan(x_tan)
plt.figure(figsize=(8,8))
plt.plot(x_tan,y_tan)
plt.title('tan curve')
plt.show()

#cot curve
x_cot = np.arange(0,2*pieValue, 0.1)
y_cot = 1/np.tan(x_cot)
plt.figure(figsize=(8,8))
plt.plot(x_cot,y_cot)
plt.title('cot curve')
plt.show()

'''
now lets put all these into 
a single plot using subplot
'''
plt.figure(figsize=(10,10))
plt.title('all plots')
plt.subplot(2,2,1,)
plt.plot(x_sin,y_sin,'b--')
plt.xlabel('x_sin')
plt.ylabel('y_sin')
plt.title('sin curve')

plt.subplot(2,2,2)
plt.plot(x_cos,y_cos,'r-')
plt.xlabel('x_cos')
plt.ylabel('y_cos')
plt.title('cos curve')

plt.subplot(2,2,3)
plt.plot(x_tan,y_tan,'y-')
plt.xlabel('x_tan')
plt.ylabel('y_tan')
plt.title('tan curve')

plt.subplot(2,2,4)
plt.plot(x_cot,y_cot,'g-')
plt.xlabel('x_cot')
plt.ylabel('y_cot')
plt.title('cot curve')

plt.show()