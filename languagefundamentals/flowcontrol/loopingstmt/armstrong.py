num=int(input("enter number"))#153
res=0
t=num
while(t>0):
    dig=t%10#153%10
    res=res+(dig**3)
    t=t//10#15
#print(res)
if t == res:
    print("arm")
else:
    print("not")