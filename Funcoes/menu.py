def menu(option):
    while True:
     tamanho=len('SISTEMA DE ESTACIONAMENTO')
     print('='*(tamanho+4))
     print('  SISTEMA DE ESTACIONAMENTO')
     print('='*(tamanho+4))
     print('''[A] PARA ADICIONAR UM NOVO CARRO
[L] PARA LISTAR OS CARROS ESTACIONADOS
[X] SAIR  
[B] PARA BUSCAR POR PLACA''')
     opcao=str(input(option)).strip().upper()
     if opcao in ('A','L','X','B'):   
      return opcao
     print('\n ERRO! DIGITE APENAS A, L, B ou X.\n')