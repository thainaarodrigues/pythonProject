
#DADO BOOLEANO -> Boolean: tem duas formas, verdadeiro ou falso.
var_verdade = True
var_false = False
print(type(var_verdade),type(var_false)) #resultado 'bool'

#É através dele que o phyton toma decisões utilizando If ou Else.
#Quando você usa somente um =, está atribuindo variáveis, quando usa dois ==, está comparando valores
#Para comparação pode utilizar ==, > ou <, >= ou <=, != (saber se é igual, maior ou menor, diferente)
''' Exemplo 1: if var_verdade == True: #dois pontos inicia a função. Se quiser escrever fora da função, basta escrever em uma linha sem os 4 espaços
    print('Var verdade é verdadeiro')
    # o espaço antes do print se chama identação, uma sentença está dentro da outra, e só acontece quando a de cima é cumprida
    # Para ajudar na comparação, pode utiilizar o OR (apenas um requisito o torna verdadeiro) e o AND (precisa ter os dois requisitos)
    Vai no phyton Console para ver como acontece a comparação escreva: >>> 1 = 1 e dê enter, ele vai te responder True
    Você pode comparar, números, strings, boolean, floats. No console pode testar todas as variáveis lógicas. 
    Ex: 1 == 1 and 1 == 2 (False)    -    1 == 1 or 1==2 (True)    -   True or False (True)    -   1<=2 (True)'''
a = 50
b = 20

if a > b: #se isso acontecer, faça isso:
    print(a, 'é maior que', b)
else: #se não acontecer, faça isso:
    print(a, 'é menor do que', b) #Resultado: 2 é menor do que 20
#EXEMPLO 2 (USANDO AND E OR)
c = 50
d = 20
if ((c > d) and ('abacaxi' == 'uva')) or 2 == 2 or True: #se isso acontecer, faça isso. Se abacaxi == abacaxi, o if vai funcionar. O true valida sempre esse enunciado.
    print(c, 'é maior que', d)
else: #se não acontecer, faça isso:
    print('Não deu certo o if :(') #Resultado: Não deu certo o if :(

#PARA FAZER UM MENU DE OPÇÕES
print('Menu:\n1 = Escreve Guilherme\n2 = Escreve João\n3 = Escreve Maria\n')
opcao = input('Escolha uma opção:')
#Para fazer a lógica do programa:
if opcao == '1':
    print('Guilherme')
elif opcao == '2': #funciona, mas a forma correta é o elif. Roda ainda que a afirmação já seja valida
    print('João')
elif opcao == '3': #elif= se não se. Se deu certo em cima nao executa mais
    print('Maria')
    '''A forma correta de comparar, seria usando o 'elif' (else if)
    Se opcao = 1, faça isso, se nao se =2 e se não se =3.. 
    O else dará uma responsta caso a opção escolhida esteja fora das condições especificadas'''
else:
    print('Opção Inválida!')

#NOT - COMO USAR
print (True) #imprime verdadeiro
print (not True) #imprime o que não é verdadeiro, ou seja, FALSO

idade = 50

if idade == 50:
    print('\nVocê tem 50 anos.')
else:
    print('\nVocê não tem 50 anos')
    #Resultado seria: Você tem 50 anos
#Usando o not, ficaria assim:

peso = 30
if not peso == 30:
    print('Você não tem 30 kg') #se não for 30, entra aqui
else:
    print('Você tem 30 kg') #se for 30 entra aqui

if True:
    print('\nEntrou no if')
else:
    print('\nEntrou no else')

if not True:
    print('\nEntrou no if')
else:
    print('\nEntrou no else')

''' Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela está apta a ser do Exército.
Para entrar no exército é preciso ter mais de 18 anos,
pesar mais ou igual de 60 quilos e medir mais ou igual a 1,70 metros'''