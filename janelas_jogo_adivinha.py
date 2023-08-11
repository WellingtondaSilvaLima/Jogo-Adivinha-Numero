from PySimpleGUI import *
from funcoes_jogo_adivinha import *
import random as rd

'''
def janela_apresentacao():    
    theme('DarkPurple')
    layout = [
            [Image()],
            [Button('Ranking'), Button('Jogar'), Button('Parar')],
        ]
    
    return Window(
        'Jogo Adivinha o Número',
        layout=layout,
        finalize=True,
        element_justification='c',
        size=(400, 150)
        )
'''

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

def janela_aposta(chances):
    theme('DarkPurple')
    layout = [
        [Text('Vamos iniciar o jogo?')],
        [Text('Sua aposta é:')],
        [Input(key='-APOSTA-', size=(20))],
        [Button('Apostar')],
        [Text(f'Você terá 6 chances para acertar.', key='-CHANCE-')],
        ]
    
    return Window(
        'Jogo Adivinha o Número',
        layout=layout,
        finalize=True,
        element_justification='c',
        size=(400, 150)
        )

def janela_vencedor(nome):
    theme('DarkPurple')
    layout = [
        [Text(f'Parabéns {nome}, você venceu!')],
        [Button('Reiniciar'), Button('Parar')],
        ]
    
    return Window(
        'Jogo Adivinha o Número',
        layout=layout,
        finalize=True,
        element_justification='c',
        size=(400, 150)
        )

def janela_perdedor(nome):
    theme('DarkPurple')
    layout = [
        [Text(f'Que pena {nome}, você perdeu!')],
        [Button('Reiniciar'), Button('Parar')],
        ]
    
    return Window(
        'Jogo Adivinha o Número',
        layout=layout,
        finalize=True,
        element_justification='c',
        size=(400, 150)
        )


chances = 6

janela_1 = janela_inicial()
janela_2 = None
janela_3 = None
janela_4 = None
janela_5 = None

while True:
    window, event, values = read_all_windows()    

    match event:
        case 'Começar':
            janela_2 = janela_bem_vindo(values['-NOME-'])
            nome = values['-NOME-']
            janela_1.close()
        case 'Enviar':
            janela_3 = janela_aposta(chances)

            if values['-FACIL-']:
                intervalo = verificacao_intervalo('-FACIL-')
            elif values['-NORMAL-']:
                intervalo = verificacao_intervalo('-NORMAL-')
            elif values['-DIFICIL-']:
                intervalo = verificacao_intervalo('-DIFICIL-')
            else:
                janela_3.close()
                popup('Erro! Escolha uma opção')
                continue

            inicio = intervalo[0]
            fim = intervalo[1]
            numero_escolhido = rd.randint(inicio, fim)
            
            janela_2.close()
        case 'Apostar':
            aposta = values['-APOSTA-']
            

            if not(aposta.isdigit()) or int(aposta) < inicio or int(aposta) > fim:
                popup('Você precisa apostar em números inteiros e que estejam dentro do intervalo!')
                continue

            
            if int(aposta) == numero_escolhido:
                janela_3.close()
                janela_4 = janela_vencedor(nome)
            elif int(aposta) < numero_escolhido:
                popup('Um pouco mais!')
                chances -= 1
                
                if chances == 0:
                    janela_5 = janela_perdedor(nome)
                    janela_3.hide()
                
                window['-CHANCE-'].update(f'Você terá {chances} chances para acertar.')
                window['-APOSTA-'].update('')
                continue
            elif int(aposta) > numero_escolhido:
                popup('Um pouco menos!')
                chances -= 1
                
                if chances == 0:
                    janela_5 = janela_perdedor(nome)
                    janela_3.hide()
                
                window['-CHANCE-'].update(f'Você terá {chances} chances para acertar.')
                window['-APOSTA-'].update('')
                continue
        case 'Reiniciar':
            chances = 6
            if not(janela_4 == None):
                janela_4.close()
            if not(janela_5 == None):
                janela_5.close()
            janela_2 = janela_bem_vindo(nome)
        case 'Parar':
            break
        
        case None:
            break
    



















           
    

