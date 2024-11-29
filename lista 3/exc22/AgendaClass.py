class Agenda:
    def __init__(self):
        self.contatos = []
    def adicionar(self):
        tel=input('telefone: ')
        nome=input('nome: ')
        contato={'nome': nome, 'telefone': tel}
        self.contatos.append(contato)
    def listar(self):
        for contato in self.contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")
