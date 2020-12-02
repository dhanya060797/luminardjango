employees=[[1001,"ajay","qa",1981,2003],
          [1882,"vijay","devoloper",1992,2008],
          [1884,"arun","ba",1989,2010],
          [1884,"amal","devoloper",2009,2014]

for emp in employees:
    if ((emp[4]-emp[3])>9):
        print(emp)