f=open("emp","r")
emp_dict={}
for lines in f:
    print(lines)
    id,name,des,ep,sal=lines.rstrip("\n").split(",")

    if id not in emp_dict:
        emp_dict[id]={"id":id,"name":name,"design":"devop","ep":"ep"}
    print(emp_dict)