
def main():
    negarBooleano(bool(False), 4)
    print(negarBooleano)


def negarBooleano(booleean, cantidad):
    if cantidad == 1:
        return (not booleean)

    bul = negarBooleano(bool(booleean), cantidad - 1)
    return bul


if __name__ == "__main__":
    main()
