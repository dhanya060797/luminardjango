list=[6,6,8,9,4,2,3]#[7,7,9,10,3,1,2]
out=[]
for num in list:
    if(num>5):
        out.append(num+1)
    else:
        out.append(num-1)
print(out)