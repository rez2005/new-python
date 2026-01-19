from class1 import Restaurant
my_restaurant=Restaurant('a','b')
my_restaurant.describe_restaurant()

import class1 as c1
my_admin=c1.Admin('Admin','User')
my_admin.privileges.add_privilege('can add post')
my_admin.privileges.show_privileges()

import random
class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        result = random.randint(1, self.sides)
        print(f"Rolled a {self.sides}-sided die: {result}")
        return result

six_sided_die = Die()
ten_sided_die = Die(10)
twenty_sided_die = Die(20)
for _ in range(10):
    six_sided_die.roll_die()
    ten_sided_die.roll_die()
    twenty_sided_die.roll_die()

lottery_numbers = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']
winning_number = random.sample(lottery_numbers, k=5)
print("Winning number:", ''.join(winning_number))

attempts = 0
while True:
    attempts += 1
    my_ticket = random.sample(lottery_numbers, k=5)
    if set(my_ticket) == set(winning_number):
        print(f"\n中奖了！")
        print(f"尝试次数: {attempts}")
        break






