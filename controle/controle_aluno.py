from model.model_aluno import aluno_model
from view.pagina_cadastro_aluno import cadastro

class aluno_controle:

    def __init__(self):
          self.model = aluno_model()
          self.view = cadastro()
    
    def salvando_aluno(self):
         nome, idade, peso = self.view.obter_dados_aluno()
         self.model.gravar_aluno(nome,idade,peso)
         self.view.mostrarmensagem("ALUNO CADASTRADO COM SUCESSO! ")
