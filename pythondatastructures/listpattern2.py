list=[2,5,6,3]#[14,11,10,13]
total=sum(list)
out=[]
for num in list:#5,6,3
    out.append(total-num)#16-2,16-5 so on
print(out)