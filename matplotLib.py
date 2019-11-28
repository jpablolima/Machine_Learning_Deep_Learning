# -*- coding: utf-8 -*-
# Visualizar Dados e gerar Gráficos  - MatplotLibf

#________ Importar para alterar a fonte padrão__________# 
from __future__ import unicode_literals
#_______________________________________________________#
from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.2]

# Criar um Gráfico de linha, anos eixo x , gpd no eixo y

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# Adicionar Título eixo X
plt.title("GDP Nominal")

# Adicionar Título eixo Y
plt.ylabel("Bilhões de $")
plt.show()