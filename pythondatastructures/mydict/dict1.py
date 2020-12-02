stud={"rol":88,"name":"dhanya","course":"python"}
print(stud["name"])#to fetch values we use key
for key in stud:
    print(key,stud[key])#print only key
for k,v in stud.items():
    print(k,v)
#updation
stud["name"]="DHANYA"
print(stud)
#checking for a key
print("rol" in stud)
print("total" in stud)
#add key
if("total" not in stud):
    stud["total"]=150
    print(stud)
stud["total"]+=50
print(stud)
stud["gender"]="male"
print(stud)