# Exercício Python 085:
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[], []]
for c in range(0,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    elif n % 2 == 1:
        numeros[1].append(n)
print('='*30)
numeros[0].sort()
numeros[1].sort()
print(f"""Os valores pares digitados foram: {numeros[0]}.
Os valores impares digitados foram: {numeros[1]}.""")
