from Classes import Retangulo
import os


comprimento=int(input('comprimento: '))
largura=int(input('largura: '))

retangulo1=Retangulo(largura,comprimento)

piso=int(input('tamanho do piso ao quadrado: '))
os.system('cls')
test=input('deseja mudar o tamanho? (Y/N)')
if test=='Y':
    comprimento2=int(input('novo comprimento: '))
    largura2=int(input('nova largura: '))
    retangulo1=Retangulo.mudar_lados(retangulo1,comprimento2,largura2)
else:
    pass
Retangulo.mostrar_lado(retangulo1)