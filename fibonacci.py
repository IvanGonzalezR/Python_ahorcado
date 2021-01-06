//dsdsdsd
def main():
    # numero = int(input('Ingresa el n-esimo termino para fibonacci: '))
    # while numero <= 2:
    #     numero = int(input('Asegurate que sea mayor a 2: '))

    res = fibonacci(3)
    print(res)


def fibonacci(numero):
    if numero == 2 or numero == 1:
        return 1

    r1 = fibonacci(numero - 1)
    r2 = fibonacci(numero - 2)

    return (r1 + r2)


if __name__ == "__main__":
    main()
