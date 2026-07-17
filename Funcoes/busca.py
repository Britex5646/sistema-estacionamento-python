def busca(carros):
    placa=input('Digite a Placa do carro: ')
    for carro in carros:
        if placa== carro['placa']:
                print('Veículo Encontrado!')
                print(f"{carro['fabricante']}")
                print(f"{carro['modelo']}")    
                print(f"{carro['placa']}")    
                return
    print('Veiculo Não Encontrado')