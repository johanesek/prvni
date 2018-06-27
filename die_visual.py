import pygal

from die import Die

die = Die()

results = []
for roll_num in range(1000):
    results.append(die.roll())

frequencies = []
for value in range(1, 1+die.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)
#visualisation - histogram

hist = pygal.Bar()

hist.title = "Results D6 1000x times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "result"
hist.y_title = "frequency of result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
