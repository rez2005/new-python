sandwichs_orders=['a','b','c','b','b']
finished_sandwiches=[]
while sandwichs_orders:
	sandwich=sandwichs_orders.pop()
	print(f"I am preparing {sandwich} for you.")
	finished_sandwiches.append(sandwich)
print("Every sandwich is ready")
print("'b' has run out.")
while 'b' in finished_sandwiches:
	finished_sandwiches.remove('b')
print(finished_sandwiches)
numbers={}

while 1:
	name=input("What's your name?")
	number=input("What's your favorite number?")
	if name == 'quit':
		break
	numbers[name]= number
for name,number in numbers.items():
	print(f"{name}'s favorite number is {number}")



