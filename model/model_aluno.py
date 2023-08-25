import sqlite3

class aluno_model:
    def __init__(self):
        # Inicializa a conexão com o banco de dados SQLite (ou cria o arquivo se não existir)
        self.conexao = sqlite3.connect('banco_de_dados')
        self.cursor = self.conexao.cursor()
        # Cria a tabela students se ela não existir
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tb_alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER,
                peso REAL
            )
        ''')
        self.conexao.commit()

    def gravar_aluno(self, nome, idade, peso):
        self.cursor = self.conexao.cursor()
        self.cursor.execute("INSERT INTO tb_alunos (nome, idade, peso) VALUES (?,?,?)", (nome, idade, peso))
        self.conexao.commit()
        
        
    def lista_alunos(self):
        alunos = self.cursor.execute("SELECT * FROM tb_alunos").fetchall()
        for aluno in alunos:
            print(aluno)
        return alunos
    


    def close(self):
        self.conexao.close()
