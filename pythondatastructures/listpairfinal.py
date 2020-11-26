list=[1,2,3,4,6,7]#values(4,2)(3,3)
total=6
for i in list:
    for j in list:
        ctotal=i+j
        if(total==(ctotal)):
            print(i,j)
            break