from images import IMAGES
from utils import clear

intentos = 0


def main():
    es_una_letra = False
    juego_terminado = False
    global IMAGES
    global intentos

    clear()
    print("JUEGO DEL AHORCADO!!!!\n")
    # INPUT DE LOS DATOS
    frase_ingresada = input(
        'Ingresa la palabra o frase a utilizar (No se lo cuentes a nadie!!!)\n').lower().strip()
    # CREACION DE LISTA EN MINUSCULAS DEL INPUT Y SIN ESPACIOS A LOS LADOS
    frase_ingresada_lista = list(frase_ingresada.lower().strip())

    print(frase_ingresada_lista)
    print('\nAdivina la palabra o frase (Si puedes...)')

    progreso = ['_'] * len(frase_ingresada_lista)
    print(progreso)
    clear()

    # PEDIR UNA LETRA, SI SON MAS DE UNA, VOLVER A PEDIRLA
    while es_una_letra is False or juego_terminado is False:

        print(IMAGES[intentos])
        print(progreso)
        letra = input('\nIngresa SOLO UNA letra...: ').strip().lower()
        if len(letra) == 1:
            progreso = verifica_letra(letra, frase_ingresada, progreso)
            es_una_letra = True
            try:
                progreso.index('_') == -1
            except ValueError:
                juego_terminado = True
                print('FELICIDADES, ENCONTRASTE LA FRASE ESCONDIDA!!!')
                break
            if intentos == 6:
                juego_terminado == True
                print('No has encontrado la frase escondida, FIN DEL JUEGO!')
                break
        clear()
    # lista_indices = verificaLetra(letra, frase_ingresada)
    # print(lista_indices)


intentos = 0


def verifica_letra(letra, lista_cadena, progreso):
    """
    """
    indice = []  # INDICES A REGRESAR
    cadena = "".join(lista_cadena)  # CADENA JNTA
    size_cadena = len(cadena)  # TAMANO DE LA CADENA

    for i in range(size_cadena):  # BUSCAR LA LETRA EN EL STRING
        # AGREGAR LOS INDICES DONDE LA LETRA OCURRE
        if lista_cadena[i] == letra:
            indice.append(i)
            # SUSTITUIR ESPACIOS POR
        if lista_cadena[i] == ' ':
            progreso[i] = 0

    if len(indice) != 0:
        for i in range(len(indice)):
            progreso[indice[i]] = letra

    global intentos
    # AUMENTAR LA VARIABLE DE LOS ERRORES ACTUALES
    if len(indice) == 0:
        intentos += 1

    # print(progreso)

    return progreso


if __name__ == "__main__":
    main()
