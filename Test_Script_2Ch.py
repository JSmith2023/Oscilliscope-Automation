#start: 0Hz
#stop: 200Mhz
#RBW: 100kHz


import pyvisa
import time
import matplotlib.pyplot as plt
rm = pyvisa.ResourceManager()
ID='TCPIP0::169.254.12.105::hislip0::INSTR'
scope=rm.open_resource(ID)
print(rm.list_resources())  
vRange= .008
tRange=10e-9
triglevel=0
ch=1
#scope.write('*rst')
scope.query('*opc?')
#scope.write(f'timebase:Range {tRange}')
#scope.write(f'channel1:range {vRange}')
#print(float(scope.query(f'channel{ch}:range?')))
#scope.write('trigger:mode edge')
#scope.write(f'trigger:level channel{ch}, {triglevel}')


#scope.write("function1:FFTMagnitude Channel1")
#scope.write("SYStem:Header OFF")
#print(scope.write("function1:Display?"))
#scope.write("function1:Display ON")
#input("set")

#scope.query("*opc?")
#print(scope.query("System:ERROR? string"))
#scope.write("function1:FFT:PEAK:STATE ON")
#print(scope.query("System:ERROR? string"))


#scope.write("function1:Display ON")
scope.write(f'waveform:source function1')
scope.write('waveform:format byte')
scope.write('run')
x_inc=float(scope.query('waveform:xincrement?'))
x_origin=float(scope.query('waveform:xorigin?'))
y_inc=float(scope.query('waveform:yincrement?'))
y_origin=float(scope.query('waveform:yorigin?'))
print("y_origin:", y_origin)
print("x_origin: ", x_origin)
print("y_increment:", y_inc)
print("x_increament: ", x_inc)
#scope.write("ACQuire:POINts 500")

run_time=int(input("input number of seconds to run the test"))
start_time=time.time()
while(int(time.time())<int(start_time)+run_time):                        
    measure_time=time.time()        #time at which measurement starts
    scope.write('digitize')         #stops and capture waveform
    scope.query('*opc?')
    measure_time=time.time() 
    data=scope.query_binary_values('waveform:data?', datatype='b') #data is list of signed 8-bit integers
    length=(len(data))
    wave_time=[]        #this is frequency for fft measuremnts
    wave_voltage=[]     #this is power measured in dBm for fft measurements
   
    for t in range(length):
        if((t*x_inc)+x_origin<150*(10**6)):        #stops writing data to list at 150MHz
            wave_time.append((t*x_inc)+x_origin)

    for v in data:
       wave_voltage.append((v*y_inc)+y_origin)
    
    #print(len(wave_time))
    slice_object = slice(len(wave_time))
    
    with open('function2.txt', 'a') as f:
        #print(len(data[slice_object]))
        for v in data[slice_object]:                      #[slice_object is optional data parameter to get a lower threshold set of points
            #f.write("%s\n" % v)
            f.write("%s " % v)
        f.write(str(measure_time-start_time))
        f.write("\n")

    scope.write(f'waveform:source function1')
    scope.write('digitize')         #stops and capture waveform
    data=scope.query_binary_values('waveform:data?', datatype='b') #data is list of signed 8-bit integers
    
    length=(len(data))
    wave_time=[]        #this is frequency for fft measuremnts
    wave_voltage=[]     #this is power measured in dBm for fft measurements
   
    for t in range(length):
        if((t*x_inc)+x_origin<150*(10**6)):        #stops writing data to list at 150MHz
            wave_time.append((t*x_inc)+x_origin)

    for v in data:
       wave_voltage.append((v*y_inc)+y_origin)
    
    slice_object = slice(len(wave_time))
    
    with open('function1.txt', 'a') as f:
        #print(len(data[slice_object]))
        for v in data[slice_object]:                      #[slice_object is optional data parameter to get a lower threshold set of points
            #f.write("%s\n" % v)
            f.write("%s " % v)
        f.write(str(measure_time-start_time))
        f.write("\n")


    scope.write(f'waveform:source function2')  
    scope.write('run')

    
    while(1):
        if(int(time.time())>measure_time+1):
            break

    #plt.plot(wave_time, wave_voltage[slice_object])
    #plt.show()
    print("time:", time.time()-start_time)
    #break  //break just to run once





