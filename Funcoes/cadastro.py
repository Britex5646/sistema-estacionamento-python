import os
from datetime import datetime

atual=datetime.now()
estacionamento_att=atual.strftime('%H-%M-%S')+ '.dat'

def cadastro(carros):
    try:
        fabricante=input('Fabricante: ')
        os.system("cls")
        Modelo=input('Modelo Do Veiculo: ')
        os.system("cls")
        Placa=input('Placa do Veiculo: ')
        os.system("cls")           
        carro={
        'fabricante': fabricante,
        'modelo': Modelo,
        'placa': Placa 
     }
        carros.append(carro)
        hora=datetime.now()
        horacar=hora.strftime('%H;%M')
        with open (estacionamento_att,'a') as estacionamento:
                estacionamento.write(f"{carro['placa']};{carro['modelo']};{carro['fabricante']};{horacar}\n")
    except KeyboardInterrupt:
        print('O usuário não finalizou o Cadadstro')
    else:
        print('Cadastro de Veiculo feito.')
   
           
