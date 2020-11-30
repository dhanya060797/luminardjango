students=[[1081,"ajay","mca",150],
          [1002,"vijay","bca",145],
          [3992,"dhanya","mca",908]]
#print
for student in students:
    print(student)
#print rollno
for student in students:
    print(student[0])
#print all student details whose course ="mca"
for student in students:
    if student[2]=='mca':
        print(student)
#total>200
for student in students:
    if student[3]>=200:
        print(student)
#finf total sum of total by course
totalmc=0
totalbc=0
for student in students:
    if student[2]=='mca':
        totalmc+=student[3]
    elif student[2]=='bca':
        totalbc+=student[3]
print("mca total is",totalmc)
print("bca total is",totalbc)

