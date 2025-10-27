usernames = ['a','b','c','d','admin']
for username in usernames:
	if username == 'admin':
		print("Hello admin!")
	else:
		print("Thank you for logging in.")
usernames1 = []
if usernames1:
	print("Thank you for logging in.")
else:
	print("We need some new users.")


new_users = ['a','b','C','D','g']
upper_usernames = ['A','B','C','D','ADMIN']
for new_user in new_users:
	if (new_user in usernames) or (new_user in upper_usernames):
		print("You need to enter a new username.")
	else:
	    print("The username is valid.")


