
nums=[1,3,5,7,9]

it=iter(nums)

print(it.__iter__())
print(it.__next__())
print(next(it))

#we can also write these iterator for our own objects which can be used in for loops