import unittest
from unittest.mock import patch
from io import StringIO
from controle.controle_aluno import aluno_controle

class TestAlunoControle(unittest.TestCase):

    @patch('builtins.input', side_effect=["Alice", "25", "60.5"])
    def test_salvar_aluno(self, entrada_simulada):
        controle = aluno_controle()
        controle.salvando_aluno()
        
if __name__ == '__main__':
    unittest.main()