import numpy as np
import os
import matplotlib.pyplot as plt
import functions as F
import random


        

path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('GlassCode.py')) + '\\GlassDir'))

for i in range(len(dirs)):
    
    vars()['path'+dirs[i]], vars()['dirs'+dirs[i]], vars()['files'+dirs[i]] = next(os.walk(os.path.dirname(os.path.realpath('GlassCode.py.py')) + '\\Data\\' + dirs[i]))


Val1, Val2 = 3, 0.035


suffix = ".txt"

for i in range(len(dirs)):
    for j in range(len(vars()['files'+dirs[i]])):
        vars()['files'+dirs[i]][j] = vars()['files'+dirs[i]][j][:-len(suffix)]  
        
        vars()[vars()['files'+dirs[i]][j]] = np.loadtxt(open(vars()['path'+dirs[i]] + "\\" + vars()['files'+dirs[i]][j] + ".txt", "rb"), delimiter=",",skiprows = 2).T
        vars()[vars()['files'+dirs[i]][j]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[vars()['files'+dirs[i]][j]][1])
        
        
prefix = ( "01","02","03","04","05","06","07","08")

SamBin = [[] for _ in range(len(prefix))]

colourlist = ['black','blue','red','orange','green','brown','purple','teal','magenta','indigo','gold','silver']

colours = np.random.choice(colourlist,size = len(dirs), replace = False)


prefixDict = { "01" : "Ag3BiI6"
          ,"02" : "Ag3BiI6_SR"
          ,"03" : "Cu2AgBiI6"
          ,"04" : "Cu2AgBiI6_SR"
          ,"05" : "CuAgBiI5"
          ,"06" : "CuAgBiI5_SR"
          ,"07" : "Ag2BiI5"
          ,"08" : "Ag2BiI5_SR"
          }
        
for i in range(len(dirs)):
    for j in range(len(vars()['files'+dirs[i]])):
        SamBin[prefix.index(vars()['files'+dirs[i]][j][0:2])].append([vars()[vars()['files'+dirs[i]][j]][0],vars()[vars()['files'+dirs[i]][j]+'newY'],vars()['files'+dirs[i]][j][0:2],dirs[i],colours[i]])
        
SamBin = list(filter(None,SamBin))

for i in range(len(SamBin)):
    for j in range(len(SamBin[i])):
        plt.figure(i+1*200)
        plt.title(prefixDict[SamBin[i][j][2]])
        plt.ylabel('Transmittance (%)')
        plt.xlabel('wavelength (nm)')
        plt.plot(SamBin[i][j][0],SamBin[i][j][1], label = SamBin[i][j][3], color = SamBin[i][j][4])
        plt.legend()
        
        



