class Calculadora:
    def __init__(self):
        self.historico=[]
    def cal(self):
        while True:
            n1=int(input('número 1: '))
            n2=int(input('número 2: '))
            res=n1+n2
            self.historico.append(res)
            print(self.historico)