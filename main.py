from controle.controle_aluno import aluno_controle
from model.model_aluno import aluno_model

if __name__ == "__main__":
       
    controle = aluno_controle()
    controle.salvando_aluno()
    listagem =aluno_model()
    listagem.lista_alunos()