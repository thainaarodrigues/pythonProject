'''FUNÇÕES
Sempre que a cor destaca e fica entre parêncteses. Dentro dos parênteses ficam os
parâmetros. Exemplos:
print() - imprime
len() - conta os caracteres
Se escrever a função e clicar em cima apertando ctrl, aparece uma biblioteca explicando ela
As funções podem ser criadas. Uma vez definida, não precisa ficar reescrevendo.'''
# Para criar uma função, deve escrever def na frente
# dentro dos ()o que vai ser passado pro soma
def soma(numero1, numero2):
    resp = numero1 + numero2 #variável de resposta
    return resp #quando alguem chamar a função soma, vai passar por n1 e n2, somar e retornar resposta

retorno = soma(75,1289) #fica mais fácil colocar a função dentro de uma variável
print(retorno) #Resultado: 1364

#Uma funçºao não precisa ter retorno ou argumento. Exemplo:
def imprime_oi():
    print("Oi") #Resultado: OI

imprime_oi()
imprime_oi()
imprime_oi() #Resultado: Oi Oi Oi Oi

def tem_sete_itens(argumento): #vai contar se o len do argumento é 7
    if len(argumento) == 7:
        return True #ou return(True)
    else:
        return False

print(tem_sete_itens("Oi pessoal, tudo bem?")) #Resultado: False, pq tem mais de 7
print(tem_sete_itens("1234567")) #Resultado: True

if tem_sete_itens('1234567'):
    print("Realmente tem sete letras") #Resultado: Realmente tem sete letras

#Não pode ser usado pra nº pq nº não tem len, mas pode ser usado pra dicionario, lista, conjunto, etc

if tem_sete_itens({1,2,3,4,5,6,7}):
    print("Realmente tem sete letras") #Resultado: Realmente tem sete letras

'''MÉTODO
É chamado de métdodo quando não tem retorno, exemplo o print Oi.
Não tem um consenso sobre essa definição. Não é importante'''

''''EXERCÍCIO
Escreva uma função que recebe um objeto de coleção (lista, set, conjunto, tupla),
e retorna o valor do maior numero dentro dessa coleção. Faça outra função que retorne o
menor número dessa coleção.'''


