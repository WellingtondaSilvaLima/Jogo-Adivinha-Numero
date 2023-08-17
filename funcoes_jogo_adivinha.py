import random as rd
from PySimpleGUI import *

def ranking(pontos, chances):
    match chances:
        case 6:
            pontos += 50
            return pontos
        case 5:
            pontos += 40
            return pontos
        case 4:
            pontos += 40
            return pontos
        case 3:
            pontos += 20
            return pontos
        case 2:
            pontos += 20
            return pontos
        case 1:
            pontos += 10
            return pontos
        case 0:
            pontos += 0
            return pontos
        case _:
            return 'Error'
    



# Verifica o intervalo
def verificacao_intervalo(escolha):
    match escolha:
        case '-FACIL-':
            intervalo = [1, 10]
        case '-NORMAL-':
            intervalo = [1, 50]
        case '-DIFICIL-':
            intervalo = [1, 100]

    return intervalo

# Verifica se a aposta feita é válida e se está dentro do intervalo
def verificacao_aposta(aposta, inicio, fim):
    while not(aposta.isdigit()) or int(aposta) < inicio or int(aposta) > fim:
        print('Você precisa apostar em números inteiros e que estejam dentro do intervalo!')
        aposta = input('Adivinhe o número: ')

    return int(aposta)

# Chama a lógica do jogo
def jogar():
    intervalo = verificacao_intervalo()
    inicio = intervalo[0]
    fim = intervalo[1]
    
    numero_escolhido = rd.randint(inicio, fim)

    limite_de_jogadas = 1
    while limite_de_jogadas <= 6:
        print('\n')
        print('='*50)
        aposta = input('Adivinhe o número: ')

        aposta_verificada = verificacao_aposta(aposta, inicio, fim)
        
        if aposta_verificada == numero_escolhido:
            return print('\n\n', '|'*50, '\n', 'Parabéns! Você venceu!',  '\n', '|'*50, '\n\n')
        elif aposta_verificada < numero_escolhido:
            print('\n')
            print('Um pouco mais!')
            limite_de_jogadas += 1
        elif aposta_verificada > numero_escolhido:
            print('\n')
            print('Um pouco menos!')
            limite_de_jogadas += 1

    return print('Você atingiu o limite de jogadas!', '\n', 'Você perdeu!')
