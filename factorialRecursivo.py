

def main():
    numero = int(input('Ingresa el numero para sacar factorial: \n'))
    res = factorialDe(int(numero))
    print("El factorial de " + str(numero) + ' es = ' + str(res))


def factorialDe(numero):
    if numero is 0:
        return 1
    resultado = numero * factorialDe(numero - 1)
    return resultado


if __name__ == "__main__":
    main()
