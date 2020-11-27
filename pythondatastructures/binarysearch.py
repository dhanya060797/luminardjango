lst=[2,1,5,8,7,6,8,10,3,11]
#step1:sort
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)-1):
        if(lst[i]>lst[j]):#2>1
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
elem=int(input("enter number"))
print(lst)
low=0
upp=len(lst)-1
while(low<upp):
    mid=(low + upp)//2
    #case1
    if(elem>lst[mid]):
        low=mid+1
    elif(elem<lst[mid]):
        upp=mid-1
    elif(elem==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")


#10>lst[mid] 10>6
#case1 low=mid+1
#case2 :elem<lst[mid]2<6
#upp=mid-1
#case3:if elem==lst[mid],elem found

