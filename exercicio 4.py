def contar_caracteres(texto, caractere):
    contador = 0

    for letra in texto:
        if letra == caractere:
            contador += 1

    return contador


frase = input("Digite uma frase: ")
caractere = input("Digite um caractere: ")

print("Quantidade:", contar_caracteres(frase, caractere))