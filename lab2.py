'''
This is a software tool that displays points on a coordinate plane 
based on a given dataset and 
saves the image in one of the graphic formats.
developed by Obrotskyi Myroslav group: KM-22.
'''

import matplotlib.pyplot as plt

# Reading data from the file
with open('DS7.txt', 'r') as file:
    data = [tuple(map(int, line.split())) for line in file]

# Canvas size
canvas_size = (960, 540)

# Сreating graphic
fig, ax = plt.subplots(figsize=(canvas_size[0]/100, canvas_size[1]/100), dpi=100)
ax.set_xlim(0, canvas_size[0])
ax.set_ylim(0, canvas_size[1])

# Display of points on the graph
x, y = zip(*data)
ax.scatter(x, y, s=5, color='black')

# Savimg graphic in format PNG
plt.savefig('output.png')

# Graphics output
plt.show()
