a=int(input("enter first num"))
b=int(input("enter second num"))
c=int(input("enter third num"))
if(a>b) and (a>c):
    print("a is largest")
elif(b>a) and (b>c):
    print("b is larger")
elif(c>a) and (c>b):
    print("c is larger")
else:
    print("numbers are equal")