lst=[12,34,2,32,1]
flag=0
key=int(input("enter search elem"))
for i in lst:
    if(i==key):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("search found")
else:
    print("not")


