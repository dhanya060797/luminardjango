#fetch only even numbers
lst=[10,20,30,15,40,60]
even=list(filter(lambda n:n%2==0,lst))
print(even)