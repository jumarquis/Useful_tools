# Program to read a csv file and plot the values read 
# Note: the 2 first lines are the title and a comment

import csv
import matplotlib.pyplot as plt

time = []
force = []
x_label = ""
y_label = ""
csv_title = ""

with open('8_app_double_soft.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        if plots.line_num == 1:
            x_label = row[0]
            y_label = row[1]
        elif plots.line_num == 2:
            csv_title = row[1]
        else:
            time.append(float(row[0]))
            force.append(float(row[1]))

plt.plot(time,force, label='raw force')
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(csv_title)

plt.show()

csvfile.close()
