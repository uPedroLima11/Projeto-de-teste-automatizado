
class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        if not descricao:
            raise ValueError("Descrição da tarefa não pode ser vazia.")
        self.tarefas.append({"descricao": descricao, "concluida": False})

