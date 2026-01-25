import matplotlib.pyplot as plt

input_data1 = [1, 2, 3, 4, 5]
input_data2 = [x for x in range(1, 5001)]
squared_data1 = [x**3 for x in input_data1]
squared_data2 = [x**3 for x in input_data2]
plt.style.use('seaborn-v0_8-darkgrid')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.plot(input_data1, squared_data1, linewidth=3)
ax1.set_title('Cubic Growth (1-5)', fontsize=24)
ax1.set_xlabel('value', fontsize=14)
ax1.set_ylabel('cubic value', fontsize=14)
ax1.tick_params(axis='both', labelsize=14)
ax2.scatter(input_data2, squared_data2, c=squared_data2, cmap=plt.cm.Reds, s=10)
ax2.set_title('Cubic Growth (1-5000)', fontsize=24)
ax2.set_xlabel('value', fontsize=14)
ax2.set_ylabel('cubic value', fontsize=14)
ax2.tick_params(axis='both', labelsize=14)
plt.show()

from random import choice
class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance
    
rw = RandomWalk(50000)
rw.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values,linewidth=1)
plt.show()

from random import randint
class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

die1 = Die(8)
die2 = Die(6)

from plotly.graph_objs import Bar, Layout
from plotly import offline

results1 = []
results2 = []
for roll_num in range(1000):
    result1 = die1.roll()+die1.roll()
    results1.append(result1)
    result2 = die2.roll()+die2.roll()+die2.roll()
    results2.append(result2)
results3 = [die1.roll() * die2.roll() for _ in range(1000)]
frequencies1 = []
max_result1= die1.num_sides * 2
for value in range(2, max_result1 + 1):
    frequency = results1.count(value)
    frequencies1.append(frequency)
frequencies2 = []
max_result2= die2.num_sides * 3
for value in range(3, max_result2 + 1):
    frequency = results2.count(value)
    frequencies2.append(frequency)
frequencies3 = []
max_result3= die1.num_sides * die2.num_sides
for value in range(1, max_result3 + 1):
    frequency = results3.count(value)
    frequencies3.append(frequency)
x_values1 = list(range(2, max_result1 + 1))
x_values2 = list(range(3, max_result2 + 1))
x_values3 = list(range(1, max_result3 + 1))
data1 = [Bar(x=x_values1, y=frequencies1)]
data2 = [Bar(x=x_values2, y=frequencies2)]
data3 = [Bar(x=x_values3, y=frequencies3)]
layout1 = Layout(title='Results of rolling two D8 dice 1000 times',
                 xaxis={'title':'Result'},
                 yaxis={'title':'Frequency of Result'})
layout2 = Layout(title='Results of rolling three D6 dice 1000 times',
                    xaxis={'title':'Result'},
                    yaxis={'title':'Frequency of Result'})
layout3 = Layout(title='Results of rolling one D8 and one D6 dice 1000 times',
                    xaxis={'title':'Result'},
                    yaxis={'title':'Frequency of Result'})
offline.plot({'data': data1, 'layout': layout1}, filename='d8_d8.html')
offline.plot({'data': data2, 'layout': layout2}, filename='d6_d6_d6.html')
offline.plot({'data': data3, 'layout': layout3}, filename='d8_d6.html')