for number in range(1,21,2):
	print(number)
for number2 in range(3,31,3):
	print(number2)
numberss=[]
for number in range(1,11):
	numberss.append(number**3)
print(numberss)
numbers=[number3**3 for number3 in range(1,11)]
print(numbers)
print(f"The first three items in the list are{numberss[0:3]}")
print(f"Three items from the middle of the list are{numberss[3:6]}")
print(f"The last three items in the list are{numberss[-3:]}")