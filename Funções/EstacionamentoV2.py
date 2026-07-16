from cadastro import cadastro
from menu import menu
from listar import listar
from saida import saida
carros=[]
while True:
    alternativa=menu('Digite o que Você deseja: ')
    if alternativa=='A':
        cadastro(carros)
    elif alternativa=='L':
        listar(carros)
    elif alternativa=='X':
            saida(carros)
            break
                             #chame a opcao cadastro com if

