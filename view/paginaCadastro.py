class cadastro:
    @staticmethod

    def criarAluno():
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        peso = float(input("Digite seu peso: "))
        return nome, idade, peso
    
    @staticmethod

    def mostrarMessagem(messagem):
        print(messagem)