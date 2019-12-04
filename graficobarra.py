# -*- coding: utf-8 -*-
# Visualizar Dados e gerar Gráficos  - MatplotLibf
# Gráfico de Barra

#________ Importar para alterar a fonte padrão__________# 
from __future__ import unicode_literals
#_______________________________________________________#

from matplotlib import pyplot as plt

movies = ["Senhor dos Aneis","Poderoso Chefão","Ben-Hur","O Último Imperador"]
num_oscars = [17, 3, 11,9]
#  Tamanho das Barras - Padrão 0.8 ,0.1

xs = [i + 0.1 for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars)

plt.ylabel("# Prremiações")
plt.title("Filmes")

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()