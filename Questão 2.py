def vogal_consoante(x):
    if x in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'):
        return print('True')
  
    else:
        print('False')


def main():
    letra = input('').lower()
    vc = vogal_consoante(letra)


if __name__=='__main__':
    main()
