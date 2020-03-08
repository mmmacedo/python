# -*- coding: utf-8 -*-

#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
tupla = ("alface", "tomate", "cenoura")
try:
    tupla[0] = "beterraba"
except: 
    print("Deu ruim, tuplas não podem ser modificadas!")

print(tupla)