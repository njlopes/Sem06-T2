def consoante(x):
    if x in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
        return print('True')
  
    else:
        print('False')


def main():
    letra = input('').lower()
    c = consoante(letra)


if __name__=='__main__':
    main()
