num1 = float(input("Value 1: "))
num2 = float(input("\nValue 2: "))

try:
	sum = num1.__add__(num2)
	print(f"\nAddition of Numbers is {sum}")
	
except:
	print("Value Error!")