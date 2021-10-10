def vogal(x):
    if x in ('a', 'e', 'i', 'o', 'u'):
        return print('True')
  
    else:
        print('False')


def main():
    letra = input('').lower()
    v = vogal(letra)


if __name__=='__main__':
    main()
