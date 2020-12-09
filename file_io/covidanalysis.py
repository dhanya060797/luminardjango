f=open("complete.csv")
covid_data={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1]
    confirmed=data[4]
    cured=data[6]
    death=data[5]
    if state not in covid_data:
        covid_data[state]={
            "state":state,
            "confirmed":confirmed,
            "cured":cured,
            "death":death

        }
    else:
        covid_data[state] = {

            "state": state,
            "confirmed": confirmed,
            "cured": cured,
            "death": death
        }
i=0
for k,v in covid_data.items():
    if i==5:
        break
    print(k,v)

def print_covid_data(**kwargs):
    state=kwargs.get("state")
    if state in covid_data:
        print(state,covid_data[state]["confirmes"])
        if "property" in kwargs:
            prop=kwargs["property"]
            if prop in covid_data[state]:
                print(covid_data[state][prop])
    else:
        print("there is no state with provided name")


