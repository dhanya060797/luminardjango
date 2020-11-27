list=[12,2,34,5,77,51]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if(list[i]<list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print(list)
print(list[1],"second lar")
