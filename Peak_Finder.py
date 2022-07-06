import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from matplotlib.pyplot import figure
import numpy as np



y_origin=-78.6279          ##This parameters are only accurate based on the setting of the oscilliscope (preset#10 saved in setups)
x_origin=0.0
y_inc=0.812698
x_inc=4768.37158203125

time=[]
ROC=[]



input("stop")

with open('function2.txt', 'r') as f:
    for line in f:
        #max_freq=0                                     #max_freq is the INDEX at which the peak frequency of the ROC is
        freq=[]
        pwr=[]
        data=line.split(' ')
        length=len(data)-1
        time.append(data.pop(length))
        for i in range(length):
            freq.append(float(i)*x_inc+x_origin)
            pwr.append(float(data[i])*y_inc+y_origin)
        ROC_peak=0                                      #ROC_peak is the INDEX at which the peak frequency of the ROC is
        peak_width=150
        #print(freq[0])
        while(1):
            peaks=find_peaks(pwr, width=peak_width, distance=200)       #distance= 0.95 MHz
            try:
                ROC_peak=peaks[0][0]
            except:
                "nothing to do here"
            
            for i in peaks[0]:
                if(abs(freq[ROC_peak]-94*(10**6))>abs(freq[i]-94*(10**6))):
                        ROC_peak=i
            if(freq[ROC_peak]>95*(10**6) or freq[ROC_peak]<93*(10**6)):
                peak_width-=5
            elif(peak_width<0):
               print("error: peak width 0 at: ", time[len(time)-1])
               input("continue?")
               break
            else:
               break
            
        
        if(freq[ROC_peak]>95*(10**6) or freq[ROC_peak]<93*(10**6) or True):                 #just some error checking
            print("error: peak out of expected range at: ", time[len(time)-1])
            print("peak calculated at",  freq[ROC_peak], "Hz")
            print("index: ", ROC_peak)
            print("width: ", peak_width)
            peaks=find_peaks(pwr, width=peak_width, distance=200)
            for i in peaks[0]:
                print(freq[i])
            plt.plot(freq, pwr)
            plt.axvline(x = freq[i], color = 'b', label = 'axvline - full height')
            plt.show()
            input("continue")

            
        ROC.append(freq[ROC_peak])
        
            
   
        

print("done")

def app():

    with open('ROC.txt', 'a') as f:
        for i in ROC:                      
            f.write("%s " % i)


    with open('time.txt', 'a') as f:
        for i in time:                      
            f.write("%s " % i)

      
    

plt.plot(time,ROC, linewidth=.1)
plt.xticks
plt.show()
        

    


        
        
        
        
        
        
