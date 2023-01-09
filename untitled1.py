import numpy as np
import os
import matplotlib.pyplot as plt
import functions as F


path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('GlassCode.py')) + '\\OrDir'))

Val1, Val2 = 3, 0.035
h = 6.63e-34
c = 3e8
LamMax = 800

suffix = ".txt"



for i in range(len(files)):
    files[i] = files[i][:-len(suffix)]
    
    vars()[files[i]] = np.loadtxt(open(path + "\\" + files[i] + ".txt", "rb"), delimiter=",",skiprows = 2).T

    vars()[files[i]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[files[i]][1])


plt.figure(1)
for i in range(len(files)):
    plt.plot(vars()[files[i]][0],vars()[files[i]+'newY'],label = files[i])
plt.ylabel('Transmittance')
plt.title('I Transmittance')
plt.xlabel('Wavelength (nm)')
plt.legend()

    