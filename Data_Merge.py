from csvtools import *

DeploymentPath = "PATH_TO_FILES"
files = ["_Battery_Activity.csv","_EndOfDay_EMA_Activity.csv","_EndOfDay_EMA_Results.csv","_Estimote_Data.csv","_Followup_EMA_Activity.csv","_Followup_EMA_Results.csv","_Heart_Rate_Data.csv","_Pain_EMA_Activity.csv","_Pain_EMA_Results.csv","_Pedometer_Data.csv","_System_Activity.csv"]

for f in files:
    # Patient Data
    try:
        ptdata = read(DeploymentPath+"PT/PT"+f)
        for i in read(DeploymentPath+"PT/PT2"+f):
            ptdata.append(i)
        ptdata = sort(ptdata)
        write(DeploymentPath+"PT/Patient"+f,ptdata)
    except:
        print()
    # CareGiver Data
    try:
        cgdata = read(DeploymentPath+"CG/CG"+f)
        for i in read(DeploymentPath+"CG/CG2"+f):
            cgdata.append(i)
        cgdata = sort(cgdata)
        write(DeploymentPath+"CG/CareGiver"+f,cgdata)
    except:
        continue

print("Done!")

