names=["ajay","dhanya","appu"]
na=list(map(lambda name:name.upper(),names))
print(na)
#select name start with 'a' pr ind==0
aname=list(filter(lambda name:name[0]=='a',names))
print(aname)