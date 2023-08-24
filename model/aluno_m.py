import pymysql.cursors

class aluno:
    def __init__(self):
        self.conexao = pymysql.connect(
            host = "localhost",
            user = "root",
            passaword = "@Cursos21",
            database = "serpro",
            cursorclass=pymysql.cursors.DictCursor
        )
        
    def salvarAluno(self,nome,idade,peso):
        try:
            with self.conexao.cursor() as cursor:
                mysql = "INSERT INTO tb_alunos (nome, idade,peso) VALUES (%s,%s,%s)"
                valores = (nome, idade, peso)
                cursor.execute(mysql,valores)
            self.conexao.commit()
        finally:
            self.conexao.close()