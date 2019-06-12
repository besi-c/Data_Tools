from csvtools import *
from sys import argv as arg

# to use this scrpit call >>python accelsplit.py C:\FakePath\filename.csv C:\fakeSavePath\

filename = arg[1]
savepath = arg[2]

data = read(filename)

new_data = []
currentday = ""

day = 1

for line in data:
    try:
        float(line[1])
        if (currentday != ""):
            if line[0].split(' ')[0].split("/")[1] == currentday:
                new_data.append(line)
                continue
            else:
                write(savepath+"Accelerometer_day_"+str(day)+".csv",new_data)
                day += 1
                currentday=""
                new_data = []
        else:
            currentday = line[0].split(' ')[0].split("/")[1]
            new_data.append(line)
            continue
    except:
        continue
write(savepath+"Accelerometer_day_"+str(day)+".csv",new_data)
exit()