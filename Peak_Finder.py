import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from matplotlib.pyplot import figure
import numpy as np



y_origin= -58.6279
x_origin=  0.0
y_inc= 0.812698
x_inc=  15258.7890625


cuton_freq = 130*10**6
cutoff_freq = 160*10**6

time=[]
ROC=[]

input("Continue")

with open('C:/Users/muhaa/OneDrive/Desktop/Test_Env/function2.txt', 'r') as f:
    for line in f:

        freq=[]
        pwr=[]
        data=line.split(' ')
        length=len(data)-1
        time.append(data.pop(length))
        for i in range(length):
            freq.append(float(i)*x_inc+x_origin)
            pwr.append(float(data[i])*y_inc+y_origin)
     
        peaks=find_peaks(pwr)[0]
        ROC_peak = None
      
        for i in peaks:
            print(freq[i])
            if(freq[i]<cutoff_freq and freq[i]> cuton_freq):
                print("Valid peak at: ", freq[i])
                if(ROC_peak == None or pwr[i]>pwr[ROC_peak]):
                    print("peak_found at: ", freq[i])
                    ROC_peak=i
                   
        if(ROC_peak == None):
            print("Error, no valid peak within range found")
        
        elif(freq[ROC_peak]>cutoff_freq or freq[ROC_peak]<cuton_freq):                 #just some error checking
            print("error: peak out of expected range at: ", time[len(time)-1], "seconds")
            print("peak calculated at",  freq[ROC_peak], "Hz")
            peaks=find_peaks(pwr)[0]
            plt.plot(freq, pwr)
            plt.axvline(x = freq[ROC_peak], color = "red", label = 'axvline - full height')
            plt.ylabel("dBm")
            plt.xlabel("Frequency")
            plt.show()
   

            
        ROC.append(freq[ROC_peak])
        
          
input("Done: press enter to save data")

with open('C:/Users/muhaa/OneDrive/Desktop/Test_Env/ROC.txt', 'a') as f:
    for i in ROC:                      
        f.write("%s " % i)
    print("data saved to ROC")


with open('C:/Users/muhaa/OneDrive/Desktop/Test_Env/time.txt','a') as f:
    for i in time:                      
        f.write("%s " % i)
    print("data saved to ROC")

      
    
plt.plot(time,ROC, linewidth=.1)            #plots ROC frequency vs time. Ensure that it looks correct
plt.xticks
plt.show()
        

    


        
        
        
        
        
        

