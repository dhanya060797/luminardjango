low=int(input("enter lower limit"))
high=int(input("enter higher limit"))
sum=0
if(low>high):
    print("error")
while(low<=high):
    if(low%2!=0):
        sum+=low
    low+=1
print(sum)