# -*- coding: utf-8 -*-
#________ Importar para alterar a fonte padrão__________# 
from __future__ import unicode_literals
#_______________________________________________________#


from matplotlib import pyplot as plt

variance = [1,2,4,8,16,32,64,128,256]
bias_squared=[256,128,64,32,16,8,4,2,1]
total_error=[x + y for x,y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# multiplas chamadas para plt.plot
#para mostrar mútiplas séries no mesmo gráfico
plt.plot(xs,variance, 'g-', label = 'variance') # linha verde sólida
plt.plot(xs, bias_squared, 'r-', label='bias^2') # linha com linha de ponto tracejado vermelho
plt.plot(xs, total_error, 'b:', label='total error') # linha com pontilhado azul

# rótulos para cada série
#obter legenda gratuita
#loc=9 siguinifica  "top center"
plt.legend(loc=9)
plt.xlabel("complexidade do modelo")
plt.title("Compromisso entre polaização e Variância")
plt.show()