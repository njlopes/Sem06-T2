def letra_numero(x):
    if x in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'):
        return print('True')
    if x in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return print('True')
    else:
        print('False')


def main():
    letra = input('').lower()
    ln = letra_numero(letra)


if __name__=='__main__':
    main()
