''' LISTA - usada com colchetes
É uma coleção, e você consegue colocar várias coisas dentro dela '''
# minhalista = ['Gui','João']

''' TUPLA - usada com parênteses
Não é mutável como a lista, não pode remover ou adicionar objetos (tem nº definido de coisas)
você consegue alterar valor de objetos, mas não o nº de itens '''
# minhatupla = ('Gui','João')

'''DICIONÁRIO - usado com chaves
Tem uma chave (key) e um valor (value), tal como um dicionario de portugues.
Ex: cadastro. Também conhecido como Dict '''
# meudicionario = {'nome': 'Guilherme', 'idade': 27}

'''CONJUNTO (set) - usado com chaves, é uma lista misturada com dicionário
Não tem chave de valor, somente os valores lá dentro. Não é ordenado, não tem índice.
No conjunto não existe itens repetidos (isso que o difere da lista)'''
# meuconjunto = {'Gui, 'João'}

#TUPLA
minhatupla = ('Gui', 'João')

print(minhatupla) # ('Gui', 'João')
print(minhatupla[1]) # João

for nome in minhatupla:
    print(nome) #Gui \n João

# Para substituir a tupla é preciso substituir ela toda.
minhatupla = ('João', 'Fabrício')
print(minhatupla) # ('João', 'Fabrício')

#Para perguntar se um item está dentro de uma coleção (pode usar pra todos, menos dicionário)
if 'Fabrício' in minhatupla:
    print('Está na coleção!') #Está na coleção!


#DICIONÁRIO (usando o ponto tem várias funções), para buscas é mais eficiente que listas
meudicionario = {'nome': 'Guilherme', 'idade': 27}
print(meudicionario) # {'nome': 'Guilherme', 'idade': 27}
print(meudicionario['nome']) #não tem indice, tem chave (nome). Resultado: Guilherme
print(len(meudicionario)) #o len pode ser usado com qualquer coleção. Resultado 2 (tamanho)

'''if 'Guilherme' in meudicionario.values(): #para procurar valores dentro do dicionario
    print('Guilherme está no dicionário') #Resultado: Guilherme está no dicionário'''

for valores in meudicionario.values(): #se colocar .keys vai impromir as chaves
    print(valores) #Resultado: Guilherme \n 27

meudicionario['nome'] = 'João' #Para alterar o valor da chave nome
print(meudicionario) # Resultado: {'nome': 'João', 'idade': 27}

meudicionario['endereço'] = 'Av. João das Neves' # Para adicionar uma nova chave
meudicionario['telefone'] = '98282-2988'
print(meudicionario) #{'nome': 'João', 'idade': 27, 'endereço': 'Av. João das Neves', 'telefone': '98282-2988'}

# meudicionario.clear (limpa) meudicionario.pop (ir tirando, igual lista) .copy .update

# CONJUNTO - usa quando não quer repetir valores
meuconjunto = {'Gui', 'João'}
print(meuconjunto) #Não tem indice, não tem ordem. print(meuconjunto[0]) não funciona

meuconjunto.add('Maria') #Para adicionar um valor no conjunto
print(meuconjunto) # {'Maria', 'João', 'Gui'}
meuconjunto.add('Gui')
print(meuconjunto) # {'Maria', 'João', 'Gui'}. Não repete valores

if 'Gui' in meuconjunto:
    print('Foi encontrado dentro do conjunto!') #Foi encontrado dentro do conjunto!
'''Na lista o python compara Gui com todos os itens da lista, ja o conjunto é uma 
tabela HASH, cada palavra é transformada em um código que é ransformada em uma tabela,
então a busca é instantânea. Se fizer na lista demora mais. Bom para estrutura de dados
grande. Conjunto e dicionário são instantâneos.'''

# Para inicializar a estrutura vazia
lista = []
tupla = ()
dicionario = {}
conjunto = set()

#Você pode usar uma estrutura dentro da outra
mixdeestrutura = [(1,2), (3,4), (5,6), ({'João', 'Maria'}, {'Gabriel'})]
print(mixdeestrutura) #LISTA ( tupla, tupla, tupla, tupla (conjunto (item), conjunto (item))

# Site: doc python 3 você tem tudo que tem na aula detalhado (boa fonte de estudo) - EM INGLÊS



