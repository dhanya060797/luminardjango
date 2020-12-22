lst=[10,11,12,13,14,15]
#squares
#map(function,iterable)

# def squ(no):
#     return no**2
# squares=map(squ,lst)
# print(squares)
squares=list(map(lambda n1:n1**2,lst))
print(squares)
cubes=list(map(lambda n:n**3,lst))
print(cubes)

