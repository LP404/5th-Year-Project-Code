import numpy as np
import os
import matplotlib.pyplot as plt
import functions as F
from mpl_toolkits.axes_grid1.inset_locator import inset_axes




def add_subplot_axes(ax,rect,axisbg='w'):
    fig = plt.gcf()
    box = ax.get_position()
    width = box.width
    height = box.height
    inax_position  = ax.transAxes.transform(rect[0:2])
    transFigure = fig.transFigure.inverted()
    infig_position = transFigure.transform(inax_position)    
    x = infig_position[0]
    y = infig_position[1]
    width *= rect[2]
    height *= rect[3]  # <= Typo was here
    #subax = fig.add_axes([x,y,width,height],facecolor=facecolor)  # matplotlib 2.0+
    subax = fig.add_axes([x,y,width,height],axisbg=axisbg)
    x_labelsize = subax.get_xticklabels()[0].get_size()
    y_labelsize = subax.get_yticklabels()[0].get_size()
    x_labelsize *= rect[2]**0.5
    y_labelsize *= rect[3]**0.5
    subax.xaxis.set_tick_params(labelsize=x_labelsize)
    subax.yaxis.set_tick_params(labelsize=y_labelsize)
    return subax


suffix = ".txt"
Val1, Val2 = 3, 0.035
h = 6.63e-34
c = 3e8
LamMax = 800
LamMin = 400

# LamMax = 750
# LamMin = 575

path, dirs, files = next(os.walk(os.path.dirname(os.path.realpath('UV_Vis_plotter.py')) + '\\UV-Vis\\Transmittance\\Sample'))
path1, dirs1, files1 = next(os.walk(os.path.dirname(os.path.realpath('UV_Vis_plotter.py')) + '\\UV-Vis\\Transmittance\\Substrate'))
path2, dirs2, files2 = next(os.walk(os.path.dirname(os.path.realpath('UV_Vis_plotter.py')) + '\\UV-Vis\\Reflectance'))


for i in range(len(files1)):
    files1[i] = files1[i][:-len(suffix)] 
    
for i in range(len(files2)):    
    files2[i] = files2[i][:-len(suffix)]  

for i in range(len(files)):
    files[i] = files[i][:-len(suffix)]  

if len(files) == 4 : 
    SamName = ['A3','A4','A1','A2']
elif len(files) == 8:
    SamName = ['I','II','IX','V','VI','VII','VIII','X']
else:
    SamName = files

for i in range(len(files1)):
    
    temp = np.loadtxt(open(path1 + "\\" + files1[i] + ".txt", "rb"), delimiter=",",skiprows = 2).T
    Loc1 = np.where((temp[0] < LamMax) & (temp[0] > LamMin))[0]
    
    temp1 = np.array([temp[0][Loc1],temp[1][Loc1]])
    vars()[files1[i]] = temp1
    vars()[files1[i]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[files1[i]][1])
    
    
    # plt.figure(i+len(files)+1+len(files2))
    # plt.plot(vars()[files1[i]][0],vars()[files1[i]][1],label = files1[i])
    # plt.plot(vars()[files1[i]][0],vars()[files1[i]+'newY'],label = files1[i]+' filtered')

    # plt.xlabel('Wavelength (nm)')
    # plt.ylabel('Reflectance')    
    
    # plt.title(files1[i])
    # plt.legend()

for i in range(len(files2)):
    
    temp2 = np.loadtxt(open(path2 + "\\" + files2[i] + ".txt", "rb"), delimiter=",",skiprows = 2).T
    
    Loc2 = np.where((temp2[0] < LamMax) & (temp2[0] > LamMin))[0]
    temp3 = np.array([temp2[0][Loc2],temp2[1][Loc2]])
    
    vars()[files2[i]] = temp3
    
    vars()[files2[i]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[files2[i]][1])
    
    vars()[files2[i]+'newYNorm'] = vars()[files2[i]+'newY']/100
    
    # plt.figure(i+len(files)+1)
    # plt.plot(vars()[files2[i]][0],vars()[files2[i]][1],label = files2[i])
    # plt.plot(vars()[files2[i]][0],vars()[files2[i]+'newY'],label = files2[i]+' filtered')

    # plt.xlabel('Wavelength (nm)')
    # plt.ylabel('Reflectance')    
    
    # plt.title(SamName[i] + ' Reflectance')
    # plt.legend()
    
thickness = 4e-5
# thickness = 4e-5

for i in range(len(files)):
    
    temp4 = np.loadtxt(open(path + "\\" + files[i] + ".txt", "rb"), delimiter=",",skiprows = 2).T
    Loc3 = np.where((temp4[0] < LamMax) & (temp4[0] > LamMin))[0]
    temp5 = np.array([temp4[0][Loc3],temp4[1][Loc3]])
    vars()[files[i]] = temp5   
    vars()[files[i]+'newY'] = F.NoiseFilter(Val1,Val2,vars()[files[i]][1])
    
    
    # plt.figure(i)
    # plt.plot(vars()[files[i]][0],vars()[files[i]][1],label = files[i])
    # plt.plot(vars()[files[i]][0],vars()[files[i]+'newY'],label = files[i]+' filtered')
    # Point = np.where(np.gradient(vars()[files[i]+'newY']) == max(np.gradient(vars()[files[i]+'newY'])))[0][0]
   
    # m,c,err = F.LineValFinder(vars()[files[i]][0],vars()[files[i]+'newY'],10)
    # yFit = m * vars()[files[i]][0] + c
    # Contstraint = (yFit >= 0) & (yFit <= max(vars()[files[i]+'newY']))
    
    # line1start = (min(vars()[files[i]][0]),0)
    # line1end = (max(vars()[files[i]][0]),0)    
    
    # line2start = (min(vars()[files[i]][0][Contstraint]),min(yFit[Contstraint]))
    # line2end = (max(vars()[files[i]][0][Contstraint]),max(yFit[Contstraint]))

    # vars()[files[i]+'Intercept'] = F.LineIntersection((line1start,line1end),(line2start,line2end))    
    
    # plt.plot(vars()[files[i]][0][Contstraint],yFit[Contstraint],label = 'Intercept = '+str(np.around(vars()[files[i]+'Intercept'][0],2)))
    # plt.xlabel('Wavelength (nm)')
    # bgEn = (3e8 * 6.63e-34)/(vars()[files[i]][0][Point]*1e-9)
    # bgeV =  np.around((6.242e18 * bgEn),2)
    # plt.ylabel('Transmittance, E_bg =' + str(bgeV)+'eV')    
    
    # plt.ylabel('Transmittance, E_bg =' + str(np.around(vars()[files[i]+'Intercept'][0],2)))
    # plt.ylabel('Transmittance')
    # plt.title(SamName[i] + ' Transmittance')
    # plt.legend()
    
    vars()[files[i]+'_CorrectedTrans'] = vars()[files[i]+'newY']/vars()[files1[0]+'newY']
    
    plt.figure(100+i)
    plt.plot(vars()[files[i]][0],(vars()[files[i]+'_CorrectedTrans'])*100)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Transmittance') 
    plt.title(SamName[i]+' Transmittance')
    
    
    #hv is identical for all measuremnts 
    hv = ((h * c) / (vars()[files[0]][0] * 1e-9)) * 6.242e18
    # vars()[files[i]+' alpha'] = (np.log((1/vars()[files[i]+'_CorrectedTrans']))) / 7e-5
    
    vars()[files[i]+' alpha1'] = np.log( ( ((1- vars()[files2[i]+'newYNorm'])) / vars()[files[i]+'_CorrectedTrans']) ) / thickness
    
    # vars()[files[i]+' alpha2'] = np.log(( ((1- vars()[files2[i]+'newYNorm'])**2) / (2 * vars()[files[i]+'_CorrectedTrans'])) + np.sqrt( (( ((1- vars()[files[i]+'_CorrectedTrans'])**4) / (4 * vars()[files[i]+'_CorrectedTrans']**2)) + (vars()[files2[i]+'newYNorm']**2)) )) / 7e-5

    # vars()[files[i]+' kub'] = (1 - vars()[files2[i]+'newY'])**2 / (2 * vars()[files2[i]+'newY'])  






expval = 2

# for i in range(len(files)):
#     plt.figure(200 + i)
#     plt.plot(hv,vars()[files[i]+' alpha1'])
#     plt.legend()
#     plt.xlabel('hv (eV)')
#     plt.ylabel('α (cm^-1)')
#     plt.title(SamName[i] + " Absorbtion")

LamMaxBg = 688
LamMinBg = 575

hvMin = ((h * c) / (LamMaxBg * 1e-9)) * 6.242e18
hvMax = ((h * c) / (LamMinBg * 1e-9)) * 6.242e18

# path3, dirs3, files3 = next(os.walk(os.path.dirname(os.path.realpath('UV_Vis_plotter.py')) + '\\UVVisLineDir\\Ivy'))

# for i in range(len(files3)): 
#     files3[i] = files3[i][:-len(suffix)] 
#     vars()[files3[i]] = np.loadtxt(open(path3 + "\\" + files3[i] + '.txt', "rb"), delimiter=",")


for i in range(len(files)):
    vars()[files[i]+'FinalY'] = (hv*vars()[files[i]+' alpha1'])**expval
    


for i in range(len(files)):
    plt.figure(300 + i)
    plt.xlim([1.4,3.1])
    plt.xticks(np.arange(1.4,3.2,0.1))
    plt.rc('xtick', labelsize=8)
 
    Point = np.where(np.gradient(vars()[files[i]+'FinalY']) == min(np.gradient(vars()[files[i]+'FinalY'])))[0][0]
    
    m,c,err = F.LineValFinder(hv,vars()[files[i]+'FinalY'],10,'bg',hvMin,hvMax)
    yFit = m * hv + c
    Contstraint = (yFit >= 0) & (yFit <= max(vars()[files[i]+'FinalY']))
    
    line1start = (min(hv),0)
    line1end = (max(hv),0)    
    
    line2start = (min(hv[Contstraint]),min(yFit[Contstraint]))
    line2end = (max(hv[Contstraint]),max(yFit[Contstraint]))

    vars()[files[i]+'Intercept'] = F.LineIntersection((line1start,line1end),(line2start,line2end))   
    
    vars()[files[i]+'hvConst'] = hv[Contstraint]
    vars()[files[i]+'yFitConst'] = yFit[Contstraint]
    

    plt.plot(hv[Contstraint],yFit[Contstraint],label = 'Intercept = '+str(np.around(vars()[files[i]+'Intercept'][0],2)))
    plt.ylabel('Transmittance, E_bg =' + str(vars()[files[i]+'Intercept'])+'eV')        
  
    vars()[files[i]+'hvCOnt'] = hv[Contstraint]
    vars()[files[i]+'YfitCon'] = yFit[Contstraint]
  
    
    plt.plot(hv,vars()[files[i]+'FinalY'])
    # plt.plot(vars()[files3[i]][0],vars()[files3[i]][1])
    plt.scatter(hv[Point],vars()[files[i]+'FinalY'][Point])
    plt.xlabel('hv (eV)')
    plt.ylabel('αhv^2 (cm^-1 eV)^2')
    plt.xlim(max(hv),min(hv))
    plt.title(SamName[i] + ' Absorbtion Squared')
    plt.legend()
    plt.plot()

    np.savetxt(str(SamName[i])+'_Linedata.txt',(hv[Contstraint],yFit[Contstraint]), delimiter=',')   

if len(files) == 4 : 
    path3, dirs3, files3 = next(os.walk(os.path.dirname(os.path.realpath('UV_Vis_plotter.py')) + '\\UVVisLineDir\\Huimin'))
 
    for i in range(len(files3)): 
        files3[i] = files3[i][:-len(suffix)] 
        vars()[files3[i]] = np.loadtxt(open(path3 + "\\" + files3[i] + '.txt', "rb"),delimiter = ',')
        
        
    

    for i in range(len(files)):
        
        fig,ax1 = plt.subplots()
        left, bottom,width,height = [0.55,0.2,0.3,0.3]
        ax2 = fig.add_axes([left, bottom,width,height])
        ax1.plot(hv,vars()[files[i]+' alpha1'])
        ax2.plot(hv,vars()[files[i]+'FinalY'])
        ax2.plot(vars()[files3[i]][0],vars()[files3[i]][1])
        ax1.set_xlabel('hv (eV)')
        ax1.set_ylabel('α (cm^-1)')
        ax1.set_title(SamName[i] + ' Absorbtion')
        ax2.set_title('Absorbtion squared', fontsize = 7)
        ax2.set_ylabel('αhv^2 (cm^-1 eV)^2',fontsize = 7)



elif len(files) == 8:
    path3, dirs3, files3 = next(os.walk(os.path.dirname(os.path.realpath('UV_Vis_plotter.py')) + '\\UVVisLineDir\\Ivy'))

    for i in range(len(files3)): 
        files3[i] = files3[i][:-len(suffix)] 
        vars()[files3[i]] = np.loadtxt(open(path3 + "\\" + files3[i] + '.txt', "rb"),delimiter = ',')


    for i in range(len(files)):

        
        fig,ax1 = plt.subplots()
        left, bottom,width,height = [0.55,0.2,0.3,0.3]
        ax2 = fig.add_axes([left, bottom,width,height])
        ax1.plot(hv,vars()[files[i]+' alpha1'])
        ax2.plot(hv,vars()[files[i]+'FinalY'])
        ax2.plot(vars()[files3[i]][0],vars()[files3[i]][1])
        ax1.set_xlabel('hv (eV)')
        ax1.set_ylabel('α (cm^-1)')
        ax1.set_title(SamName[i] + ' Absorbtion')
        ax2.set_title('Absorbtion squared', fontsize = 7)
        ax2.set_ylabel('αhv^2 (cm^-1 eV)^2',fontsize = 7)



else:
    for i in range(len(files)):
        fig,ax1 = plt.subplots()
        left, bottom,width,height = [0.55,0.2,0.3,0.3]
        ax2 = fig.add_axes([left, bottom,width,height])
        ax1.plot(hv,vars()[files[i]+' alpha1'])
        ax2.plot(hv,vars()[files[i]+'FinalY'])
        ax1.set_xlabel('hv (eV)')
        ax1.set_ylabel('α (cm^-1)')
        ax1.set_title(SamName[i] + ' Absorbtion')
        ax2.set_title('Absorbtion squared', fontsize = 7)
        ax2.set_ylabel('αhv^2 (cm^-1 eV)^2',fontsize = 7)

    # plt.plot(vars()[files[i]+'hvConst'],vars()[files[i]+'yFitConst'],label = 'Intercept = '+str(np.around(vars()[files[i]+'Intercept'][0],2)))
    # plt.ylabel('Transmittance, E_bg =' + str(vars()[files[i]+'Intercept'])+'eV')        
 
    
 
    # plt.plot(hv,vars()[files[i]+'FinalY'])
    # plt.scatter(hv[Point],vars()[files[i]+'FinalY'][Point])
    # plt.xlabel('hv (eV)')
    # plt.ylabel('αhv^2 (cm^-1 eV)^2')
    # plt.xlim(max(hv),min(hv))
    # plt.title(SamName[i] + ' Absorbtion Squared')
    # plt.legend()
    # plt.plot()

    #np.savetxt(str(SamName[i])+'_MCErrLinedata.txt',(m,c,err), delimiter=',')   

for i in range(len(files)):
    fig,ax1 = plt.subplots()
    left, bottom,width,height = [0.5,0.2,0.35,0.35]
    ax2 = fig.add_axes([left, bottom,width,height])
    ax1.semilogy(hv,vars()[files[i]+' alpha1'])
    ax2.plot(hv,vars()[files[i]+'FinalY'])
    ax2.plot(vars()[files[i]+'hvConst'],vars()[files[i]+'yFitConst'], label = 'Ebg = '+str(np.around(vars()[files[i]+'Intercept'][0],2))+'eV')
    ax1.set_xlabel('hv (eV)')
    ax1.set_ylabel('α (cm^-1)')
    ax2.set_title('Tauc plot', fontsize = 8)
    ax2.set_xlim(1.8,2.2)
    ax2.set_ylim(0,vars()[files[i]+'yFitConst'][np.where(np.around(vars()[files[i]+'hvConst'],2) == 2.2)[0][0]])
    ax2.set_ylabel('αhv^2 (cm^-1 eV)^2',fontsize = 8)
    ax2.legend(fontsize = 8)
    plt.rc('axes', labelsize=12) 
    plt.rc('xtick', labelsize=12)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=12)    # fontsize of the tick labels
    plt.savefig(files[i]+"myimg.svg",bbox_inches="tight")


    
# for i in range(len(files)):
#     plt.figure(400 + i)
#     plt.xlim([1.4,2.2])
#     plt.xticks(np.arange(1.4,2.25,0.05))
#     plt.rc('xtick', labelsize=8)
#     vars()[files[i]+'FinalY'] = (hv*vars()[files[i]+' alpha1'])**expval
#     plt.semilogy(hv,vars()[files[i]+'FinalY'],label = '1')
#     # Max = np.where(np.gradient(vars()[files[i]+'FinalY']) == max(np.gradient(vars()[files[i]+'FinalY'])))[0][0]   
#     # plt.scatter(hv[Max],vars()[files[i]+'FinalY'][Max])
#     plt.xlabel('hv (eV)')
#     plt.ylabel('αhv^2 (cm^-1 eV)^2')
#     plt.title(files[i]+' zoom')
#     plt.plot()    
    
# for i in range(len(files)):
#     plt.figure(500 + i)
#     plt.xlim([1.42,1.9])
#     plt.xticks(np.arange(1.42,1.92,0.02))
#     plt.rc('xtick', labelsize=4)
#     vars()[files[i]+'FinalY'] = (hv*vars()[files[i]+' alpha1'])**expval
#     plt.semilogy(hv,vars()[files[i]+'FinalY'],label = '1')
#     # Max = np.where(np.gradient(vars()[files[i]+'FinalY']) == max(np.gradient(vars()[files[i]+'FinalY'])))[0][0]   
#     # plt.scatter(hv[Max],vars()[files[i]+'FinalY'][Max])
#     plt.xlabel('hv (eV)')
#     plt.ylabel('αhv^2 (cm^-1 eV)^2')
#     plt.title(files[i]+' zoom 2')
#     plt.plot()    