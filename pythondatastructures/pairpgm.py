lst=[2,1,3,4,6,7]
lst.sort()
low=0
upp=len(lst)-1
elem=int(input("enter num"))
while(low<=upp):
    total=lst[low]+lst[upp]
    #case1
    if(elem<total):
        upp=upp-1
    #case2
    elif(elem>total):
        low=low+1
    #case3
    elif(elem==total):
        print("pairs are",lst[low] ,lst[upp])
        break