import numpy as np
import os
import matplotlib.pyplot as plt
import functions as F 

path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('PhotoPlotter.py')) + '\\PhotoDir\\IV'))
path1, dirs1, files1 = next(os.walk(os.path.dirname(os.path.realpath('PhotoPlotter.py')) + '\\PhotoDir\\time'))

Val1, Val2 = 3, 0.035

axis = np.arange(0,195,15)

suffix = ".csv"



for i in range(len(files)):
    files[i] = files[i][:-len(suffix)]  
    
    vars()[files[i]] = np.loadtxt(open(path + "\\" + files[i] + ".csv", "rb"), delimiter=",",skiprows = 2).T
    vars()[files[i]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[files[i]][1])

    plt.figure(i)
    plt.plot(vars()[files[i]][0],vars()[files[i]][1],label = files[i])
    plt.plot(vars()[files[i]][0],vars()[files[i]+'newY'],label = files[i]+' filtered')
    
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (A)')
    plt.title(files[i])
    
for i in range(len(files)):
    files1[i] = files1[i][:-len(suffix)]  
    
    vars()[files1[i]] = np.loadtxt(open(path1 + "\\" + files1[i] + ".csv", "rb"), delimiter=",",skiprows = 2).T
    vars()[files1[i]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[files1[i]][1])

    plt.figure(i+len(files1)+len(files))
    plt.xticks(axis)
    plt.plot(vars()[files1[i]][0],vars()[files1[i]][1],label = files1[i])
    plt.plot(vars()[files1[i]][0],vars()[files1[i]+'newY'],label = files1[i]+' filtered')
    
    plt.xlabel('time (s)')
    plt.ylabel('Current (A) ')
    plt.title(files1[i])