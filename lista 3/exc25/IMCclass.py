class IMC:
    def __init__(self,peso: float,altura:float):
        self.peso=peso
        self.altura=altura
    def imc(self):
        print(self.peso/(self.altura**2))
