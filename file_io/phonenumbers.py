f=open("data","r")
st=set()
for lines in f:
    st.add(lines.rstrip("\n"))
print(st)
