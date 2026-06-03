def soma_elementos(lista):
    soma = 0

    for numero in lista:
        soma += numero

    return soma


numeros = [1, 2, 3, 4, 5]
print("Soma:", soma_elementos(numeros))