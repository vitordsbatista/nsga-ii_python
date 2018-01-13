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
import random as rd

#Cria a população inicial
def gen_pop(pop_size, ind_size, ind_range, pop_type):
    """ Cria uma população
    Parâmetros: pop_size(int) - Tamanho da população
                ind_size(int) - Tamanho do indivíduo
                ind_range([min, max]) - Intervalo dos gens do indivíduo
                pop_type('bin', 'int', 'float') - Tipo dos gens do indivíduo

    Retorno:   pop(list) - Lista com a população inicial
    TODO: criar a população em binário e em float
    """
    pop = list()
    if pop_type == 'bin':
        pass
    elif pop_type == 'int':
        for i in range(pop_size):
            x = rd.sample(range(ind_range[0], ind_range[1]), ind_size)
            pop.append(x)
    elif pop_type == 'float':
        pass
    return pop

#Dominância de uma população
def non_dom_sort(pop, fit):
    """ Realiza o processo de não dominância de uma população
    Parâmetros: pop(list) - lista com os indivíduos nela
                fit(list) - lista com as fits do algoritmo
    Retorno:    pop_out   - lista com os indivíduos não domidados de pop
    """
    pop_out = [pop[0]]                      #Inicia a pop_out 
    for n, i in enumerate(pop):
        if not (i in pop_out):              #Se o i não está no pop_out
            pop_out.append(i)               #Adiciona o i na pop_out
            pop_out_tmp = pop_out[:]        #Copia a pop_out
            for m, j in enumerate(pop_out_tmp):
                if i != j:                  #Não compara dois iguais
                    if dom(i, j, fit):      #Se o i domina o j
                        if j in pop_out :
                            pop_out.remove(j)   #Remove o j do pop_out
                    elif dom(j, i, fit):    #Se o j domina o i
                        if i in pop_out:
                            pop_out.remove(i)   #Remove o i do pop_out
    return pop_out

#Dominação (verifica se o a domina o b)
def dom(ind1, ind2, fit):
    """  Verifica se um indivíduo domina o outro. A verificação é se o ind 1 
        domina o ind 2, se verdadeiro, retorna True, caso contrário, 
        retorna False

    Parâmetros: ind1(list) - indivíduo 1
                ind2(list) - indivíduo 2
                fit(list) - lista com as fits do problema
    Retorno:    boolean
    """
    for f in fit:
        if f(ind1) > f(ind2):   #Caso uma fit do ind1 for pior que a do ind2
            return False        #Retorna False
    for f in fit:               #Caso uma fit do ind1 for melhor que a do ind2
        if f(ind1) < f(ind2):
            return True         #Retorna True
    return False                #Se nada acontecer, retorna False

#==============================================================================#
#Fitness
#==============================================================================#
def f1(ind):
    x, y = ind
    a = 4*pow(x,2)+4*pow(y,2)
    if g1(x, y):
        a = a+2
    if g2(x, y):
        a = a+2
    return a
def f2(ind):
    x, y = ind
    a = pow((x-5),2) + pow((y-5),2)
    if g1(x, y):
        a = a+2
    if g2(x, y):
        a = a+2
    return a
def g1(x, y):    
    s = pow((x-5),2) + y**2
    if s <= 25:
        return True
    return False
def g2(x, y):
    s = x - 3*y + 10
    if s <= 0:
        return True
    return False
