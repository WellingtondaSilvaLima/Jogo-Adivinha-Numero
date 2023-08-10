from PySimpleGUI import *
from funcoes_jogo_adivinha import *
import random as rd

def janela_inicial():    
    theme('DarkPurple')
    layout = [
            [Text('Digite seu nome:')],
            [Input(key='-NOME-')],
            [Button('Começar')],
        ]
    
    return Window(
        'Jogo Adivinha o Número',
        layout=layout,
        finalize=True,
        element_justification='c',
        size=(400, 150)
        )

def janela_bem_vindo(nome):
    theme('DarkPurple')
    layout = [
            [Text(f'Seja bem-vindo {nome}!')],
            [Text('Escolha o nível do jogo')],
            [Radio('1 a 10 - Fácil', 'dificuldade', key='-FACIL-'),
             Radio('1 a 50 - Normal', 'dificuldade', key='-NORMAL-'),
             Radio('1 a 100 - Difídil', 'dificuldade', key='-DIFICIL-')],
            [Button('Enviar')],
            [Text('Você terá 6 chances para acertar.')],
        ]
    
    return Window(
        'Jogo Adivinha o Número',
        layout=layout,
        finalize=True,
        element_justification='c',
        size=(400, 150)
        )

def janela_aposta():
    theme('DarkPurple')
    layout = [
        [Text('Vamos iniciar o jogo?')],
        [Text('Sua aposta é:')],
        [Input(key='-APOSTA-', size=(20))],
        [Button('Apostar')],
        ]
    
    return Window(
        'Jogo Adivinha o Número',
        layout=layout,
        finalize=True,
        element_justification='c',
        size=(400, 150)
        )



janela_1 = janela_inicial()

while True:
    window, event, values = read_all_windows()

    match event:
        case 'Começar':
            janela_2 = janela_bem_vindo(values['-NOME-'])
            janela_1.hide()
        case 'Enviar':
            janela_3 = janela_aposta()

            if values['-FACIL-']:
                intervalo = verificacao_intervalo('-FACIL-')
            elif values['-NORMAL-']:
                intervalo = verificacao_intervalo('-NORMAL-')
            elif values['-DIFICIL-']:
                intervalo = verificacao_intervalo('-DIFICIL-')
            else:
                janela_3.hide()
                popup('Erro! Escolha uma opção')
                continue

            inicio = intervalo[0]
            fim = intervalo[1]
            numero_escolhido = rd.randint(inicio, fim)
            
            janela_2.hide()
        case 'Apostar':
            aposta = values['-APOSTA-']
            

            if not(aposta.isdigit()) or int(aposta) < inicio or int(aposta) > fim:
                popup('Você precisa apostar em números inteiros e que estejam dentro do intervalo!')
                continue

            
            if int(aposta) == numero_escolhido:
                popup('Parabéns! Você venceu!')
                break
            elif int(aposta) < numero_escolhido:
                popup('Um pouco mais!')
                window['-APOSTA-'].update('')
                continue
            elif int(aposta) > numero_escolhido:
                popup('Um pouco menos!')
                window['-APOSTA-'].update('')
                continue
            
        case None:
            break





















           
    

