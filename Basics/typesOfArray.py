from numpy import *

arr=array([],[])

arr1=linspace(1,10,2)
print(arr1)
arr2=logspace(1,3,5)
print(arr2)
print(arange(1,5,3))
print(zeros(4))
print(ones(2))

arr3=array([1,2,3,4])
arr4=array([1,2,1,2])
arr5=arr3+arr4
arr6=arr3+5
print(arr5,arr6)
print(concatenate([arr3,arr4]))

arr7=arr3
print(arr7,arr3,id(arr7),id(arr3))

arr8=arr3.view()
arr3[2]=6
print(arr8,arr3,id(arr8),id(arr3))

arr9=arr4.copy()
arr4[2]=7
print(arr9,arr4,id(arr9),id(arr4))
