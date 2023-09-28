from PySimpleGUI import *

# Janela de início do jogo
def janela_apresentacao():    
    theme('DarkPurple')
    layout = [
            [Image(filename='logo.png')],
            [Button('Ranking'), Button('Jogar')],
        ]
    
    return Window(
        'Jogo Adivinha o Número',
        layout=layout,
        finalize=True,
        element_justification='c',
        size=(400, 300)
        )

# Janela que mostra os 10 melhores jogadores
def janela_ranking(dados, titulos):
    theme('DarkPurple')
    layout = [
            [Text('Classificação de Jogadores')],
            [Table(
                values=dados,
                headings=titulos,
                num_rows=10,
                hide_vertical_scroll=True,
                justification='center',
                expand_x=True,
                auto_size_columns =False)],
            [Button('Voltar')],
        ]
    
    return Window(
        'Jogo Adivinha o Número',
        layout=layout,
        finalize=True,
        element_justification='c',
        size=(400, 500)
        )

# Janela que pede o nome do participante
def janela_inicial():    
    theme('DarkPurple')
    layout = [
            [Text('Digite seu nome:')],
            [Input(key='-NOME-')],
            [Button('Começar')],
        ]
    
    return Window(
        'Jogo Adivinha o Número', # nome da janela
        layout=layout,
        finalize=True, # possibilita abrir várias janelas
        element_justification='c', # centraliza os elementos
        size=(400, 150) # define um tamanho para a janela
        )

# janela que pede para o jogador escolher o nível de dificuldade
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

# Janela que solicita o número que o jogador quer apostar
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

# Janela que aparece quando o jogador vence
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
        size=(250, 80)
        )

# Janela que aparece quando o jogador perde
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
        size=(250, 80)
        )











# SDG
