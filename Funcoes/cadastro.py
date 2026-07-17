import os
from datetime import datetime

atual=datetime.now()
estacionamento_att=atual.strftime('%d-%m-%y')+ '.dat'

def cadastro(carros=list):
    try:
        fabricante=input('Fabricante: ').upper().strip()
        os.system("cls")
        Modelo=input('Modelo Do Veiculo: ').upper().strip()
        os.system("cls")
        Placa=input('Placa do Veiculo: ').upper().strip()
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
   
           
