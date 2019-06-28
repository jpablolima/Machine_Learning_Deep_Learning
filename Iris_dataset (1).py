#!/usr/bin/env python
# coding: utf-8

# # iris dataset

# ### Importação de dados

# In[1]:


from sklearn.datasets import load_iris
iris = load_iris()


# ### observações

# In[2]:


x = iris.data
print(x)


# ## target resultado

# In[3]:


y = iris.target
print(y)


# ### target - especies

# In[4]:


print(iris.target_names)


# ### shape das obeservações

# In[5]:


print(iris.data.shape)


# ### shape do target

# In[6]:


print(iris.target.shape)


# ### importação KNN

# In[7]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)


# ### trienar maquina

# In[8]:


knn.fit(x,y)


# ### fazer previsões 

# In[9]:


species = knn.predict([[5.9,3,5.1,1.8]])[0]
print(iris.target_names[species])


# ### separar os dados em dois grupos

# In[10]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)


# ### performance do modelo

# In[11]:


knn.fit(x_train, y_train)
previsoes = knn.predict(x_test)
print(previsoes)


# In[12]:


from sklearn import metrics
acertos = metrics.accuracy_score(y_test, previsoes)
print(acertos)


# # Regressão logistica

# In[13]:


from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(x_train, y_train)
print(logreg.predict([[6.2,3.4,5.4,2.3]]))


# ### Probabilidade das especies

# In[14]:


from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(x_train, y_train)
print(logreg.predict_proba([[6.2,3.4,5.4,2.3]]))


# ### Previsões e Performace

# In[15]:


from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(x_train, y_train)
previsoes_logreg = logreg.predict(x_test)
acertos_logreg = metrics.accuracy_score(y_test, previsoes_logreg)
print(acertos_logreg)


# In[ ]:




