#to read file
#name=open(file name,mode of operation)
f=open("tst","r")
#for lines in f:
#    print(lines)
lst=[]
for lines in f:
    lst.append(lines.rstrip("\n"))
print(lst)