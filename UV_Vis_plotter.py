import numpy as np
import os
import matplotlib.pyplot as plt


path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('UV_Vis_plotter.py')) + '\\Data'))

suffix = ".txt"
for i in range(len(files)):
    files[i] = files[i][:-len(suffix)]  
    
    vars()[files[i]] = np.loadtxt(open(path + "\\" + files[i] + ".txt", "rb"), delimiter=",",skiprows = 2).T
    
    plt.figure(i)
    plt.plot(vars()[files[i]][0],vars()[files[i]][1])
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Transmittance')
    plt.title(files[i])