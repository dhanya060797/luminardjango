number=int(input("enter number"))
for i in range(2,number):
    if(number%i==0):
        flag=1
        break
    else:
        flag=0
if(flag==0):
        print("prime")
else:
        print("not prime")