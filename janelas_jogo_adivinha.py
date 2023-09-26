from PySimpleGUI import *
from funcoes_jogo_adivinha import *
import random as rd
from database_ranking import *

# Janela de início do jogo
def janela_apresentacao():    
    theme('DarkPurple')
    layout = [
            [Image(filename='logo.png')],
            [Button('Ranking'), Button('Jogar'), Button('Parar')],
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
            [Button('Voltar'), Button('Jogar'), Button('Parar')],
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

# Define a quantidade de chances que o jogador tem
chances = 6

pontos_agora = []
pontos_somados = 0


janela_0 = janela_apresentacao()
janela_r = None
janela_1 = None
janela_2 = None
janela_3 = None
janela_4 = None
janela_5 = None

while True:
    window, event, values = read_all_windows()

    match event:
        case 'Voltar':
            janela_0 = janela_apresentacao()
            janela_r.hide()
        case 'Jogar':
            janela_1 = janela_inicial()
            janela_0.hide()
        case 'Começar':
            janela_2 = janela_bem_vindo(values['-NOME-'])

            # Salva o nome do jogador
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
            
            pontos_ranking = pontuacao(chances)
            pontos_agora.append(pontos_ranking)
            
            chances = 6
            
            if not(janela_4 == None):
                janela_4.close()
            if not(janela_5 == None):
                janela_5.close()
            janela_2 = janela_bem_vindo(nome)
        case 'Parar':

            pontos_ranking = pontuacao(chances)
            pontos_agora.append(pontos_ranking)

            for pontos in range(len(pontos_agora)):
                pontos_somados += pontos_agora[pontos]

            dados = {'nome': nome, 'pontos': pontos_somados}

            nova_posicao(dados)
            
            break
        case 'Ranking':
            titulos = ['Nº', 'NOME', 'PONTUAÇÃO']
            dados = ler_ranking()

            tabela_ranking = ordena_ranking(dados)
            
            janela_r = janela_ranking(tabela_ranking, titulos)
            janela_0.hide()
        case None:
            break
    














           
    
# SDG
