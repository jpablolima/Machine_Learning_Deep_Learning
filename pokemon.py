#!/usr/bin/env python
# coding: utf-8

# In[129]:


import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Import DataSet

# In[130]:


df = pd.read_csv('pokemon.csv',index_col=0, header=0,encoding = 'unicode_escape')


# In[131]:


df.head()


# ### grafico de dispersão

# In[132]:


sns.lmplot(x = 'Attack', y="Defense", data=df)


# ### gráfico de dispersão

# In[133]:


sns.lmplot(x="Attack", y="Defense", data=df,
          fit_reg = False, #apada linha de regressão
          hue='Stage') #colorir a evelução


# ### plot Seaborn  

# In[134]:


sns.lmplot(x= "Attack", y="Defense", data=df,
          fit_reg = False,
          hue="Stage") 
          
    ### configuarções com Matplotlib
plt.ylim(0, None, )
plt.xlim(0, None,)


# In[135]:


### Box plot
sns.boxplot(data=df)


# ### Pré-formatar DataFrame - Pandas

# In[136]:


stats_df = df.drop(['Total', 'Stage','Legendary'], axis=1)
sns.boxplot(data = stats_df)


# ### Temas Seaborn

# ### Paleta de Cores

# In[137]:


sns.set_style('whitegrid')

## violino plot
sns.violinplot(x = "Type 1", y="Attack", data=df)


# In[138]:


pkmn_type_colors   =   [ '#78C850' ,    # Grass 
                     '#F08030' ,    # Fire 
                     '#6890F0' ,    # Water 
                     '#A8B820' ,    # Bug 
                     '#A8A878' ,    # Normal 
                     '#A040A0' ,    # Poison 
                     '#F8D030' ,    # Electric 
                     '#E0C068' ,    # Ground 
                     '#EE99AC' ,    # Fairy 
                     '#C03028' ,    # Fighting 
                     '#F85888' ,    # Psychic 
                     '#B8A038' ,    # Rock 
                     '#705898' ,    # Ghost 
                     '#98D8D8' ,    # Ice 
                     '#7038F8' ,    # Dragon 
                    ] 


# In[139]:


sns.violinplot(x= "Type 1", y='Attack', data=df,
             palette=pkmn_type_colors) ### seleçaõ de paletas de cores


# In[140]:


sns.swarmplot(x= "Type 1", y='Attack', data=df,
             palette=pkmn_type_colors) ### seleçaõ de paletas de cores


# In[141]:


# Set figure size with matplotlib 
plt . figure ( figsize = ( 10 , 6 ) ) 

# Create plot 
sns . violinplot ( x = 'Type 1' , 
               y = 'Attack' ,  
               data = df ,  
               inner = None ,   # Remove the bars inside the violins 
               palette = pkmn_type_colors ) 

sns . swarmplot ( x = 'Type 1' ,  
              y = 'Attack' ,  
              data = df ,  
              color = 'k' ,   # Make points black 
              alpha = 0.7 )   # and slightly transparent 

# Set title with matplotlib 
plt . title ( 'Attack by Type' ) 


# In[142]:


stats_df.head()


# In[143]:


### Derretar DataFrame - juntar colunas


# In[144]:


melted_df = pd.melt(stats_df,
                  id_vars  = ["Name", "Type 1", "Type 2"],
                  var_name = "Stat")
melted_df.head()


# In[145]:


print(stats_df.shape)
print(melted_df.shape)


# In[146]:


sns.swarmplot(x = 'Stat', y = 'value', data=melted_df,
             hue='Type 1')


# ## Ajuste do Gráfico

# In[151]:


plt.figure(figsize = (10, 6))
sns.swarmplot(x = 'Stat',
              y = 'value',
              data= melted_df,
             hue = 'Type 1',
             split = True, ## seperação dos pontos na Matriz
             palette = pkmn_type_colors) ## paleta de cores
plt.ylim(0,260) ## ajuste dos eixos
plt.legend(bbox_to_anchor = (1,1), loc=2) ## alinhamento a direita


# ### Mapa de Calor

# In[153]:


### correlaççao de Calor 
corr = stats_df.corr()
### mapa de calor
sns.heatmap(corr)


# # Histograma

# In[155]:


sns.distplot(df.Attack)


# In[ ]:




