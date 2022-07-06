import matplotlib.pyplot as plt

y_origin=-78.6279          ##This parameters are only accurate based on the setting of the oscilliscope (preset#10 saved in setups)
x_origin=0.0
y_inc=0.812698
x_inc=4768.37158203125


time=[]
ROC=[]
with open('function2.txt', 'r') as f:
    for line in f:
        max_freq=0       #max_freq is the INDEX at which the peak frequency of the ROC is
        freq=[]
        pwr=[]
        data=line.split(' ')
        length=len(data)-1
        time.append(data.pop(length))
        for i in range(length):
            freq.append(float(i)*x_inc+x_origin)
            pwr.append(float(data[i])*y_inc+y_origin)
            if(pwr[i]>pwr[max_freq] and freq[i]<=98*(10**6)):
                max_freq=i
        ROC.append(freq[max_freq])
        #print(time[len(time)-1])
        if(len(time)==1319):
            plt.plot(freq,pwr)
            plt.show()
            input()
            



plt.plot(time,ROC)
plt.xticks(np.arange(range(x), 1.0))
plt.show()
        

    


        
        
        
        
        
        
