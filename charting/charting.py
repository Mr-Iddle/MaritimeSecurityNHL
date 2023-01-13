# needs manual pip import when not working
import matplotlib.pyplot as plt
import os

names = []
work = []
 
# Get the directory where the current file is located
#set total directory to avid errors
currentDir = os.path.dirname(os.path.abspath(__file__))
logFile = os.path.join(currentDir, "log.txt")

for line in open(logFile, 'r'):
    Data = [i for i in line.split()]
    names.append(Data[0])
    New_Data= [ j for j in Data[1].split('%')]

    work.append(New_Data[0])
colors = ['yellow', 'b', 'green', 'cyan','red']

# plotting pie chart 
plt.pie(work, labels = names, colors = colors, startangle = 90,
    shadow = True, radius = 1.2, autopct = '%1.1f%%')
plt.show()
