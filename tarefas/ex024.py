# ##Exercício Python 24: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO"
city = input('Digite o nome da sua cidade: ')
city = city.split()
print(f'O nome da sua cidade começa com: {city[0]}')
print(f'Sua cidade começa com "Santo" no nome? {"SANTO" in city[0].upper()}')