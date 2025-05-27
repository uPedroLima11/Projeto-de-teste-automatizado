import unittest
from todo import ListaDeTarefas

class TesteListaDeTarefas(unittest.TestCase):
    def setUp(self):
        self.lista = ListaDeTarefas()

    def test_adicionar_tarefa(self):
        self.lista.adicionar_tarefa("Estudar para a avaliação de Qualidade de Software")
        self.assertEqual(len(self.lista.tarefas), 1)

    def test_concluir_tarefa(self):
        self.lista.adicionar_tarefa("Comprar Notebook Novo para Faculdade")
        self.lista.concluir_tarefa(0)
        self.assertTrue(self.lista.tarefas[0]["concluida"])

if __name__ == '__main__':
    unittest.main()
