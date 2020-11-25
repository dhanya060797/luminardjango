bdaydate=input("enter the b date dd-mm-yyyy")
cdate=input("enter the c date dd-mm-yyyy")
bdate,bmonth,byear=bdaydate.split("-")
cudate,cumonth,cuyear=cdate.split("-")
print(bdaydate)
print(cdate)
age=int(cuyear)-int(byear)
print(age)
if(cumonth<=bmonth):
    if(cudate<bdate):
        age-=1
print("you are",age,"years old")