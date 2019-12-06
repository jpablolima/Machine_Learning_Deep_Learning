# -*- coding: utf-8 -*-
#________ Importar para alterar a fonte padrão__________# 
from __future__ import unicode_literals
#_______________________________________________________#
from matplotlib import pyplot as plt

friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,192]
labels = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends, minutes)


#nomeia cada posição
for label, friend_count,minute_count in zip(labels, friends, minutes):
  plt.annotate(label,
               xy=(friend_count, minute_count), # coloca rótulo com sua posição
               xytext=(5,-5),                  
               textcoords='offset points')
  plt.title("Minutos Diários vs. Números de Amigos")
  plt.xlabel(" De Amigs")
  plt.ylabel(" Minutos diários passados no site")
  plt.show()