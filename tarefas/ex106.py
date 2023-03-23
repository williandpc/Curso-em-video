from time import sleep


def pyhelp():
    comando = ''
    while True:
        print('\033[01:42m~' * 30)
        print("SISTEMA DE AJUDA PyHELP".center(30))
        print('~' * 30)
        print('\033[m')
        comando = input('\033[mFunção ou Biblioteca > ')
        if comando.upper() == 'FIM':
            print('\033[01:41m~' * 10)
            print("ATÉ LOGO".center(10))
            print('~' * 10)
            break
        print('\033[01:44m~' * 50)
        print(f"Acessando o manual do comando '{comando}'".center(50))
        print('~' * 50)
        sleep(1)
        print('\033[07:30m')
        help(comando)
        sleep(1)
        print('\033[m')



pyhelp()
