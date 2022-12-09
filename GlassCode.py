import numpy as np
import os
import matplotlib.pyplot as plt
import functions as F


path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('GlassCode.py')) + '\\GlassDir\\Pre\\Transmittance'))
path3, dirs3, files3 = next(os.walk(os.path.dirname(os.path.realpath('GlassCode.py')) + '\\GlassDir\\Post\\Transmittance'))

path2, dirs2, files2 = next(os.walk(os.path.dirname(os.path.realpath('GlassCode.py')) + '\\GlassDir\\Pre\\Reflectance'))
path1, dirs1, files1 = next(os.walk(os.path.dirname(os.path.realpath('GlassCode.py')) + '\\GlassDir\\Post\\Reflectance'))

Val1, Val2 = 3, 0.035
h = 6.63e-34
c = 3e8
LamMax = 800

suffix = ".txt"

samName = ['C3','C4','C1','C2']


for i in range(len(files2)):
    files1[i] = files1[i][:-len(suffix)]  
    files2[i] = files2[i][:-len(suffix)]  
    
    
    vars()[files1[i]] = np.loadtxt(open(path1 + "\\" + files1[i] + ".txt", "rb"), delimiter=",",skiprows = 2).T
    vars()[files2[i]] = np.loadtxt(open(path2 + "\\" + files2[i] + ".txt", "rb"), delimiter=",",skiprows = 2).T
        
    vars()[files1[i]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[files1[i]][1])
    vars()[files2[i]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[files2[i]][1])
        
    plt.figure(i+len(files)+1)
    
 #   plt.plot(vars()[files2[i]][0],vars()[files2[i]][1],label = files2[i])
    plt.plot(vars()[files2[i]][0],vars()[files2[i]+'newY'],label = samName[i]+' filtered')
    
    
#    plt.plot(vars()[files1[i]][0],vars()[files1[i]][1],label = 'Post Exposure ' + files2[i])
    plt.plot(vars()[files1[i]][0],vars()[files1[i]+'newY'],label = 'Post Exposure ' + samName[i]+' filtered')
    

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Reflectance')    
    
    plt.title(samName[i] + ' Reflectance')
    plt.legend()
    
    plt.figure(i+len(files)+100)

    delta = vars()[files1[i]][1] - vars()[files2[i]][1]

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Change in Reflectance')    
    
    plt.plot(vars()[files2[i]][0],delta,label = files2[i])
    
    
    plt.title(files2[i]+ ' Delta')
    plt.legend()
    

for i in range(len(files)):
    files[i] = files[i][:-len(suffix)]
    files3[i] = files3[i][:-len(suffix)]  
    
    vars()[files[i]] = np.loadtxt(open(path + "\\" + files[i] + ".txt", "rb"), delimiter=",",skiprows = 2).T
    vars()[files3[i]] = np.loadtxt(open(path3 + "\\" + files3[i] + ".txt", "rb"), delimiter=",",skiprows = 2).T

    vars()[files[i]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[files[i]][1])
    vars()[files3[i]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[files3[i]][1])
    
    
    plt.figure(i)
#    plt.plot(vars()[files[i]][0],vars()[files[i]][1],label = files[i])
    plt.plot(vars()[files[i]][0],vars()[files[i]+'newY'],label = samName[i]+' filtered')

#    plt.plot(vars()[files3[i]][0],vars()[files3[i]][1],label = 'Post Exposure ' +  files[i])
    plt.plot(vars()[files3[i]][0],vars()[files3[i]+'newY'],label = 'Post Exposure ' +  samName[i]+' filtered')

    plt.ylabel('Transmittance')
    plt.title(samName[i] + ' Transmittance')
    plt.legend()
    