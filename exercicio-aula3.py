''' Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela está apta a ser do Exército.
Para entrar no exército é preciso ter mais de 18 anos,
pesar mais ou igual de 60 quilos e medir mais ou igual a 1,70 metros'''

print('INSCRIÇÃO PARA O EXÉRCITO \nPreencha seus dados:')

nome = input('Nome:')
idade = int(input('Idade:')) #preciso converter de str para inteiro
peso = float(input('Peso:'))#preciso converter de str pra decimal
altura = float(input('Altura:'))#preciso converter de str pra decimal
limite_idade = 18 #poderia não ter usado isso e colocado os valores direto no IF
limite_peso = 60
limite_altura = 1.70

if idade >= limite_idade and peso >= limite_peso and altura >= limite_altura:
    print(nome,', você está apto para entrar no exército!')
else:
    print(nome,', você não atende a um dos requisitos para candidatura.')