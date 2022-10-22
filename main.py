# Jacob Rebell
# This program will autmatically resize based on how many countries are in the file and the maximum population in the file.

import arcade

graph_file = open('nationsPop.txt', 'r')
graph = graph_file.readlines()
#Dictionaries to help me pull data for the graph
pop_dict = {}
growth_dict = {}
#A list to enable pulling the country names one at a time for the x axis
countries = []
#How resizing works
num_countries = 0
max_pop = 0
#Used to pull from countries in a for loop
counter = 0
#Splitting the file and adding information to its respective dictionaries
for line in graph:
    info = line.split(',')
    country = info[0]
    population = info[1]
    growth = info[2]
    pop_dict[country] = population
    growth_dict[country] = growth
    num_countries += 1
    pop = int(population)
    if pop > max_pop:
        max_pop = pop
#Doing the math for window sizing
win_x = num_countries * 100 + 100
win_y = max_pop // 1_000_000 + 100
win = arcade.open_window(win_x, win_y, "JRebell Project 4")
arcade.set_background_color(arcade.color.WHEAT)
arcade.start_render()
arcade.draw_line(50, 50, win_x, 50, arcade.color.BLACK, 5)
arcade.draw_line(50, 50, 50, win_y, arcade.color.BLACK, 5)
#Printing the text on y axis for the population. The if statement will switch from Millions to Billions after 1B is reached.
#This makes the graph more readable along with fixing a collision with the y axis line and the numbering with a fourth digit
for y in range(0, win_y, 100):
    print(y)
    if y < 1000:
        y_axis = arcade.Text(f"{y}M", 0, y + 55, arcade.color.BLACK, 5)
    else:
        y_axis = arcade.Text(f"{y / 1000}B", 0, y + 55, arcade.color.BLACK, 5)
    y_axis.font_size = 12
    y_axis.draw()
#Actually adding the country name into the list countries
for key in pop_dict.keys():
    countries.append(key)
#Drawing the country names and the bars in one loop. It could probably be rewritten shorter as I was fighting an issue
#where the program would complain about not being able to compare a string to an interger then would not work because I
#turned grow into an interger instead of a floating point. It works so I left it.
for x in range(100, win_x , 100):
    x_axis = arcade.Text(f"{countries[counter]}", x, 8, arcade.color.BLACK, 2)
    x_axis.font_size = 12
    x_axis.draw()
    grow = growth_dict[countries[counter]]
    grow = grow.strip()
    grow = float(grow)
    if grow > 0:
        color = arcade.color.MOSS_GREEN
    else:
        #Interesting they have BU Red in arcade
        color = arcade.color.BOSTON_UNIVERSITY_RED
    arcade.draw_xywh_rectangle_filled(x, 55, 50, int(pop_dict[countries[counter]])/1_000_000, color)
    counter += 1


arcade.finish_render()

arcade.run()