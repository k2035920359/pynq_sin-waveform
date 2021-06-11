
# coding: utf-8

# In[19]:


from pynq.overlays.base import BaseOverlay
from pynq.lib import Pmod_ADC, Pmod_DAC
base = BaseOverlay("base.bit")

adc = Pmod_ADC(base.PMODA)
dac = Pmod_DAC(base.PMODB)

from math import ceil
from time import sleep
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# In[22]:


delay = 0.0

y=[]

for value in y:
    dac.write(value)
    sleep(delay)
    input_volt = adc.read()
    samples.append(input_volt[0])
    print('Value written: {:4.2f}\tSample read: {:4.2f}\tError: {:+4.4f}'.
          format(value, input_volt[0], input_volt[0]-value))


#write sinwave
s_rate = 44100
T = 1/s_rate
t=.1
N=s_rate*t

freq=100
omega=2*np.pi*freq

t_seq=np.arange(N)*T

y=np.sin(omega*t_seq)


error = 0

get_ipython().magic('matplotlib notebook')

plt.plot(t_seq,y)

plt.plot(t_seq,samples)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




