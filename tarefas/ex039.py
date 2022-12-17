# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua
# idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
ano = int(input('Digite seu ano de nacimento: '))
age = datetime.date.today().year - ano

if age > 18:
    print(f'Você tem {age} anos, seu tempo de alistamento já passou. O senhor está {age - 18} anos fora do prazo,'
          f' \033[31:4mcaso não tenha se alistado favor comparecer ao distrito militar mais proximo.\033[m')
elif age < 18:
    print(f'Você tem {age} anos, seu seu periodo de alistamento ainda não chegou, '
          f'falta {18 - age} anos para você poder se alistar')
elif age == 18:
    print(f'Parabens, seu tempo de alistamento chegou, dirija-se a junta militar mais proxima, \033[32:4mBrasil!')