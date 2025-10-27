pizzas=['a','b','c']
for pizza in pizzas:
	print(f"I like {pizza.title()} pizza.")
print("I really like all the pizzas.")
friend_pizzas=pizzas[:]
pizzas.append('e')
friend_pizzas.append('d')
print(f"My favorite pizzas are{pizzas}")
print(f"My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print({pizza})
