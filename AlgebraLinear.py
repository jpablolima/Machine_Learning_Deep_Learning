# -*- coding: utf-8 -*-
#________ Importar para alterar a fonte padrão__________# 
from __future__ import unicode_literals
#_______________________________________________________#
from matplotlib import pyplot as plt


height_weight_age = [70, # Polegadas 
                     170, # quilos
                     40] # Anos
grades = [90, # teste1
          80,#teste2
          75,#teste3
          62] # teste4
def vector_add(v,w):
  "soma dos elementos Correspondente"
  return[v_i + w_i
         for v_i, w_i in zip(v, w)]
def vector_subtract(v,w):
  "Subtração dos elementos correspondente"
  return[v_i - w_i
         for v_i, w_i in zip(v,w)]
  def vector_sum(vectors):
    "Soma de todos os elementos correspondente"
    result = vectors[0]
    for vector in vectors[1]:
      result = vector_add(result, vector)
    return result
def vector_sum(vectors):
  return reduce(vector_add, vectors)
#vector_sum = partial(reduce, vector_add)

def scalar_multply(c,v):
  "C é um número, v é um vetor"
  return[c * v_i for v_i in v]

def vector_mean(vectors):
  #"computar o vetor cujo i-ésimo elemento seja a média dos i-ésimos 
  #"elementos dos vetores incluidos"
  n = len(vectors)
  return scalar_multply(1/n, vector_sum(vectors))
  
  def dot(v,w):
    #"v_i * w_i + ... + v_n + w_n"
    return sum(v_i * w_i
            for v_i, w_i in zip(v,w))
  