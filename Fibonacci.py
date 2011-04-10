#!/usr/bin/python
# -*- coding: utf_8 -*-
#TAREA 2

#FUNCION DE FIBONACCI


def fibonacci(n):
	'''Recibe el numero n y devuelve los numeros de
	Fibonacci hasta dicho numero
	'''
	lista= list()
	a=1
	b=1
	c=0
	lista.append(c)
	while (b<=n):
		lista.append(b)
		a,b = b, a+b
	return lista
	print lista #para probarla

