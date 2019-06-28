#!/usr/bin/env python
# coding: utf-8

#  ## importação dos modulos

# In[36]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np


# In[52]:


testes = [['TV','radio','newspaper'],['radio','newspaper'],['TV','newspaper'], ['TV','radio']]
vencedor = {'teste' : '', 'performance': None}
primeira_passagem = True
publi = pd.read_csv('E:\\vm\\iris_dataset\\Advertising.csv', index_col=0)


# In[64]:


for teste in testes:
    x = publi[teste]
    y = publi['sales']
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.30,random_state=5)
    reglin = LinearRegression()
    reglin.fit(x_train, y_train)
    y_prev = reglin.predict(x_test)
    rmse = np.sqrt(metrics.mean_squared_error(y_test,y_prev))
    print('Teste:')
    print(teste)
    print('Performance: ')
    print(rmse)
    print('------------------')
    if(primeira_passagem):
        vencedor['teste'] = teste
        vencedor['performance'] = rmse
        primeira_passagem = False
    else:
        if (rmse < vencendor['performace']):
        vencedor['teste'] = teste
        vencedor['performance'] = rmse
        
print('------------------')
print('Vencedor:')
print(Vencedor['teste'])
print('Performance do Vencendor:')
print(vencedor['performance'])


# In[ ]:





# In[ ]:




