list=["java","python","c","javascript"]
print(list)
print(list[-1:-5:-1])
print(list[0:4])#slicing operation
for item in list:
    print(item)
list.append("dart")
print(list)
list[0]="ruby"
print(list)
list.insert(3,"perl")
print(list)