jk = {'first_name': 'j','last_name': 'k','age':"180",'city':'Shanghai'}
print(f"{jk['first_name']},{jk["last_name"]},{jk['age']},{jk['city']}")
favroite_numbers = {
	'a':'1',
	'b':'2',
	'c':'3',
	'd':'4',
}
print(f"{favroite_numbers}")
favroite_numbers['a']='5'
del favroite_numbers['b']
print(f"{favroite_numbers}")
print(f"{favroite_numbers.get('b','nothing')}")
for letter,number in favroite_numbers.items():
	print(f"{letter.title()}:{number}\n")
rivercountry = {'nile':'Egypt','yangtze':'China','Amazon':'Brazil'}
for river in rivercountry.keys():
	print(river)
for country in rivercountry.values():
	print(country)