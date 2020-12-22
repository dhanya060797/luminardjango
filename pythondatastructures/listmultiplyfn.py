list=[2,3,4,6]#(2*1,3**2,4**3,]
count=1
out=[]
for num in list:
    data=num**count
    out.append(data)
    count+=1
print(out)