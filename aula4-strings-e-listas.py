frase = 'Oi, tudo bem?'
print (frase) #Resultado: Oi, tudo bem?

'''STRING - O phyton trata string como uma lista de letras/caracteres
A LISTA sempre inicia a contagem com 0 (O é 0, I é 1, vígula é 2, etc)
Então se eu quiser imprimir o 'O', basta:'''

print(frase[0]) #Resultado: 'O'

# LISTA é uma coleção, e você consegue colocar várias coisas dentro dela
# O que tiver dentro do colchete é um item (come se fosse um caractere no caso na frase)
lista_nomes = ['João', 'Maria', 'Guilherme', 'Diego', 10, 10.2, True]
print(lista_nomes[0]) #Resultado: João
print(lista_nomes[2]) #Resultado: Guilherme
print(lista_nomes) #Resultado: ['João', 'Maria', 'Guilherme', 'Diego', 10, 10.2, True]
print(frase[12])#Resultado: ?

#Você também pode imprimir intervalos utilizando dois pontos entre os índices [x:y]
print(frase[0:5]) #Resultado: Oi, t (ele conta espaço como caractere)

#Você pode usar mais um : (step) para indicar de quantos em quantos números vai pular
print(frase[0:13:1]) # O 1 é o padrão, vai contar de 1 em 1 (Oi, tudo bem?)
print(frase[0:13:2]) # Com o 2, ele vai printar a cada 2 caracteres no intervalo de 0 a 13 (ou seja, pula 1 - O,td e?)

print(lista_nomes[0:2]) #Resultado: ['João', 'Maria'] - não imprime o item 2
#PS: para listas, ele imprime até o nº indicado, mas sem incluí-lo (conforme exemplo acima) - o último nunca é incluso

#Você também pode usar índices negativos. Por exemplo, o -1 sempre vai puxar o ultimo item da lista
print(lista_nomes[-1]) #Resultado: True (conta de trás pra frente)
print(lista_nomes[-3]) #Resultado: 10 (terceiro de tras pra frente)

#O passo também pode ser negativo (desde que os índices também sejam)
print(lista_nomes[-1:-4:-1]) #Resultado: [True, 10.2, 10]

#Para INVERTER a frase basta deixar os índices em branco e colocar -1 como passo (step)
print(frase[::-1]) #Resultado: ?meb odut ,iO

'''OPERAÇÕES DE LISTA'''
#PARA LISTAS

#.append() - usado para inserir mais nomes na lista (sempre no último lugar)
lista_nomes.append('Geralda')
print(lista_nomes) #Resultado: ['João', 'Maria', 'Guilherme', 'Diego', 10, 10.2, True, 'Geralda']

#.remove() - usado para remover algum item da lista (o que estiver dentro dos parenteses)
lista_nomes.remove('João')
print(lista_nomes) #Resultado:['Maria', 'Guilherme', 'Diego', 10, 10.2, True, 'Geralda']

#.clear() - usado para limpar a lista, ela fica vazia
'''lista_nomes.clear()
print(lista_nomes) #Resultado: []'''

#.insert() - usado para falar o local onde quer inserir determinado nome (onde, o que)
lista_nomes.insert(1, 'Thainá') #Resultado:
print(lista_nomes) #Resultado: ['Maria', 'Thainá', 'Guilherme', 'Diego', 10, 10.2, True, 'Geralda']

#Para substituir um nome diretamente na lista, basta fazer uma atribuição no índice
lista_nomes[0] = 'George' #isso irá tornar o índice 0 (Maria) em George.
print(lista_nomes) #Resultado: ['George', 'Thainá', 'Guilherme', 'Diego', 10, 10.2, True, 'Geralda']

#.count() - para CONTAR quantos itens se repetem na lista
contador_thaina = lista_nomes.count('Thainá') #Ele diferencia acento para contar
print(lista_nomes) #imprimir só pra confirmar a quantidade
print(contador_thaina) #Resultado: 1

#len() - para saber o tamanho de alguma coisa, pode ser uma frase, uma lista.
print(len(lista_nomes)) #Resultado: 8 (oito itens na lista)

#.pop() - sempre vai pegar o último item da lista para print e depois vai retirá-lo da lista
print(lista_nomes.pop()) #Resultado: Geralda
print(lista_nomes) #Resultado: ['George', 'Thainá', 'Guilherme', 'Diego', 10, 10.2, True]
#Se colocar mais um, ele vai fazer com os dois últimos
print(lista_nomes.pop()) #Resultado: True
print(lista_nomes) #Resultado: ['George', 'Thainá', 'Guilherme', 'Diego', 10, 10.2]

#PARA STRINGS - não tem todas as funções que podem ser aplicadas em lista (Ex: append, mas tem count)

#.lower() - passa tudo para letra minúscula (não é uma alteração permanete)
print(frase.lower()) #Resultado: oi, tudo bem?

#.upper() - transforma tudo em maiúsculo

#split() - transforma em lista, separa a frase onde você quer (coloca o que vai usar como separador dentro dos parênteses)
frase_separada = frase.split(',')
print(frase_separada) #Resultado: ['Oi', ' tudo bem?'] o 0 é o Oi e o 1 o Td bem?
print(frase_separada[0]) #Resultado: Oi
print(frase_separada[1]) #Resultado: tudo bem?

#Para concatenar (juntar) strings
frase_nova = frase + ' Como vai você?'
print(frase_nova) #Resultado: Oi, tudo bem? Como vai você?
