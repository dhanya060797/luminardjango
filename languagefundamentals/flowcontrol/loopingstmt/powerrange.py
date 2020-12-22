number=input("enter number")#4
i=1
sum=0
while(i<=int(number)):#i<4,2<4,3<4
    data=number*i#4,8,12,16
    sum=sum+int(data)#4,12,24,40
    i+=1#2,3
print(sum)