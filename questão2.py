
def percorrer_caminho(caminho_puffle, energia, moedas, itens_raros):
    if(energia <= 0):
        print('Ah, cansei. Vou descansar.')
        resultado_final(moedas, itens_raros)
        return

    if(not caminho_puffle):
        resultado_final(moedas, itens_raros)
        return

    caminho = caminho_puffle[0]
    if(caminho.isnumeric()):
        moedas += int(caminho)
        energia -= 1
    elif(caminho == 'X'):
        energia -= 1
    else:
        print(f'Oba! Encontrei um {caminho} 🐧🎉')
        energia -= 1
        itens_raros += 1
        energia += 2
    return percorrer_caminho(caminho_puffle[1:], energia, moedas, itens_raros)

def resultado_final(moedas, itens_raros):
    if(moedas == 0 and itens_raros == 0):
        print('Essa caminhada não foi nada produtiva. É melhor ir pescar.')
    elif(moedas > 0 and itens_raros == 0):
        print(f'Estamos ricos!! Encontrei {moedas} moedas.')
    elif(moedas == 0 and itens_raros > 0):
        print(f'Dinheiro? Não temos. Mas temos {itens_raros} itens raros.')
    else:
        print(f'Quem diria!! {moedas} moedas e {itens_raros} itens raros. Hoje eu mereço bolo, não aqueles puffitos de sempre.')

caminho_puffle = input().split(', ')
energia = 4
moedas = 0
itens_raros = 0
percorrer_caminho(caminho_puffle, energia, moedas, itens_raros)