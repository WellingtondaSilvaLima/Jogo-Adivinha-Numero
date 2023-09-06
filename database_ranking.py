import requests
import json

link = 'https://ranking-jogo-default-rtdb.firebaseio.com' 


# Criando uma posição do ranking
def nova_posicao(dados):
    global link
    
    requisicao = requests.post(f'{link}/Ranking/.json', data=json.dumps(dados))


def ler_ranking():
    global link
    dados = {}
    jogador = []
    pontuacao = []

    requisicao = requests.get(f'{link}/Ranking/.json')

    dicionario_requisicao = requisicao.json()

    return dicionario_requisicao


# SDG
