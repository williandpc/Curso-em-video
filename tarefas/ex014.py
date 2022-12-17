###Exercício Python 14: Escreva um programa que converta uma temperatura digitando
# em graus Celsius e converta para graus
temp = float(input('Digite a temperatura que deseja converter, em °C:'))
f = (temp * 9/5) + 32
print(f'{temp}°C em °F é igual à {f}°F')