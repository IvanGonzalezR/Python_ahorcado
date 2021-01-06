import random


def main():
    ejecutaBucle()


def ejecutaBucle():
    numero_random = random.randint(1, 1000)
    res = int(input('Intenta adivinar el numero, basofia :v'))
    es_verdadero = False

    while not es_verdadero:
        if res == numero_random:
            print('Eres la mamada, hijo...')
            es_verdadero = True
        elif res < numero_random:
            res = int(input('Mas arriba we: '))
        elif res > numero_random:
            res = int(input('Mas abajo we nmms: '))


if __name__ == "__main__":
    main()
