#! /usr/bin/python
#Author: jcastelo on 240218

a = 4
b = 27

suma = (a + b)
resta = (a - b)
multp = (a * b)
div = float(a) / float(b)

#SI a<b el resultado sera a
porc = (a % b)

#Estamos utiizanco str() para poder mostrar el resultado en pantalla ya que estamos concatenando cadenas
print 'La suma de a = ' + str(a) + ' y b = ' + str(b) + ' es: ' + str(suma)
print 'La resta de a = ' + str(a) + ' y b = ' + str(b) + ' es: ' + str(resta)
print 'La multiplicacion de a = ' + str(a) + ' y b = ' + str(b) + ' es: ' + str(multp)
print 'La division de a = ' + str(a) + ' y b = ' + str(b) + ' es: ' + str(div)
print 'El modulo de a = ' + str(a) + ' y b = ' + str(b) + ' es: ' + str(porc)