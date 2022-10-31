import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
from scipy.signal import argrelextrema
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter
from scipy import stats

def LineValFinder(xArray,yArray,guage):
    

    point = np.where(np.gradient(yArray) == max(np.gradient(yArray)))[0][0]
    xSec = xArray[point - guage : point + guage]
    ySec = yArray[point - guage : point + guage] 
     
     
    m,c,r,p,err = stats.linregress(xSec,ySec)
    
    
     
    return m,c,err

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def NoiseFilter(Val1,Val2,yArray):
    b, a = butter(Val1, Val2)
    zi = lfilter_zi(b, a)
    z, _ = lfilter(b, a, yArray, zi=zi*yArray[0])
    z2, _ = lfilter(b, a, z, zi=zi*z[0])
    yFiltered = filtfilt(b, a, yArray)
    
    return yFiltered

#Takes in two arrayes and finds all indices where one is in another
#Assumes each value in the bigArray is unique
def ValueFinder(guageArray,bigArray):
    num = len(guageArray)
    finalArrayInd = np.zeros(num)
    for i in range(len(guageArray)):
        guess = guageArray[i]
        point = np.where(guess == bigArray)[0][0]
        finalArrayInd[i] = int(point)
        
        
    finalArrayInd = finalArrayInd.astype(int)
    return finalArrayInd
        

path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('MultiDirPlotter.py')) + '\\Data'))

for i in range(len(dirs)):
    
    vars()['path'+dirs[i]], vars()['dirs'+dirs[i]], vars()['files'+dirs[i]] = next(os.walk(os.path.dirname(os.path.realpath('UV_Vis_plotter.py')) + '\\Data\\' + dirs[i]))


Val1, Val2 = 3, 0.035


suffix = ".txt"



# for i in range(len(files)):
#     files[i] = files[i][:-len(suffix)]  
    
#     vars()[files[i]] = np.loadtxt(open(path + "\\" + files[i] + ".txt", "rb"), delimiter=",",skiprows = 2).T
#     vars()[files[i]+'newY'] = NoiseFilter(Val1,Val2,vars()[files[i]][1])
    
    
    
    
#     plt.figure(i)
#     plt.plot(vars()[files[i]][0],vars()[files[i]][1],label = files[i])
#     plt.plot(vars()[files[i]][0],vars()[files[i]+'newY'],label = files[i]+' filtered')
#     Point = np.where(np.gradient(vars()[files[i]+'newY']) == max(np.gradient(vars()[files[i]+'newY'])))[0][0]
#     m,c,err = LineValFinder(vars()[files[i]][0],vars()[files[i]+'newY'],10)
#     yFit = m * vars()[files[i]][0] + c
#     Contstraint = (yFit >= 0) & (yFit <= max(vars()[files[i]+'newY']))
    
#     line1start = (min(vars()[files[i]][0]),0)
#     line1end = (max(vars()[files[i]][0]),0)    
    
#     line2start = (min(vars()[files[i]][0][Contstraint]),min(yFit[Contstraint]))
#     line2end = (max(vars()[files[i]][0][Contstraint]),max(yFit[Contstraint]))

#     vars()[files[i]+'Intercept'] = line_intersection((line1start,line1end),(line2start,line2end))    
    
#     # plt.plot(vars()[files[i]][0][Contstraint],yFit[Contstraint],label = 'Intercept = '+str(np.around(vars()[files[i]+'Intercept'][0],2)))
#     plt.xlabel('Wavelength (nm)')
#     plt.ylabel('Transmittance, E_bg =' + str(np.around(vars()[files[i]+'Intercept'][0],2)))
#     plt.title(files[i])
#     plt.legend()