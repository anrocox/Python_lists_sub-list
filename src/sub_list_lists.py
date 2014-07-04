#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 2, 2014

@author: anroco

How to get a list of sub-lists in python?

¿como obtener una sub-lista de una lista en python?
'''

#create a list
lista = ['a', 'b', 'c', 'd', 'e']
print (lista)

#used list[i:j] where 'i' is the starting index and 'j' is the index of the end
#the start index is inclusive and the end index is exclusive.
sub_list = lista[1:3]
print(sub_list)

#if the start index isn't defined, is taken from the beginning of the list.
sub_list = lista[:3]
print(sub_list)

#if the end index isn't defined, is taken until the end of the list
sub_list = lista[1:]
print(sub_list)

#if neither is defined, returns the full list
sub_list = lista[:]
print(sub_list)

#The indexes can be defined with negative values
sub_list = lista[-3:-2]
print(sub_list)
