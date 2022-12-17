###Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('insira o valor (em metros):'))
print(f'{m}m é igual à {m*100}cm \n'
      f' que tambem é igual à {m*1000}mm \n'
      f' que corresponde tambem à {m*10}dm \n'
      f' que tambem é igual à {m/10}dam \n'
      f' que corresponde tambem à {m/100}hm \n'
      f' que tambem é igual à {m/1000}km')