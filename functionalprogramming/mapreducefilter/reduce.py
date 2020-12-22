from functools import *
lst=[10,11,12,13,14,15]
sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)
#min
min=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(min)

#ma
ma=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(ma)

#sum of even numbers
evensum=reduce(lambda n1,n2:n1+n2,list(filter(lambda n:n%2==0,lst)))
print(evensum)

#min of even number
evenmini=reduce(lambda n1,n2:n1 if n1<n2 else n2,
                list(filter(lambda n:n%2==0,lst)))
print(evenmini)
