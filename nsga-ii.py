#!/usr/bin/python
# -*- coding: utf-8 -*-
#===================================#
# File name: 						#
# Author: Vitor dos Santos Batista	#
# Date created: 					#
# Date last modified: 				#
# Python Version: 2.7				#
#===================================#

import numpy as np
import matplotlib.pyplot as plt
import functions as f

#==============================================================================#
#Parâmetros
#==============================================================================#
n_ind = 10
ind_size = 2
pop_size = 100
ind_range = [0, 6]
fronts = dict()
fit = [f.f1, f.f2]                          #Todas as funções de fitness

#==============================================================================#
#Inicialização
#==============================================================================#
#Criação da população inicial
pop = f.gen_pop(pop_size, ind_size, ind_range, 'int')

#Criação dos fronts
i = 0                                       #Contador
while any(pop):                            #Enquanto existir algo na pop
    tmp = f.non_dom_sort(pop, fit)  #Front não dominado
    #Remove o front da população
    for j in tmp:
        pop.remove(j)
    fronts[str(i)] = tmp                    #Adiciona ele no dicionario
    i += 1                                  #Incrementa o contador
    

#==============================================================================#
#Loop principal
#==============================================================================#




#==============================================================================#
#Plot dos fronts
#==============================================================================#
#Plot dos fronts [f1:]
for i in range(1,len(fronts)):
    for j in fronts[str(i)]:
        k = []
        for f in fit:
            k.append(f(j))
        plt.plot(k[0], k[1], 'o', color='b')
    plt.plot(k[0], k[1], 'o', color='b')
#Plot do fornt f0, fiz isso pq existem alguns ind que ficam em dois fronts,
#e assim o f0 sempre fica em destaque
for i in fronts['0']:
    k = []
    for f in fit:
        k.append(f(i))
    plt.plot(k[0], k[1], 'o', color='r')
plt.plot(k[0], k[1], 'o', color='r', label='f0')
#Exibe o plot
plt.legend(loc='best')
plt.show()
