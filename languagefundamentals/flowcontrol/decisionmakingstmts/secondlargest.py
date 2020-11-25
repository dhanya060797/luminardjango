num1=int(input("enter a number1"))
num2=int(input("enter a number2"))
num3=int(input("enter a number3"))

if((num1>num2)^(num1>num3)):
    print("second lar is",num1)
elif((num2>num1)^(num2>num3)):
    print("second lar is",num2)
elif((num3>num2)^(num1<num3)):
    print("second lar is", num3)
else:
    print("equal")