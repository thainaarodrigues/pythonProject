''''EXERCÍCIO
Escreva uma função que recebe um objeto de coleção (lista, set, conjunto, tupla),
e retorna o valor do maior numero dentro dessa coleção. Faça outra função que retorne o
menor número dessa coleção.'''


def numero_maior(lista):
    i = lista.__getitem__(0)
    for numero in lista:
        if numero > i:
            i = numero
    return i #A identação precisa estar de acordo para chegar no resultado correto


def numero_menor(lista):
    i = lista.__getitem__(0)
    for numero in lista:
        if numero < i:
            i = numero
    return i


lista_de_numeros = []
print("\nLISTA DE NÚMEROS", "\n(Para finalizar, tecle n)\n")
numero = int
n = int

while numero != 'n':
    numero = input("Escreva um número: ")
    if numero != 'n':
        lista_de_numeros.append(int(numero))

print("\nLista:", lista_de_numeros)
print("\nO número maior é: ", numero_maior(lista_de_numeros))
print("O número menor é: ", numero_menor(lista_de_numeros))