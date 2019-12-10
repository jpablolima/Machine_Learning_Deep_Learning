# -*- coding: utf-8 -*-
#________ Importar para alterar a fonte padrão__________# 
from __future__ import unicode_literals
#_______________________________________________________#

from matplotlib import pyplot as plt
from collections import Counter
num_friends = [100,49,41,40,25,75,60,6,70,61,
11,91,24,92,87,	
40,7,42,52,100,	
59,68,93,4,2,	
20,3,84,66,81,	
61,26,33,23,77,	
84,13,38,23,22,	
73,33,87,7,76,
45,78,70,91,55,	
25,76,67,92,52]

friend_counts = Counter(num_friends)
xs = range(101) # valor maior é 100
ys = [friend_counts[x] for x in xs] # altura é somente # amigos

num_points=len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)
sorted_values = sorted(num_friends)
smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]


plt.bar(xs,ys)
plt.axis([0,101,0,25])
plt.title("Histograma da Contagem de Amigos")
plt.xlabel("# de amigos")
plt.ylabel("# de pessoas")
plt.show()



