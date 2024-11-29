class Elevador:
    def __init__(self,andarAtual,totalAndares):
        self.andarAtual=andarAtual
        self.totalAndares=totalAndares
    def subir(self):
        return self.andarAtual+1
    def descer(self):
        return self.andarAtual-1