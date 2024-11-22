class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor=cor
        self.circunferencia=circunferencia
        self.material=material
    def troca_cor(self,cor2):
        self.cor=cor2
    def mostra_cor(bola):
        print(bola.cor)

class Quadrado:
    def __init__(self,Tlado):
        self.Tlado=Tlado
    def mostrar_area(self):
        print(self.Tlado*self.Tlado)
    def mudar_lado(self,lado2):
        self.Tlado=lado2
class Retangulo:
    def __init__(self,largura,comprimento):
        self.largura=largura
        self.comprimento=comprimento
    def mostrar_lado(retangulo):
        print('comprimento: ',retangulo.comprimento)
        print('largura: ',retangulo.largura)
    def mudar_lados(self,comprimento2,largura2):
        self.comprimento=comprimento2
        self.largura=largura2
    def area(self):
        print(self.largura*self.comprimento)
    def perimetro(self):
        print(self.largura+self.comprimento)