from csvtools import *
from sys import argv as arg
import re
from time import time as t

# to use this scrpit call >>python accelsplit.py C:\FakePath\filename.csv C:\fakeSavePath\

t_s = t()

filename = arg[1]
savepath = arg[2]

data = open(filename)

new_data = []
currentday = ""

day = 1

# Check to verify that the element in question is actually going to be a datetime format by using
# regex:
# \d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{1,2}:\d{1,2}.?\d{,3}
# if it matches, go on, rip skip

timestampFormat = re.compile("\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{1,2}:\d{1,2}.?\d{,3}")

for line in data.readlines():
    try:
        line = line.split(',')
        if timestampFormat.match(line[0]):
            dayval = line[0].split(' ')[0].split("/")[1]
            if (currentday != ""):
                if dayval == currentday:
                    new_data.append(line)
                    continue
                else:
                    write(savepath+"Accelerometer_day_"+str(day)+".csv",new_data)
                    day += 1
                    currentday= dayval
                    new_data = []
                    new_data.append(line)
            else:
                currentday = dayval
                new_data.append(line)
                continue
    except Exception as ex:
        print("Error Occurred:", ex)
        continue
write(savepath+"Accelerometer_day_"+str(day)+".csv",new_data)
print("Done!")
print("Program completed in", t()-t_s,"s")
exit()