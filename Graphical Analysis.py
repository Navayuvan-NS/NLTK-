
# coding: utf-8

# # Importing Matplotlib for graphical plotting 

# In[54]:

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time


# # Creatring Instances 

# In[55]:


style.use("ggplot")
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


# In[58]:


def animate(i):
    pulldata = open("twitter-out.txt", "r").read()
    lines = pulldata.split('\n') 
    
    xar = []
    yar = []
    
    x = 0
    y = 0
    
    for l in lines:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg"  in l:
            y -= 1
        
        xar.append(x)
        yar.append(y)
        
    
    ax1.clear()
    ax1.plot(xar, yar)


# In[59]:


ani = animation.FuncAnimation(fig, animate, interval = 100)
plt.show()

