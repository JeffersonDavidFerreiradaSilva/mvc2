from model.m_aluno import m_aluno
from view.p_aluno import p_aluno

class c_aluno:
    def __init__(self):
        self.model = m_aluno()
        self.view = p_aluno()
    
    def gravarAluno (self):
        nome,idade,peso = self.view.pegar_dados_aluno()
        self.model.salvarAluno(nome,idade,peso)
        self.view.mostrarMessagem("Aluno salvo com sucesso! ")