limit=int(input("enter limit"))
lst=list()
for i in range(1,limit+1):
    lst.append(i)
print(lst)
#store even and odd into separate list
list1=[]
list2=[]
for num in lst:
    if(num%2==0):
        list1.append(num)
    else:
        list2.append(num)
print(list1)
print(list2)
