names=["a","b","c","d","e","f"]
passed=["a","b","c"]
st=set(names)
print(st)
st2=set(passed)
print(st2)
failed=st.difference(st2)
print(failed)