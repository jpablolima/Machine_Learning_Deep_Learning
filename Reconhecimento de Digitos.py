#!/usr/bin/env python
# coding: utf-8

# In[81]:


import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

get_ipython().run_line_magic('matplotlib', 'inline')
digits = datasets.load_digits()


# In[82]:


print(digits.data.shape)
print(digits.target.shape)


# In[83]:


print(digits.images[128])


# In[84]:


plt.Figure(figsize=(2,2))
plt.imshow(digits.images[128],cmap=plt.cm.gray_r)


# ## Suport vertor machine - SVN

# In[85]:


from sklearn.model_selection import train_test_split
x = digits.data
y = digits.target
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20, random_state=5)


# In[86]:


classifire = svm.SVC()
classifire.fit(x, y)


# ## Leitura de Imagem de digito - Array

# In[98]:


img = mpimg.imread('number.png')


# In[99]:


def rgb2gray(rgb):
    img_array = np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
    img_array = (16 - (img_array * 16)).astype(int)
    img_array = img_array.flatten()
    # print(type(img_array))
    # print(img_array)
     # print(img_array.shape, 'quantidade de elementos')
    return img_array
previsao = classifire.predict([rgb2gray(img)])
print(previsao)
    
# rgb2gray(img)


# ##  Regressão Logistica

# In[100]:


# Calculo de Previsão
logreg = LogisticRegression()
logreg.fit(x_train,y_train)
previsoes_logreg = logreg.predict(x_test)
acertos_logreg = metrics.accuracy_score(y_test,previsoes_logreg)
#previsao_logred = logred.predict([rgb2gray(img)])
print(acertos_logreg)


# In[101]:


logreg = LogisticRegression()
logreg.fit(x,y)
previsao_logreg = logred.predict([rgb2gray(img)])
print(previsao_logreg)


# In[ ]:




