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

    for id_posicao in dados:
        tabela_ranking.append([dados[id_posicao]['nome'], dados[id_posicao]['pontos']])
    
    tabela_tratada = select_sort(tabela_ranking)
    
    return tabela_tratada
    

def select_sort(tabela_ranking):
    for indice in range(len(tabela_ranking)):
        indice_minimo = indice
        for indice_2 in range(indice + 1, len(tabela_ranking)):
            if tabela_ranking[indice_minimo][1] < tabela_ranking[indice_2][1]:
                indice_minimo = indice_2
        tabela_ranking[indice], tabela_ranking[indice_minimo] = tabela_ranking[indice_minimo], tabela_ranking[indice]

    
    return tabela_ranking

def ordena_ranking(dados):
    tabela_tratada = cria_tabela_ranking(dados)
    tabela_ordenada = []
    posicao = 1

    for id_posicao in range(len(tabela_tratada)):
        tabela_ordenada.append([posicao, tabela_tratada[id_posicao][0], tabela_tratada[id_posicao][1]])
        posicao += 1
        
    return tabela_ordenada







# SDG

