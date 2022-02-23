lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print (len(tupla))
print(len(lista_animal))
tupla_animal = tuple (lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)


# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print (soma)