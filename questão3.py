def separar_polinomio(polinomio):
    termos = polinomio.replace('-', '+-').split('+') # Alterar os termos com '-' por '+-' em seguida separar em uma lista pelos termos que possuem '+'.
    coeficientes = []
    expoentes = []

    for termo in termos:
        if('x^' in termo):
            coef, expoe = termo.split('x^')
        elif('x' in termo):
            coef, expoe = termo[:-1], '1'
        else:
            coef, expoe = termo, '0'
    
        if(coef == ''):
            coef = '1'
        elif(coef == '-'):
            coef = '-1'

        coeficientes.append(int(coef))
        expoentes.append(int(expoe))

    return coeficientes, expoentes

def derivar_polinomio(coeficientes, expoentes, ordem):
    if(ordem == 0):
        return coeficientes, expoentes
        
    novos_coeficientes = []
    novos_expoentes = []

    for i in range(len(coeficientes)):
        if(expoentes[i] > 0):
            novos_coeficientes.append(coeficientes[i] * expoentes[i])
            novos_expoentes.append(expoentes[i] - 1)
        else:
            novos_coeficientes.append(0)
            novos_expoentes.append(0)
    return derivar_polinomio(novos_coeficientes, novos_expoentes, ordem - 1)

def novo_polinomio(coeficientes, expoentes):
    resultado = []
    for i in range(len(coeficientes)):
        if(expoentes[i] == 0):
            if(coeficientes[i] != 0):
                resultado.append(f'{coeficientes[i]}')
        elif(expoentes[i] == 1):
            resultado.append(f'{coeficientes[i]}x')
        else:
            resultado.append(f'{coeficientes[i]}x^{expoentes[i]}')
    return '+'.join(resultado).replace('+-', '-')

polinomio = input()
ordem = int(input())

if('x' not in polinomio):
    print(f'A derivada de ordem {ordem} da função {polinomio} é:')
    print('0')
else:
    coeficientes, expoentes = separar_polinomio(polinomio)
    derivadas_coef, derivadas_exp = derivar_polinomio(coeficientes, expoentes, ordem)
    resultado = novo_polinomio(derivadas_coef, derivadas_exp)
    print(f'A derivada de ordem {ordem} da função {polinomio} é:')
    print(resultado)