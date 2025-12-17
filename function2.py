def makesandwiches(*toppinngs):
	for topping in toppinngs:
		print(topping)
makesandwiches('a')
makesandwiches('b','c')
makesandwiches('c','d','e')
def buildprofiles(first,last,**infomation):
	infomation['first_name']= first
	infomation['last_name']= last
	return infomation
Iam = buildprofiles('r','enze',address='Chongqing')
print(Iam)
