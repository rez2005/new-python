prompt="\nWhich topping would you like to enter?"

flag = True
while flag:
	topping=input(prompt)
	if topping =='quit':
		flag= False
	else:
		print(topping)
age="1"
count = 0
while age :
	age=input("What's your age?")
	if age == 'quit':
		break
	else:
		count=count+1
	age=int(age)
	if age <= 3:
		print("The ticket is free.")
	elif age > 3 and age <= 12:
		print("The ticket is 10 dollars.")
	else:
		print("The ticket is 15 dollars.")
	if count > 2:
		break



