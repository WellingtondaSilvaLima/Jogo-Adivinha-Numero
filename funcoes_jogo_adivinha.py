from database_ranking import *


# Define a pontuação por rodada
def pontuacao(chances):
    pontos = 0
    
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

def cria_tabela_ranking(dados):
    tabela_ranking = []
    posicao = 1

    for id_posicao in dados:
        tabela_ranking.append([posicao, dados[id_posicao]['nome'], dados[id_posicao]['pontos']])
        posicao += 1

    return tabela_ranking
    








# SDG

