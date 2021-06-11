
# coding: utf-8

# In[1]:


from pynq.overlays.base import BaseOverlay
from pynq.lib import Pmod_ADC, Pmod_DAC
base = BaseOverlay("base.bit")


# In[2]:


adc = Pmod_ADC(base.PMODA)
dac = Pmod_DAC(base.PMODB)


# In[3]:


#dac.write(0.35)
#sample = adc.read()
#print(sample)


# In[4]:


from math import ceil
from time import sleep
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pynq.lib import Pmod_ADC, Pmod_DAC

#adc = Pmod_ADC(1)
#dac = Pmod_DAC(2)
delay = 0.0
input_volt = adc.read()
input_volt = 1
neg = 0 
samples = []
x = np.arange(0,10*np.pi,0.01)
error = 0

get_ipython().magic('matplotlib notebook')
fig, ax = plt.subplots()

xdata, ydata = [], []

data=[]

for i in range(2 , 3 , 1):
    
#     print(i) 
    ln, = ax.plot(x, abs(np.sin(x*input_volt*i)), 'r-', animated=False)
    ln1, = ax.plot(x, abs(np.sin(x*input_volt*i)), 'b-', animated=False)
    
    def init():
        ax.set_xlim(0, 2*np.pi,3)
        ax.set_ylim(-1.05, 2.05)
        ln.set_ydata([np.nan] * len(x))
        ln1.set_ydata([np.nan] * len(x))
        return ln1,
        return ln,

    for j in x:
#         data.append(np.sin(i*input_volt*j))
        dac.write(np.sin(i*input_volt*j)+1)
        sleep(delay)
        sample = dac.write(np.sin(i*input_volt*j)+1)
#         sample=dac.write(1)
        print(sample)
#         //sample = [none][none][none]...[none]
#         samples.append(sample[0])
#         print('Value written: {:4.2f}\t{:4.2f}\tSample read: {:4.2f}\tError: {:+4.4f}'.
#               format(value, np.sin(i*value*j), sample[0], abs(sample[0])-np.sin(i*value*j)))
#         k = abs(np.sin(i*input_volt*j))-abs(sample[0])
#         if(error < abs(k)):
#             error = abs(k)
            
        def update(frame):
            ln.set_ydata(np.sin(i*x+(frame/2)))
            ln1.set_ydata(sample)
            ln1.set_xdata(x-(frame/2/i))
            return ln1,
            return ln,

#     samples = []
#     print(error)
#     print('it spends ',t_end-t_start ,'sec')
    ani = FuncAnimation(fig, update,frames=np.linspace(0, 10*np.pi, 400),init_func=init, interval=2, blit=True, save_count=100) 
    fig.set_size_inches(6, 4)
#     ani.save("/home/xilinx/jupyter_notebooks/data/fig1.gif",'pillow','GIF')
    plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




