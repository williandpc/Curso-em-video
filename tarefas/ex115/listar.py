def listar():
    try:
        with open("registro.txt", "r+") as registro:
            print(registro)
    except:
        print('registro inexistente, cadastre uma pessoa para começar')