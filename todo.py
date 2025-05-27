
class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

# Criado Por Pedro Lima
    def adicionar_tarefa(self, descricao):
        if not descricao:
            raise ValueError("Descrição da tarefa não pode ser vazia.")
        self.tarefas.append({"descricao": descricao, "concluida": False})

# Criado Por Pedro Siqueira
    def concluir_tarefa(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            raise IndexError("Índice inválido.")
        self.tarefas[indice]["concluida"] = True