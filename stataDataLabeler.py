#Quickly label data in stata
import csv
import os
os.chdir('T:\\Middlebury\\OneDrive - Middlebury College\\2021 2Summer\\Pulse')
lecsv = "key.csv"
vals = []
labs = []

with open (lecsv) as keyfile:
    csv_reader = csv.reader(keyfile,delimiter = ",")
    for row in csv_reader:
        vals.append(row[0])
        labs.append(row[1])

labName = "week_lab"
outputstring = "label define " + labName + " "
for i in range(0,len(vals) - 1):
    outputstring = outputstring + vals[i] + ' "' + labs[i] + '" '
print(outputstring)