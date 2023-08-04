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
            [Text(f'Seja bem-vindo {nome}')],
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
            [Input(key='-APOSTA-')],
            [Button('Apostar')],
            [Text(f'Você tem 6 chances para acertar.')],
        ]
    return Window('Aposta', layout=layout, finalize=True)

def janela_erro_aposta():
    theme('DarkPurple')
    layout = [
            [Text('Você precisa apostar em números inteiros e que estejam dentro do intervalo!')],
            [Button('Próxima aposta'), Button('Cancelar')],
        ]
    return Window('Erro - Aposta', layout=layout, finalize=True)

def janela_erro_intervalo():
    sg.theme('DarkPurple')
    layout = [
            [sg.Text('Você precisa digitar dois números inteiros para prosseguir com o jogo!')],
            [sg.Button('Próxima aposta'), sg.Button('Cancelar')],
        ]
    return sg.Window('Erro - Intervalo', layout=layout, finalize=True)

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
            Janela_3 = janela_aposta()
            janela_2.hide()
        case 'Apostar':
            popup('Um pouco mais!')
    

