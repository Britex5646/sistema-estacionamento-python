def menu(option):
    while True:
     tamanho=len('SISTEMA DE ESTACIONAMENTO')
     print('='*(tamanho+4))
     print('  SISTEMA DE ESTACIONAMENTO')
     print('='*(tamanho+4))
     print('''[A] PARA ADICIONAR UM NOVO CARRO
[L] PARA LISTAR OS CARROS ESTACIONADOS
[X] SAIR  ''')
     opcao=str(input(option)).strip().upper()
     if opcao in ('A','L','X'):   
        return opcao
     print('\n ERRO! DIGITE APENAS A, L ou X.\n')