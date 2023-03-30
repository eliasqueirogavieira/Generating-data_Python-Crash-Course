from die import Die
import matplotlib.pyplot as plt

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []

results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_result+1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results with matplotlib.
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.bar(poss_results, frequencies, edgecolor='black')

# Customize the chart.
ax.set_title(f"Results of rolling Two D6 Dices 1000 times.", fontsize=24)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=6)
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
plt.show()