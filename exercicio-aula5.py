''' EXERCÍCIO - Faça um programa que leia a quantidade de pessoas (usando input) que
serão convidadas para uma festa. Após isso o programa irá perguntar o nome de todas
as pessoas (usa while ou for, usando só uma linha como input) e colocar em uma lista
de convidados. Após isso irá imprimir todos os nomes da lista. '''

print('LISTA DE CONVIDADOS PARA FESTA\n')

convidados = int(input('Número de convidados: '))

i = 1  # O i começando de 0, vai rodar de 0 a 3 (4 numeros), começando de 1, ficam 3 numeros
lista_nomes = []

while i <= convidados:  # usando for seria: For i in range (convidados)
    nome = input(
        'Escreva o nome do convidado #' + str(i) + ': ')  # o '+ str(i) +' serve para que ele imprima o valor de i
    i += 1
    lista_nomes.append(nome)

print('\nLista de convidados: ')

for nomenalista in lista_nomes:
    print(nomenalista)

###################################################################################################################

eliminados = int(input('\nEscreva quantos eliminados do BBB 22 se lembra: '))
lista_eliminados = []
i = 1

while i <= eliminados:
    exBBB = input('Escreva o nome do eliminado #' + str(i) + ': ')
    lista_eliminados.append(exBBB)
    i += 1

print('\nLista de eliminados do BBB 22:')

for resultado in lista_eliminados:
    print(resultado)
