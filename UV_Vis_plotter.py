import numpy as np
import os
import matplotlib.pyplot as plt
import functions as F


path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('UV_Vis_plotter.py')) + '\\SingleDirData'))

Val1, Val2 = 3, 0.035


suffix = ".txt"



for i in range(len(files)):
    files[i] = files[i][:-len(suffix)]  
    
    vars()[files[i]] = np.loadtxt(open(path + "\\" + files[i] + ".txt", "rb"), delimiter=",",skiprows = 2).T
    vars()[files[i]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[files[i]][1])
    
    
    
    
    plt.figure(i)
    plt.plot(vars()[files[i]][0],vars()[files[i]][1],label = files[i])
    plt.plot(vars()[files[i]][0],vars()[files[i]+'newY'],label = files[i]+' filtered')
    Point = np.where(np.gradient(vars()[files[i]+'newY']) == max(np.gradient(vars()[files[i]+'newY'])))[0][0]
    m,c,err = F.LineValFinder(vars()[files[i]][0],vars()[files[i]+'newY'],10)
    yFit = m * vars()[files[i]][0] + c
    Contstraint = (yFit >= 0) & (yFit <= max(vars()[files[i]+'newY']))
    
    line1start = (min(vars()[files[i]][0]),0)
    line1end = (max(vars()[files[i]][0]),0)    
    
    line2start = (min(vars()[files[i]][0][Contstraint]),min(yFit[Contstraint]))
    line2end = (max(vars()[files[i]][0][Contstraint]),max(yFit[Contstraint]))

    vars()[files[i]+'Intercept'] = F.LineIntersection((line1start,line1end),(line2start,line2end))    
    
    # plt.plot(vars()[files[i]][0][Contstraint],yFit[Contstraint],label = 'Intercept = '+str(np.around(vars()[files[i]+'Intercept'][0],2)))
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Transmittance, E_bg =' + str(np.around(vars()[files[i]+'Intercept'][0],2)))
    plt.title(files[i])
    plt.legend()