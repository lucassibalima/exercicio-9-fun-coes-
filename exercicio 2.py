def e_palindromo(texto):
    texto_invertido = texto[::-1]

    if texto == texto_invertido:
        return True
    else:
        return False


palavra = input("Digite uma palavra: ")

if e_palindromo(palavra):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")