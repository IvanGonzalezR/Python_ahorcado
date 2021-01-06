import math


def main():
    numbers = [1, 4, 2, 6, 5, 51, 27, 11, 9, 19, 25, 28, 34, 36, 49]
    print(numbers)
    ordenedNumbers = sorted(numbers)
    print(ordenedNumbers)
    numero = int(input('Ingresa el numero a buscar: \n'))
    buscaNumero(ordenedNumbers, numero, 0, len(ordenedNumbers) - 1)


def buscaNumero(listaNumeros, numero, low, high):

    if low > high:
        print('numero no encontrado...')
        return

    indice = int((low + high) / 2)

    if listaNumeros[indice] == numero:
        print('numero encontrado: ')
        print(numero)
        return

    if numero > listaNumeros[indice]:
        buscaNumero(listaNumeros, numero, indice + 1, high)

    elif numero < listaNumeros[indice]:
        buscaNumero(listaNumeros, numero, low, indice - 1)


if __name__ == "__main__":
    main()
