from Media import Media
import os
med=Media
list=[]
os.system("cls")
while True:
    num=int(input("insira 0 para encerrar\ninsira numeros: "))
    list.append(num)
    os.system("cls")
    if num==0:
        break
med.Media(list)
