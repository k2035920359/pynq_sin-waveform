
# coding: utf-8

# In[8]:


from pynq.overlays.base import BaseOverlay
from pynq.lib import Pmod_ADC, Pmod_DAC
base = BaseOverlay("base.bit")


# In[9]:


adc = Pmod_ADC(base.PMODA)
dac = Pmod_DAC(base.PMODB)


# In[10]:


from math import ceil
from time import sleep
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pynq.lib import Pmod_ADC, Pmod_DAC

delay = 0.0

output_volt = 1
input_v = 0
neg = 0 
input_vs= []
xdata,ydata=[],[]
data=[]
x = np.arange(-10*np.pi,10*np.pi,0.01)
error = 0

get_ipython().magic('matplotlib notebook')
fig, ax = plt.subplots()

for i in range(2 , 3 , 1):
    ln = ax.plot(x, (np.sin(x*output_volt*i)), 'r-', animated=False)
    ln1 = ax.plot(x, (np.sin(x*input_volt*i)), 'b-', animated=False)
    
    def init():
        ax.set_xlim(0, 2*np.pi,3)
        ax.set_ylim(-1.05, 2.05)
    
        ln.set_ydata([np.nan] * len(x))
        ln1.set_ydata([np.nan] * len(x))
        return ln1,
        return ln,

    for j in x:

        sample = np.sin(np.sin(i*output_volt*j)+1)  #sin waveform
        sleep(delay)                        
        dac.write(sample) #write to DAC
     
        
 
        input_v = adc.read()    #read sin waveform from ADC
        input_vs.append(input_v[0])
    
        print('Value written: {:4.2f}\tSample read: {:4.2f}'.
              format(sample, input_v[0]))
            
        def update(frame):
            ln.set_ydata(np.sin(i*x+(frame/2)))
            ln1.set_ydata(sample)
            ln1.set_xdata(x-(frame/2/i))
            return ln1,
            return ln,


    ani = FuncAnimation(fig, update,frames=np.linspace(0, 10*np.pi, 400),init_func=init, interval=2, blit=True, save_count=100) 
    fig.set_size_inches(6, 4)

    plt.show()
    


# In[ ]:





# In[ ]:





# In[ ]:




