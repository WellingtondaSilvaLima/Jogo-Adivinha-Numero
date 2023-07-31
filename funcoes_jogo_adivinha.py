import random as rd
import PySimpleGUI as sg

# Verifica se os números digitados são inteiros
def verificacao_intervalo():
    inicio = input('Digite o início do intervalo: ')
    fim = input('Digite o final do intervalo: ')
    
    while not(inicio.isdigit()) or not(fim.isdigit()):
        print('\n')
        print('*'*50)
        print('Você precisa digitar dois números inteiros para prosseguir com o jogo!')
        inicio = input('Digite o início do intervalo: ')
        fim = input('Digite o final do intervalo: ')

    intervalo = [int(inicio), int(fim)]
    return intervalo

# Verifica se a aposta feita é válida e se está dentro do intervalo
def verificacao_aposta(aposta, inicio, fim):
    while not(aposta.isdigit()) or int(aposta) < inicio or int(aposta) > fim:
        print('\n')
        print('*'*50)
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
