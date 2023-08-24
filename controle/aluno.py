from model.aluno import aluno
from view.paginaCadastro import cadastro
class aluno:
    def __init__(self):
        self.model = aluno()
        self.view = cadastro()

    def salvarAluno(self):
        nome,idade,peso = self.view.criarAluno()
        self.model.salvarAluno(nome,idade,peso)
        self.view.mostrarMessagem("Aluno Salvo com Sucesso!")