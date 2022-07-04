# Para fazer programas no estilo SQL map (feito em python) - sem ser interativo
# BIBLIOTECA são codigos pré-escritos em python, e assim podera usar mais métodos e funções

'''Para importar uma BIBLIOTECA'''

import sys # permite usar algumas coisas do sistema operacional

argumentos = sys.argv #Os argumentos são recebidos como string, é preciso passar para nº float
#arg1 metod (o que fazer) // arg2 - n1 (numero)// arg3 - n2 (numero)

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if argumentos [1] == "soma":
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    resp = sub(float(argumentos[2]), float(argumentos[3]))

print(resp)

#Resultado: ['/home/thainaarodrigues/PycharmProjects/pythonProject/aula-8-passagem-de-argumentos.py']
#O argumento nº 0 que o sistema passa é sempre o caminho do arquivo do python
#No terminal pode rodar mais argumentos (por aqui só roda o primeiro) ou usar o Prompt de Comando
'''NO TERMINAL
(venv) thainaarodrigues@penguin:~/PycharmProjects/pythonProject$ python3 aula-8-passagem-de-argumentos.py 
['aula-8-passagem-de-argumentos.py']
(venv) thainaarodrigues@penguin:~/PycharmProjects/pythonProject$ python3 aula-8-passagem-de-argumentos.py  aaa bbb
['aula-8-passagem-de-argumentos.py', 'aaa', 'bbb']
(venv) thainaarodrigues@penguin:~/PycharmProjects/pythonProject$ 
'''
'''NO TERMINAL
(venv) thainaarodrigues@penguin:~/PycharmProjects/pythonProject$ python3 aula-8-passagem-de-argumentos.py soma 1234 627
1234627
(venv) thainaarodrigues@penguin:~/PycharmProjects/pythonProject$ python3 aula-8-passagem-de-argumentos.py soma 1234 627
1861.0
(venv) thainaarodrigues@penguin:~/PycharmProjects/pythonProject$ python3 aula-8-passagem-de-argumentos.py sub 300 223.1
76.9
(venv) thainaarodrigues@penguin:~/PycharmProjects/pythonProject$ 
'''