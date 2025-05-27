
import unittest
from todo import ListaDeTarefas

class TesteListaDeTarefas(unittest.TestCase):
    def setUp(self):
        self.lista = ListaDeTarefas()

    def test_adicionar_tarefa(self):
        self.lista.adicionar_tarefa("Estudar para a prova")
        self.assertEqual(len(self.lista.tarefas), 1)



if __name__ == '__main__':
    unittest.main()
