class Funcionario:
    def __init__(self,salario,nome):
        self.salario=salario
        self.nome=nome
    def aumento(self,porcentagem):
        self.salario=self.salario+(self.salario*(porcentagem/100))
        print(f'{self.salario}')
        return self.salario