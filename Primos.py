#!/usr/bin/python
# -*- coding: utf_8 -*-
#TAREA 2

#NUMEROS PRIMOS

def primos(n):
	'''Recibe un numero n y devuelve los numeros primos que hay entre 0
	y n
	'''
	lista_primos= list()
	for a in range(1,n+1):	
		divisible = False	
		for b in range(2,a):
			if ((a%b)==0) :
				divisible = True
				break
		if not(divisible):
			lista_primos.append(a)

	return lista_primos
	print lista_primos #para probarla
	
  
