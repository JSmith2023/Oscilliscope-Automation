import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from matplotlib.pyplot import figure
import numpy as np


data_x=[]
data_y=[]

interval=1000
    

with open('ROC.txt', 'r') as f:
    data=f.read()
    ROC=data.split(" ")
    temp=[]
    index=0
    for i in ROC:                   
        temp.append(i)
        index+=1
        if(index==len(ROC)):             #break at last element since it is just whitespace
            break
        if(len(temp)==interval):
            avg=0
            for n in temp:
                    avg=avg+float(n)
            avg=avg/len(temp) 
            data_y.append(avg*1e-6)
            temp.clear()



with open('time.txt', 'r') as f:
    data=f.read()
    time=data.split(" ")
    j=1
    temp=[]
    index=0
    for i in time:
        temp.append(i)
        index+=1
        if(index==len(ROC)):            #break at last element since it is just whitespace
            break       
        if(len(temp)==interval):       
            avg=0
            for n in temp:
                avg=avg+float(n)
            avg=avg/len(temp)
            data_x.append(avg)
            temp.clear()
            

ticks =[]
label=[]
for i in range(9):      #ticks every hour on x-axis
    ticks.append(i*3600)
    label.append(i);
    
    
        

fig=plt.figure(figsize=(15,10))      #11, 5
plt.plot(data_x, data_y, linewidth=1)
plt.xticks(ticks, label, rotation='horizontal', fontsize = 16)
plt.xlabel('Time (Hours)', fontsize= 16)
plt.ylabel('Ring Oscillator Frequency (MHz)', fontsize = 16)
plt.yticks(fontsize=16)


plt.xticks()
#plt.xticks(np.arange(0,10,15*(10**4)),np.arange(0,1000,15*(10**4)))  # Set text labels.
#plt.axvline(x=3600*4, color = 'b', label = 'axvline - full height')
plt.show()
