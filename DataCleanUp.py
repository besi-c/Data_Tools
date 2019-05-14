OriginalFilePath = "PATH TO THE ORIGINAL HR FILE"
NewFilePath = "PATH TO THE NEW HR FILE"

Data = open(OriginalFilePath).read()
Data = Data.split("\n")
CleanData = "TimeStamp,HR\n"
for d in Data:
    d = d.split(',')
    #print(d)
    try:
        int(d[3])
    except:
        continue

    if int(d[3]) > 1:
        CleanData += (d[0]+","+d[2]+"\n")
CleanDataFile = open(NewFilePath,'w')
CleanDataFile.write(CleanData)
CleanDataFile.close()