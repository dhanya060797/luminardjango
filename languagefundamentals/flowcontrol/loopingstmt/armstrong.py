num=int(input("enter number"))
res=0
while(num!=0):
    dig=num%10
    res=res+(dig**3)
    num=num//10
print(res)