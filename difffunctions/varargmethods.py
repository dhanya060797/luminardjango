#variable length args methods
# def add(*args):
#     total=0
#     for num in args:
#         total+=num
#     print(total)
# #     print(nums)
# add(3,4)
# add(97,29,8)
#receive as tuple
def printEmp(*args):
    print(args)
printEmp("kakkanad","ajay","always")
#in the format of dictionary
def printEmp(**args):
    print(args)
printEmp(place="kakkanad",name="ajay",working="always")
