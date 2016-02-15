#!/usr/bin/python
# -*- coding: utf-8 -*-

# hola, hola

fichero = open('/etc/passwd', 'r');

lineas = fichero.readlines();
fichero.close();

diccionario = {};

for linea in lineas:
    elementos = linea.split(':')
    usuario = elementos[0]
    shell = elementos[-1][:-1];
    diccionario[usuario] = shell;

print("La shell de root es: " + diccionario["root"]);
try:
	print(diccionario["imaginario"]);
except:
	print "El nombre de usuario 'imaginario' no existe"