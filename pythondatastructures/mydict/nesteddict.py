stud={100:{"rol":88,"name":"dhanya","course":"python"},
      101:{"rol":81,"name":"hanya","course":"c"},
      }
# print(stud)
# print(stud[100]["name"])
# print(stud[100]["course"])
def printStudent(**kwargs):#id:101
      print(kwargs)
      id=kwargs.get("id")#id=kwargs["id"]=101
      if(id in stud):
            if "property" in kwargs:
                  prop=kwargs.get("property")#total
                  if prop in stud[id]:
                        print(stud[id][prop])
            print(stud[id]["name"])

      else:
            print("no student")
#printStudent(id=102)
printStudent(id=100,property="course")
