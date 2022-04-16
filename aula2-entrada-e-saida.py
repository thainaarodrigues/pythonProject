#Saída é printar no monitor, escrever na tela, imprimir na tela. No python é print ()
#Print: imprime uma string (somente texto), pode ser entre aspas duplas (“ ”) ou simples (‘ ‘)
#CTRL+SHIFT+F10 você roda o programa que está na tela
# SHIFT+F10 ou o ‘play’ ele roda o ultimo que foi rodado;
print('Hello world!')
print('Segundo print')
#para escrever na mesma linha:
print('hello world!Segundo print')
#Para quebra de linha, basta colocar \n onde quer que aconteça?
print('Hello World!\nSegundo print')
#Para inserir um espaco, tab, colocar \t
print('Hello World!\tSegundo print')

#VARIÁVEIS sao objetos no python (nome=, abacaxi=, a=. b=). Nela voce coloca uma string.
#São sempre escritas com letra minúscula e para espaços usa underline _. E precisam ser TEXTOS
nome = 'Guilherme' #se apertar pra rodar nao vai acontecer nada, porque nao tem funcao nenhuma
print(nome) #dessa forma roda, pois coloquei o comando de printar a variável nome
#se você alterar a variável de nome, ele vai imprimir o que vocẽ colocar dentro da variável (nome, número, função)
tipo_nome = type(nome) #a função type identifica o tipo de variável
print(nome)
print(tipo_nome) #o resultado class 'str' significa string, texto

#INTEIRO
idade = 29 #se colocar o 29 entre aspas vira um texto
tipo_idade = type(idade)
print(idade)
print(tipo_idade) #o resultado 'int' significa um número inteiro
#apesar de 27 não ser um texto, a impressão é possível pq o python converte, em outras linguagens daria erro

#DECIMAL
altura = 1.62 #não se usa vírgulas para número, sempre ponto
tipo_altura = type(altura)
print(altura)
print(tipo_altura) #o resultado 'float' indica um número decimal, quebrado

#para concatenar e imprimir tudo junto ao invés de escrever print várias vezes, use a vírgula (,) ou mais (+)
print(nome, 'tem', idade, 'anos e', altura, 'de altura.' ) #Guilherme tem 29 anos e 1.62 de altura.
#o mais (+) também pode ser usado para concatenar, porém os numeros deverão ser convertidos em string
print(nome + 'tem' + str(idade) + 'anos e' + str(altura) + 'de altura.' ) #Guilhermetem29anos e1.62de altura.
#o mais não coloca sinalo, voce precisa inserir na mão, utilizando os textos da frase
print(nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura.' ) #Guilherme tem 29 anos e 1.62 de altura.
#a vantagem de usar o + é que você pode converter tudo em uma variável
frase = nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura.'
print(frase) #Guilherme tem 29 anos e 1.62 de altura.

#Para fazer o programa DINAMICO, ou seja, para que ele pergunte o nome, idade e altura de alguem para imprimir:
#INPUT: função para perguntar o que é a variável apra o usuário, pode ser em branco ou pode escrever a pergunta.
nome_dinamico = input('Escreva seu nome:') #na tela aparecerá o cursor, escreva seu nome e dê enter
idade_dinamica = input('Escreva sua idade:')
altura_dinamica= input('Escreva sua altura:')
print(nome_dinamico, 'tem', idade_dinamica, 'anos e', altura_dinamica, 'de altura.') #resultado personalizado usuário
#input sempre retorna com um objeto do tipo string:
print(type(nome_dinamico), type(idade_dinamica), type(altura_dinamica)) #<class 'str'> <class 'str'> <class 'str'>

#OPERAÇOES MATEMÁTICAS
numero1 = 27
numero2 = 53
numero3 = 10
resultado = (numero1 + numero2) * 5 #400
print(resultado) #80, pode fazer qualquer conta, +, -, /, *, pode jogar número direto no resultado
#para elevar ao quadrado basta colocar dois * (** 2), para raiz quadrada **(1/2)
resultadoquadrado = numero3 ** 2
print(resultadoquadrado) #100

#Para comentários de mais de uma linha, usar tres aspas simples pra abrir e 3 para fechar, pode dar enter:
'''
EXERCÍCIO: Faça um formulário que pergunte 
o nome, cpf, endereço, idade, altura e telefone 
e imprima isso em um relátório organizado.
'''

