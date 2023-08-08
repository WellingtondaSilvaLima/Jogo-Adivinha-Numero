from PySimpleGUI import *
from funcoes_jogo_adivinha import *

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
            [Text(f'Você tem 6 chances para acertar.')],
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
        case None:
            break
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
            
            janela_2.hide()
        case 'Apostar':
            
            popup('Um pouco mais!')
    

