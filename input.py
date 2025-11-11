input("What kind of rental car you would like?")
print("I can help you find it.")
number=input("How many people are in your group?")
number=int(number)
if number > 8:
	print("you have to wait it.")
else:
	print("It's ready")
if number%5==0:
	print("It's a multiple of 5.")
