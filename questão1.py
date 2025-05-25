def verificar_fibonacci(numero, lista_fibonacci):
    if(numero == lista_fibonacci[0]):
        return True
    elif(numero == lista_fibonacci[1]):
        return True
    elif(numero >  lista_fibonacci[-1]):
        novo_termo = lista_fibonacci[-1] + lista_fibonacci[-2]
        lista_fibonacci.append(novo_termo)
        return verificar_fibonacci(numero, lista_fibonacci)

qtd_numeros = int(input())
numeros_de_fibonacci = []

for i in range(qtd_numeros):
    lista_fibonacci = [0, 1]
    numero = int(input())
    verificar_fibonacci(numero, lista_fibonacci)

    if(numero in lista_fibonacci):
        numeros_de_fibonacci.append(numero)

print(f'Contei um total de {len(numeros_de_fibonacci)} números que estão na sequência de penguinacci!')

if(qtd_numeros == len(numeros_de_fibonacci)):
    print('Boa, Paulo! Todos esses números fazem parte da sequência de penguinacci.')
elif(len(numeros_de_fibonacci) > 0):
    print('Eita, nem todos que você falou fazem parte da sequência de penguinacci. Os que fazem parte são:')
    numeros_ordenados = sorted(numeros_de_fibonacci)
    numeros_str = []
    for num in numeros_ordenados:
        numeros_str.append(str(num))
    print(', '.join(numeros_str))
else:
    print('Acho que é melhor revisar a teoria um pouco...')
