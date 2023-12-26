def transformar_int_listas(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return lista.copy()

def adicionar_elemento_lista(lista):
    for numero in lista:
        if numero not in lista3:
            lista3.append(numero)

# Pegar cada uma das listas
lista1 = input().split()
lista2 = input().split()

# Transformar a listas com tipo strings para números inteiros
lista1 = transformar_int_listas(lista1)

lista2 = transformar_int_listas(lista2)

# adicionar cada valor da lista 1 na lista 3
lista3 = []

# Adicionar cada valor lista1 na lista3
lista3 = adicionar_elemento_lista(lista1)

# Adicionar cada valor lista2 na lista3
lista3 = adicionar_elemento_lista(lista2)

print(lista3)