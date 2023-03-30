from die import Die
import plotly.express as px

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

# Visualize the results.
title = f"Results of Rolling Two D6s 1000 times."
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# Further customize chart
fig.update_layout(xaxis_dtick=1)
fig.write_html('die_visual_2multd6.html')
fig.show()