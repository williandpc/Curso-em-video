def LeiaDinheiro():

    num = str(v)
    while not num.isnumeric():
        print(f'\033[31mERRO: "{num}" é um preço inválido!\033[m')
    return num
