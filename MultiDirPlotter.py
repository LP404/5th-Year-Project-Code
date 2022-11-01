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
        m,c,err = F.LineValFinder(vars()[vars()['files'+dirs[i]][j]][0],vars()[vars()['files'+dirs[i]][j]+'newY'],10)
        yFit = m * vars()[vars()['files'+dirs[i]][j]][0] + c
        Contstraint = (yFit >= 0) & (yFit <= max(vars()[vars()['files'+dirs[i]][j]+'newY']))
        
        line1start = (min(vars()[vars()['files'+dirs[i]][j]][0]),0)
        line1end = (max(vars()[vars()['files'+dirs[i]][j]][0]),0)    
        
        line2start = (min(vars()[vars()['files'+dirs[i]][j]][0][Contstraint]),min(yFit[Contstraint]))
        line2end = (max(vars()[vars()['files'+dirs[i]][j]][0][Contstraint]),max(yFit[Contstraint]))
    
        vars()[vars()['files'+dirs[i]][j]+'Intercept'] = F.LineIntersection((line1start,line1end),(line2start,line2end))    
        
        # plt.plot(vars()[vars()['files'+dirs[i]][j]][0][Contstraint],yFit[Contstraint],label = 'Intercept = '+str(np.around(vars()[vars()['files'+dirs[i]][j]+'Intercept'][0],2)))
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Transmittance, E_bg =' + str(np.around(vars()[vars()['files'+dirs[i]][j]+'Intercept'][0],2)))
        plt.title(vars()['files'+dirs[i]][j] + " " + dirs[i])
        plt.legend()