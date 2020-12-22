num=int(input("enter number"))#54
res=0
while(num!=0):
    dig=num%10#4
    res=res*10+dig#4
    num=num//10#5
print(res)