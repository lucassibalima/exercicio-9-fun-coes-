def maior_elemento(lista):
    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior


numeros = [10, 5, 30, 8, 15]
print("Maior elemento:", maior_elemento(numeros))