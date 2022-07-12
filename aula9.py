''' Orientação a Objetos - é um paradigma procedamental, você diz o que
é pra fazer e o programa vai executar. Você define o que vai ter e cria
os objetos. Geralmente são criados vários arquivos '''

# Representação de um carro no python
# Um objeto sempre vai ter 2 coisas, características e funções/métodos

'''CLASSE - descreve o objeto
OBJETO - criação de um objeto real através da classe '''

class Veiculo:  # classe normalmente se inicia com letra maiuscula
    # init é o método construtor, constroi um objeto. Self sempre fica dentro

    def __init__(self, cor, rodas, marca):
        self.cor = cor  # A cor do objeto agora é o que definir
        self.rodas = rodas
        self.marca = marca