# -*- coding: utf-8 -*-
"""Modulo_01_07_Elena.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IWWIfehIah8rZ78PSP8PAiVtG0JFC6AA
"""

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True
is_prime(9)

contador = 0
last_prime = 1
last_no_prime = 2
next_number = last_prime + 1
lista_no_primos = []

while contador<20:
  next_number = next_number + 1
  if is_prime (next_number):
    contador = contador + 1
    last_prime = next_number
  else:
    contador = contador +1
    last_no_prime = next_number
    print (last_no_prime)