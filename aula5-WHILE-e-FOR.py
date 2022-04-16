'''ESTRUTURAS DE LAÇO - While e For'''

nomes = ['Guilherme', 'Marcelo', 'João', 'Júlia']
#para criar uma lista vazia, basta criar com dois colchetes vazios (nomes = [])

'''FOR - for (como vai chamar os indices) in (nome da lista)
serve para criar um programa que mostre um nome de cada vez - Estrutura de laço'''
for nome in nomes: #é a estrutura de for, vai percorrer. 'nome' poderia ser X, Y, nomes, etc
    print(nome) #Resultado: Guilherme Marcelo João Júlia. Vai imprimir enquanto houver nomes

#FUNÇÃO range(x) - cria uma lista de X números de 0 ao número indicado (excluindo ele)
# range(x, y) - cria uma lista de números de X até Y (sem incluir Y)
# range(x, y, z) - Z é o passo, conta de Z em Z de X até Y

for item in range(0,10,2):
    print(item)
    # Resultado: para range(5)- 0 1 2 3 4
    # Resultado: para range(5, 10)- 5,6,7,8,9
    # Resultado: para range(0,10,2)- 0,2,4,6,8

#Podemos usar o range para indicar quais nomes queremos imprimir dentro da lista de nomes

for i in range(4): #para o item no range 4 (0-3)
    print(nomes[i]) #imprimir nomes dentro do índice i. O ítem é substituido por algo dentro da coleção indicada (nomes)
    #Resultado: Guilherme Marcelo João Júlia.
    # PS: i não pode ser maior que a coleção (lista). Para que isso não aconteça, pode usar o len()
    # O len() retrona ao tamanho do objeto. Dessa forma, jamair será maior que a coleção.
for i in range(len(nomes)):
    print(nomes[i]) #Resultado: Guilherme Marcelo João Júlia.
    nomes.append('OII') #Sempre que o programa rodar (4x), vai adicionar um OII ao final na lista

print(nomes) #Resultado: ['Guilherme', 'Marcelo', 'João', 'Júlia', 'OII', 'OII', 'OII', 'OII']

# Usando o FOR em strings (uma string também é uma coleção)
palavra = 'Thainá Rodrigues'

for letra in palavra:
    print(letra) #Resultado: imprimiu uma letra do nome por linha (incluindo espaço)


'''WHILE (enquanto)- sempre envolve uma decisão. 
Serve para fazer estruturas que se repetem até determinado momento (que você decide)
Nesse caso tem que ter cuidado com loops infinitos'''

i = 0

while i < 10:
    print('i ainda é menor que 10: ', i)
    i = i + 1 # ou (i += 1) Inteirar o i, somar 1 ao i anterior. Impede o loop infinito, pq em determinado momento i>10
    # Programa começa com i=0, enquanto for verdade (True) vai somar +1 e mostrar o valor de i
    # Resultado: i ainda é menor que 10:  de 0 a 9 (um em cada linha)
print('Acabou o while, i terminou com o valor de: ', i) # Quando o while não for mais verdade vai imprimir essa frase

# Aplicação do +=1 para contar (supondo que a função len() não existisse.
listafrutas = ['maçã', 'pera', 'uva', 'abacaxi', 'goiaba']

contador = 0

for fruta in listafrutas:
    contador += 1

print('Total de frutas é: ', contador) # Resultado: Total de frutas é:  5
print('Usando o len() seria: ',len(listafrutas))

# BREAK - é o parar, comando para sair da repetiçºao (tanto em FOR quanto WHILE)

numero = 0
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1
    # Printa o número e compara se é igual a vinte, se não for soma +1, Faz isso até que seja  =20, que ai ele pára.
(print('Saiu do While - break'))

'''EXERCÍCIO - Faça um programa que leia a quantidade de pessoas (usando input) que
serão convidadas para uma festa. Após isso o programa irá perguntar o nome de todas
as pessoas (usa while ou for, usando só uma linha como input) e colocar em uma lista 
de convidados. Após isso irá imprimir todos os nomes da lista. '''