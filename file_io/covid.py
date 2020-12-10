f=open("complete.csv")
dict={}
for lines in f:
    print(lines)
    data=lines.rstrip("\n").split(",")
    #data=lines.split(",")
    print(data)
    state=data[1]
    conf=int(data[4])
    if state not in dict:
        dict[state]=int(conf)
    else:
        dict[state]=int(conf)
for k,v in dict.items():
    print(k,v)
#find state have highest confirmed cases
highest=max(dict,key=dict.get)
print("highest=",highest,dict[highest])

lowest=min(dict,key=dict.get)
print("lowest=",lowest,dict[lowest])

srt=sorted(dict,key=dict.get,reverse=True)
print("sorted order=",srt)