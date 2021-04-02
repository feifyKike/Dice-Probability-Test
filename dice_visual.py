from die import Die
import pygal

die = Die()
die_2 = Die()

# Make some rolls, and store the results in a list
results = []
for roll_num in range(1000):
    result = die.roll() + die_2.roll()
    results.append(result)

# Analyze the frequency of each number
frequencies = []
max_result = die.num_sides + die_2.num_sides
lowest_value = min(range(1, die.num_sides)) + min(range(1, die_2.num_sides))
for value in range(lowest_value, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Creating the visual
hist = pygal.Bar()
hist.title = "Results of rolling a two D6 die 1000 times"
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_labels = []

# Automating the x_label to coincide with highest and lowest values
for number in range(lowest_value, max_result+1):
    hist.x_labels.append(str(number))
    

hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual_new.svg')
