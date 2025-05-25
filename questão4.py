def encontrar_senha():
    lista_cripitografada = input().split(', ')
    soma_da_senha = int(input())
    for indice in range(len(lista_cripitografada)):
        lista_cripitografada[indice] = int(lista_cripitografada[indice])
    passou = True
    copia_crip = lista_cripitografada[:]
    subconjuntos = criar_subconjuntos(copia_crip)
    senha = ['']
    for possivel_senha in subconjuntos:
        if (sum(possivel_senha) == soma_da_senha) and (len(possivel_senha) > len(senha)):
            senha = possivel_senha
    senha_nova = ''.join(map(str, senha))
    senha = list(senha_nova)
    while ('0' in senha or '-' in senha):
        if('0' in senha):
            senha.remove('0')
        if('-' in senha):
            senha.remove('-')
    if(len(senha) < 4):
        passou = False
    return passou, senha

def criar_subconjuntos(conjunto):
    sublistas = [[]] 
    for elemento in conjunto:
        novas = []
        for sub in sublistas:
            novas.append(sub + [elemento])  
        sublistas.extend(novas) 
    return sublistas

def verificar(qtd_portas, n_porta):
    passou, senha = encontrar_senha()
    n_porta += 1
    if(passou == False):
        return print('Não foi possível descobrir a senha dessa porta, Penguin Bond deve procurar outra entrada!')
    elif(n_porta == qtd_portas):
        return print(f"A senha da porta {n_porta} é: {''.join(senha)}")
    else:
        print(f"A senha da porta {n_porta} é: {''.join(senha)}")
        return verificar(qtd_portas, n_porta)
    
qtd_portas = int(input())
n_porta = 0
verificar(qtd_portas, n_porta)