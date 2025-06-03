minha_tupla = (1, 2, 3, 4, 5)
lista_modificavel = list(minha_tupla)
lista_modificavel[1] = 10
minha_tupla_modificada = tuple(lista_modificavel)
print(minha_tupla_modificada)