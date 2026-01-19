class Restaurant():
	"""docstring for restaurant"""
	def __init__(self,name,cuisine):
		self.name=name
		self.cuisine=cuisine
		self.number_served=0

	def describe_restaurant(self):
		print(f"The restaurant name is {self.name}.")
		print(f"The cuisine type is {self.cuisine}.")

	def open_restaurant(self):
		print(f"{self.name} is now open!")

	def set_number_served(self,number):
		self.number_served=number
		print(f"Number of customers served: {self.number_served}")
	
	def increment_number_served(self,increment):
		self.number_served+=increment
		print(f"Number of customers served: {self.number_served}")

my_restaurant=Restaurant('a','b')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print(f"The number of customers served is: {my_restaurant.number_served}")
my_restaurant.set_number_served(5)
my_restaurant.increment_number_served(3)

class User():
    """docstring for user"""
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0

    def describe_user(self):
        self.name=f"{self.first_name} {self.last_name}"
        print(f"User's full name is {self.name}.")
    def greet_user(self):
        print(f"Hello, {self.name}!")
    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f"Login attempts: {self.login_attempts}")
    def reset_login_attempts(self):
        self.login_attempts=0
        print(f"Login attempts reset to: {self.login_attempts}")

my_user=User('John','Doe')
my_user.describe_user()
my_user.greet_user()
my_user.increment_login_attempts()
my_user.reset_login_attempts()

class IceCreamStand(Restaurant):
    """docstring for IceCreamStand"""
    def __init__(self, name, cuisine='Ice Cream'):
        super().__init__(name, cuisine)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"Added flavor: {flavor}")

    def display_flavors(self):
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
my_ice_cream_stand = IceCreamStand('c')
my_ice_cream_stand.add_flavor('Vanilla')
my_ice_cream_stand.add_flavor('Chocolate')
my_ice_cream_stand.display_flavors()

class Privileges():
    def __init__(self):
        self.privileges = []

    def add_privilege(self, privilege):
        self.privileges.append(privilege)
        print(f"Added privilege: {privilege}")
    
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """docstring for Admin"""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

my_admin = Admin('Alice', 'Smith')
my_admin.privileges.add_privilege('can add post')
my_admin.privileges.add_privilege('can delete post')
my_admin.privileges.show_privileges()

   