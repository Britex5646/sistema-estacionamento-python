import os
carros=[]
def listar(carros):
    os.system("cls")

    for carro in carros:
     print(f"{carro['placa']} - {carro['modelo']}- {carro['fabricante']}")
    input('\nPressione < Enter > para voltar ao menu principal.')
    os.system("cls")




#listar

