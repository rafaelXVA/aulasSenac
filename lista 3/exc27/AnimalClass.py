class Animal:
    def __init__(self,movimento):
        self.movimento=movimento
    def como(self):
        test=int(input('1-peixe\n2-cachorro\n3-águia'))
        if test==1:
            self.movimento='nada'
            print(f'o peixe {self.movimento}')
        elif test==2:
            self.movimento='corre'
            print(f'o cachorro {self.movimento}')
        elif test==3:
            self.movimento='voa'
            print(f'a águia {self.movimento}')