import pygal

from die import Die

die1 = Die()
die2 = Die()
die3 = Die()

results = []

for roll_num in range(10000):
    results.append(die1.roll()+die2.roll()+die3.roll())

frequencies = []
for value in range(2, 1+die1.num_sides + die2.num_sides + die3.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)
#visualisation - histogram

hist = pygal.Bar()

hist.title = "Results two D6 1000x times"
hist.x_labels = [str(value) for value in range(3,19)]
hist.x_title = "result"
hist.y_title = "frequency of result"

hist.add('2x D6', frequencies)
hist.render_to_file('die_visual.svg')

