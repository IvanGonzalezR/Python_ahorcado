def main():
    palabra = input(
        'Ingresa una palabra/frase para verificar que sea palindromo: \n')
    if verificaPalindromo(palabra):
        print('La palabra/frase SI es un palindromo')
    else:
        print('La palabra/frase NO es un palindromo :(')


def verificaPalindromo(palabra):
    palabraVolteada = palabra.strip()
    palabraVolteada = palabraVolteada.replace(' ', '')
    palabraVolteada = palabraVolteada.lower()
    palabraVolteada = palabraVolteada[::-1]

    if palabraVolteada == palabra.replace(' ', ''):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
