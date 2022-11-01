import numpy as np
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter
from scipy import stats


def LineValFinder(xArray,yArray,guage):
    

    point = np.where(np.gradient(yArray) == max(np.gradient(yArray)))[0][0]
    xSec = xArray[point - guage : point + guage]
    ySec = yArray[point - guage : point + guage] 
     
     
    m,c,r,p,err = stats.linregress(xSec,ySec)
    
    
     
    return m,c,err

def LineIntersection(line1, line2):
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