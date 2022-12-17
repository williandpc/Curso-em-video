# ##Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
name = str(input("Digita seu nome completo: ")).strip()
print(f"Seu nome contem 'Silva'? {'SILVA' in name.upper()}")