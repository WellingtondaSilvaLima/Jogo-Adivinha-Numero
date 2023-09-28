from PySimpleGUI import *
from funcoes_jogo_adivinha import *
import random as rd
from database_ranking import *
from janelas_jogo_adivinha import *


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
                nivel = 'fácil'
            elif values['-NORMAL-']:
                intervalo = verificacao_intervalo('-NORMAL-')
                nivel = 'normal'
            elif values['-DIFICIL-']:
                intervalo = verificacao_intervalo('-DIFICIL-')
                nivel = 'difícil'
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
            
            pontos_ranking = pontuacao(chances, nivel)
            pontos_agora.append(pontos_ranking)
            
            chances = 6
            
            if not(janela_4 == None):
                janela_4.close()
            if not(janela_5 == None):
                janela_5.close()
            janela_2 = janela_bem_vindo(nome)
        case 'Parar':

            pontos_ranking = pontuacao(chances, nivel)
            pontos_agora.append(pontos_ranking)

            for pontos in range(len(pontos_agora)):
                pontos_somados += pontos_agora[pontos]

            if pontos_somados == 0:
                break
            else:
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
