employee=[[1001,"ajay","qa",1981,15000],
          [1882,"vijay","devoloper",1992,25000],
          [1884,"arun","ba",1989,15000],
          [1884,"amal","devoloper",2009,38800]]
#print emp id
for i in employee:
    print(i[0])
#find total of salary
totalsal=0
for i in employee:
    totalsal+=i[3]
print(totalsal)
#how many workers as devolper
count=0
for i in employee:
    if i[2]=="devoloper":
        count+=1
print(count)
#find total of salary by designation
totalqa=0
totalba=0
totaldev=0
for i in employee:
    if i[2]=="qa":
        totalqa+=i[3]
    elif i[2]=="ba":
        totalba+=i[3]
    elif i[2]=="devoloper":
        totaldev+=i[3]
print("qa total salary",totalqa)
print("ba total salary",totalba)
print("devoloper total salary",totaldev)
#print all employee designation
for i in employee:
    print(i[2])

#all empl whose des=devoloper
for i in employee:
    if(i[2]=="devolper"):
        print(i[1])
#working in 1980s
for i in employee:
    if 1990>=i[3]>=1980:
        print(i[1])
#eperience >9 yrs
employee1=[[1001,"ajay","qa",1981,2003],
          [1882,"vijay","devoloper",1992,2008],
          [1884,"arun","ba",1989,2010],
          [1884,"amal","devoloper",2009,2014]
ep=i[4]-inti[3]
for i in employee1:
    if(ep>9):
        print(i[1])
