import numpy as np
#numpy is use to create the array and perform the operation on it
arr1 = np.array([1,2,3,4,5])
#this is the 1 dimensional array
print("this is the one dimensional array",arr1)
#two dimensional array or multi dimensional array
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("this is the two dimensional or multidimensional array",arr2)
#indexing an the array
#suppose i want to access the 3rd element of the arr1
print("this is the 3rd element of the arr1",arr1[2])
#suppose i want to access the 3rd element of the arr2 which is present in the column 2
print("this is the 3rd element of the arr2",arr2[1,2])
#now we perform boolean indexing
#suppose i want to access the element which is greater than 5
condition = arr2>5
print("the element which is greater than 5",arr2[condition])
#now we perform the slicing
#suppose i want to access the element from 2 to 4
print("the element from 2 to 4 is ",arr1[1:4])
#now we perform the slicing in the multidimensional array
print("the elements from 2 to 4 in the multidimensional array",arr2[0,1:4])#this is column wise slicing which we performed in first column
#now we perform for the second column
print("the elements from 2 to 4 in the multidimensional array",arr2[1,1:4])#this is column wise slicing which we performed in second column
#creating boolean array with condition 
#suppose i want to check the element which is greater than 2 but lesser than 5 in arr2
#for that is use the logical operator such as & , | , ~
#& is use for and operator
#| is use for or operator
#~ is use for not operator
condition2 = (arr2>2) & (arr2<5)
print("the element which is greater than 2 but lesser than 5",arr2[condition2])#like this we perform the operation on the array
#now we perform the element wise  condition
condition3 = np.where(arr2>2,arr2,0) #this is the element wise condition
print("the element which is greater than 2",condition3)
#now we perform the operation on the array
#suppose i want to add the 2 in the array
print("the addition of the 2 in the array",arr2+2)
#suppose i want to subtract the 2 in the array
print("the subtraction of the 2 in the array",arr2-2)
#suppose i want to multiply the 2 in the array
print("the multiplication of the 2 in the array",arr2*2)
#suppose i want to divide the 2 in the array
print("the division of the 2 in the array",arr2/2)
#now we perform the operation using np.logical_and,np.logical_or,np.logical_not
#suppose i want to perform the logical and operation
print("the logical and operation",np.logical_and(arr2>2,arr2<5))
#suppose i want to perform the logical or operation
print("the logical or operation",np.logical_or(arr2>2,arr2<5))
#suppose i want to perform the logical not operation
print("the logical not operation",np.logical_not(arr2>2,arr2<5))
#now we perform using np.isin function
#suppose i want to check the element which is present in the array or not
print("the element which is present in the array or not",np.isin(arr2,2))#this will represent the result in the form of boolean
#now we see the shapes in array using numpy
shape1 = np.array([1,2,3,4,5,6])
#suppose i want to create upper array as 2x3 matrix
reshaped_shape1 = shape1.reshape(2,3)
print("the reshaped matrix is ",reshaped_shape1)
#now we see the flattening of the array :- means suppose we have a 2d array we wanted to convert it into an 1d array that why we use the flattening method
shape2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
reshaped_shape2 = shape2.flatten()
print("the flattened array is ",reshaped_shape2)
#now we see the transpose of the array
#suppose i want to transpose the array
print("the transpose of the array is ",shape2.transpose())
#now we see the concatenation of the array
#suppose i want to concatenate the two array
arr3 = np.array([1,2,3,4,5])
arr4 = np.array([6,7,8,9,10])
print("the concatenated array is ",np.concatenate((arr3,arr4)))#we use the concatenate function to concatenate the array
#now we add the dimension in the array
#suppose i want to add the dimension in the array
print("the dimension of the array is ",np.stack((arr3,arr4),axis=1))#we use the stack function to add the dimension in the array
#now we see the split function
#suppose i want to split the array into two parts
arr5 = np.array([1,2,3,4,5,6,7,8,9,10])
print("the split array is ",np.split(arr5,2)) #we use the split function to split the array into two parts
#now we see the hsplit function
#suppose i want to split the array horizontally
print("the horizontally split array is ",np.hsplit(arr5,2))#we use the hsplit function to split the array horizontally
#now we see the vsplit function
#suppose i want to split the array vertically
arr6 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("the vertically split array is ",np.vsplit(arr6,2))#we use the vsplit function to split the array vertically
#now we see the arange function
#suppose i want to create the array from 1 to 10
print("the array from 1 to 10 is ",np.arange(1,11))#we use the arange function to create the array from 1 to 10
#broadcasting in numpy 
#suppose i want to add the 2 in the array
arr7 = np.array([1,2,3,4,5])
print("the addition of the 2 in the array",arr7+2)
arr8 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("the addition of the 2 in the array",arr8+2)
#the addition that we performed that is in the same access 
#now we see that how we can add in different access
arr9 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
add2 = np.array([1,2,3,4,5])
print("the addition of the 2 in the array",arr9+add2)
arr10 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
add3 = np.array([[10],[20]])
print("the addition of the 2 in the array",arr10+add3)
#now we see the structure array in numpy
#suppose i want to create the structure array
data_type = [('name','S10'),('age','int'),('marks','float')]
students_details = [('abc',20,90.5),('xyz',21,95.5)]
students = np.array(students_details,dtype=data_type)
print("the structure array is ",students)
#accessing element by felid name 
print("the name of the student is ",students['name'])
#accessing the specific element by index
print("the name of the student is ",students[0]['name'])
students[0]['name']="nikhil"
print("the name of the student is ",students[0]['name'])

#reading and writing  array data on a file
#suppose i want to write the array data in the file
arr11 = np.array([1,2,3,4,5])
np.save('my_array',arr11)
#suppose i want to read the array data from the file
arr12 = np.load('my_array.npy')
print("the array data is ",arr12)
#suppose i want to write the array data in the text file
arr13 = np.array([1,2,3,4,5])
np.savetxt('my_array.txt',arr13)
#suppose i want to read the array data from the text file
arr14 = np.loadtxt('my_array.txt')
print("the array data is ",arr14)


