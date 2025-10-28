people={'jk' : {'first_name': 'j','last_name': 'k','age':"180",'city':'Shanghai'},
'ak' :{'first_name': 'a','last_name': 'k','age':"122",'city':'Beijing'},
'aad' :{'first_name': 'aa','last_name': 'd','age':"2",'city':'Chongqing'}}
for person,informatin in people.items():
	print(person,informatin)
pets=[{'a':'1','b':'2'},{'c':'2','d':'3'},{'d':'2','e':'4'}]
print(pets)
favorite_numbers = {'adad':['1','2','3'],'dasd':['2','5','7'],'asdf':['4','2','8']}
for person,numbers in favorite_numbers.items():
	print(f"{person}:")
	for number in numbers:
		print(number)
cities={'Shanghai':{'a':'1','b':'2'},'Beijing':{'c':'3','d':'4'}}
cities['Chongqing']={'e':'5','f':'6'}
del cities['Shanghai']
cities['Beijing']={'g':'7','h':'8'}
for city,information in cities.items():
	print(city)
	for letter,number in information.items():
		print(f"{letter}:{number}")
	