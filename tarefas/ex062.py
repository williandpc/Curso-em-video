# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

count = 1
num = int(input('Digite o primeiro termo da Progressão: '))
razao = int(input('Agora a razão: '))
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print(f'{num}', end='→ ')
        num += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'Finalizamos  com {total} termos!')
 
