import numpy as np
import os
import matplotlib.pyplot as plt
import functions as F


        

path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('MultiDirPlotter.py')) + '\\Data'))

for i in range(len(dirs)):
    
    vars()['path'+dirs[i]], vars()['dirs'+dirs[i]], vars()['files'+dirs[i]] = next(os.walk(os.path.dirname(os.path.realpath('UV_Vis_plotter.py')) + '\\Data\\' + dirs[i]))


Val1, Val2 = 3, 0.035


suffix = ".txt"

for i in range(len(dirs)):
    for j in range(len(vars()['files'+dirs[i]])):
        vars()['files'+dirs[i]][j] = vars()['files'+dirs[i]][j][:-len(suffix)]  
        
        vars()[vars()['files'+dirs[i]][j]] = np.loadtxt(open(vars()['path'+dirs[i]] + "\\" + vars()['files'+dirs[i]][j] + ".txt", "rb"), delimiter=",",skiprows = 2).T
        vars()[vars()['files'+dirs[i]][j]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[vars()['files'+dirs[i]][j]][1])
        
        
        
        
        plt.figure(i*10 + j)
        plt.plot(vars()[vars()['files'+dirs[i]][j]][0],vars()[vars()['files'+dirs[i]][j]][1],label = vars()['files'+dirs[i]][j])
        plt.plot(vars()[vars()['files'+dirs[i]][j]][0],vars()[vars()['files'+dirs[i]][j]+'newY'],label = vars()['files'+dirs[i]][j]+' filtered')
        Point = np.where(np.gradient(vars()[vars()['files'+dirs[i]][j]+'newY']) == max(np.gradient(vars()[vars()['files'+dirs[i]][j]+'newY'])))[0][0]
        # m,c,err = F.LineValFinder(vars()[vars()['files'+dirs[i]][j]][0],vars()[vars()['files'+dirs[i]][j]+'newY'],10)
        # yFit = m * vars()[vars()['files'+dirs[i]][j]][0] + c
        # Contstraint = (yFit >= 0) & (yFit <= max(vars()[vars()['files'+dirs[i]][j]+'newY']))
        
        # line1start = (min(vars()[vars()['files'+dirs[i]][j]][0]),0)
        # line1end = (max(vars()[vars()['files'+dirs[i]][j]][0]),0)    
        
        # line2start = (min(vars()[vars()['files'+dirs[i]][j]][0][Contstraint]),min(yFit[Contstraint]))
        # line2end = (max(vars()[vars()['files'+dirs[i]][j]][0][Contstraint]),max(yFit[Contstraint]))
    
        # vars()[vars()['files'+dirs[i]][j]+'Intercept'] = F.LineIntersection((line1start,line1end),(line2start,line2end))    
        
        # plt.plot(vars()[vars()['files'+dirs[i]][j]][0][Contstraint],yFit[Contstraint],label = 'Intercept = '+str(np.around(vars()[vars()['files'+dirs[i]][j]+'Intercept'][0],2)))
        plt.xlabel('Wavelength (nm)')
        # bgEn = (3e8 * 6.63e-34)/(vars()[vars()['files'+dirs[i]][j]+'Intercept'][0]*1e-9)
        # bgeV =  np.around((6.242e18 * bgEn),2)
        # plt.ylabel('Transmittance, E_bg =' + str(bgeV)+'eV')
        plt.ylabel('Transmittance')        
        plt.title(vars()['files'+dirs[i]][j][3:-3] + " " + dirs[i])
        plt.legend()
        

prefix = ( "01","02","03","04","05","06","07","08","09","0A","0B","0C","0D","0E","0F")

SamBin = [[] for _ in range(len(prefix))]



prefixDict = { "01" : "Ag3BiI6_I"
          ,"02" : "Ag3BiI6_II"
          ,"03" : "Cu2AgBiI6_V"
          ,"04" : "Cu2AgBiI6_VI"
          ,"05" : "CuAgBiI5_VII"
          ,"06" : "CuAgBiI5_VIII"
          ,"07" : "Ag2BiI5_IX"
          ,"08" : "Ag2BiI5_X"
          ,"09" : "Ag2BiI5_B1"
          ,"0A" : "Ag2BiI5_B2"
          ,"0B" : "Ag3BiI6_B2"
          ,"0C" : "null"
          ,"0D" : "null"
          ,"0E" : "null"
          ,"0F" : "null"}
        
for i in range(len(dirs)):
    for j in range(len(vars()['files'+dirs[i]])):
        SamBin[prefix.index(vars()['files'+dirs[i]][j][0:2])].append([vars()[vars()['files'+dirs[i]][j]][0],vars()[vars()['files'+dirs[i]][j]+'newY'],vars()['files'+dirs[i]][j][0:2],dirs[i]])
        
SamBin = list(filter(None,SamBin))

for i in range(len(SamBin)):
    for j in range(len(SamBin[i])):
        plt.figure(i+1*200)
        plt.title(prefixDict[SamBin[i][j][2]])
        plt.ylabel('Transmittance (%)')
        plt.xlabel('wavelength (nm)')
        plt.plot(SamBin[i][j][0],SamBin[i][j][1], label = SamBin[i][j][3])
        plt.legend()
        
        



