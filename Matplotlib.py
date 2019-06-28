#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt


# In[25]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[26]:


import numpy as np


# In[27]:


x = np.linspace(0., 5, 11)


# In[28]:


x


# In[29]:


y = x * x


# In[30]:


y


# In[31]:


# Modelo Funcinal
plt.plot(x,y)


# In[33]:


plt.plot(x,y)
plt.show()


# In[34]:


plt.plot(x, y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo y')
plt.title('Grafico Matplotlib')


# In[40]:


plt.plot(x,y, color='r')
plt.xlabel('Eixo X')
plt.ylabel('Eixo y')
plt.title('Grafico Matplotlib')


# In[43]:


plt.plot(x,y, 'r--')
plt.xlabel('Eixo X')
plt.ylabel('Eixo y')
plt.title('Grafico Matplotlib')


# ## Criação de dois Gráficos

# In[47]:


plt.subplots(nrows=1, ncols=2)


# In[51]:


plt.subplot(1, 2, 1)
plt.plot(x, y, 'r--')
plt.subplot(1,2,2)
plt.plot(y,x,'g*-') ## gráfico tracejado 


# In[52]:


fig = plt.figure()


# In[63]:


fig = plt.figure()
axes1=fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2=fig.add_axes([0.2, 0.5, 0.3, 0.3])

axes1.plot(x, y)
axes1.set_xlabel('Eixo X')
axes1.set_title('Gráficos')
axes2.plot(y, x)


# In[ ]:




