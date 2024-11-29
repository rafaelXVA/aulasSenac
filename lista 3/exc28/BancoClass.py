class Banco:
    def __init__(self,saldo,id):
        self.saldo=saldo
        self.id=id
    def mostrar(self):
        id1={self.id: 1, self.saldo:100}
        id2={self.id:2,self.saldo:200}
        id3={self.id:3,self.saldo:150}
        banco={id1: 'id1',id2:'id2',id3:'ide3'}
        print(banco[id1,id2,id3])