import PySimpleGUI as sg

def janela_inicial():
    sg.theme('Reddit')
    layout = [
            [sg.Text('Digite seu nome:')],
            [sg.Input(key='nome')],
            [sg.Button('Começar')],
        ]
    return sg.Window('Jogo Adivinha o Número', layout=layout, finalize=True)

def janela_bem_vindo(nome):
    sg.theme('Reddit')
    layout = [
            [sg.Text(f'Seja bem-vindo {nome}')],
            [sg.Text('Escolha o início e o fim do intervalo:')],
            [sg.Input(key='inicio'), sg.Input(key='fim')],
            [sg.Button('Enviar')],
        ]
    return sg.Window('Bem-vindo! Boa sorte!', layout=layout, finalize=True)

def janela_aposta(nome, chances):
    sg.theme('Reddit')
    layout = [
            [sg.Text(f'Boa sorte {nome}! Vamos iniciar o jogo?')],
            [sg.Text('Sua aposta é:')],
            [sg.Input(key='aposta')],
            [sg.Button('Enviar')],
            [sg.Text(f'Você tem {chances} chances para acertar.')],
        ]
    return sg.Window('Aposta', layout=layout, finalize=True)

def janela_dica_mais():
    sg.theme('Reddit')
    layout = [
            [sg.Text('Um pouco mais!')],
            [sg.Button('Próxima aposta'), sg.Button('Cancelar')],
        ]
    return sg.Window('Dica: Mais', layout=layout, finalize=True)

def janela_dica_menos():
    sg.theme('Reddit')
    layout = [
            [sg.Text('Um pouco menos!')],
            [sg.Button('Próxima aposta'), sg.Button('Cancelar')],
        ]
    return sg.Window('Dica: Menos', layout=layout, finalize=True)

def janela_erro_aposta():
    sg.theme('Reddit')
    layout = [
            [sg.Text('Você precisa apostar em números inteiros e que estejam dentro do intervalo!')],
            [sg.Button('Próxima aposta'), sg.Button('Cancelar')],
        ]
    return sg.Window('Erro - Aposta', layout=layout, finalize=True)

def janela_erro_intervalo():
    sg.theme('Reddit')
    layout = [
            [sg.Text('Você precisa digitar dois números inteiros para prosseguir com o jogo!')],
            [sg.Button('Próxima aposta'), sg.Button('Cancelar')],
        ]
    return sg.Window('Erro - Intervalo', layout=layout, finalize=True)

def janela_venceu():
    sg.theme('Reddit')
    layout = [
            [sg.Text('Parabéns! Você venceu')],
            [sg.Button('Jogar novamente'), sg.Button('Cancelar')],
        ]
    return sg.Window('Parabéns', layout=layout, finalize=True)

def janela_perdeu():
    sg.theme('Reddit')
    layout = [
            [sg.Text('Que pena! Você perdeu')],
            [sg.Button('Jogar novamente'), sg.Button('Cancelar')],
        ]
    return sg.Window('Que pena!', layout=layout, finalize=True)

janela_1, janela_2 = janela_inicial(), None

while True:
    window, event, values = sg.read_all_windows()

    if window == janela_1 and event == sg.WINDOW_CLOSED:
        break
