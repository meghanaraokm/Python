
nums = [2,3,6,9,7,8]

evens=list(filter(lambda n : n%2==0,nums))
print evens

doubles=list(map(lambda a : a*2,evens))
print doubles

sum=reduce(lambda a,b : a+b,doubles)
print sum