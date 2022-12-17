# ordem de precedencia: 1: (), 2: **, 3: divisões e *, 4: + e -
# legenda........ () - PARENTESES;
# ** - EXPONENCIAÇÃO;
# // DIVISÃO INTEIRA (NAO CONSIDERA NUMERO QUEBRADO);
# PARA POTENCIA TAMBEM DARIA PARA FAZER PELO COMANDO (pow("numero", "potencia")
# % RESTO DA DIVISÃO
# ### para raiz quadrada sem biblioteca: fazer exponenciação inversa por exemplo raiz quadrada de 9   9**(1/2)
nome = input("Qual o seu nome?" )
print(f'Prazer em te conhecer {nome:20}!')
print(f'Prazer em te conhecer {nome:>20}!')
print(f'Prazer em te conhecer {nome:<20}!')
print(f'Prazer em te conhecer {nome:^20}!')
print(f'Prazer em te conhecer {nome:.^20}!')
print(f'Prazer em te conhecer {nome:=<20}!')
# end = ' ' (END = NADA PARA N QUEBRAR A LINHA ou algo para ele seguir a linha como um sinal)
#\num para quebrar a frase
print(f'Prazer em te conhecer {nome:=<20}!', end=' ')
print(f'Prazer  em te conhecer {nome:=<20}!')

#para somente duas casas
print (f'para casas decimais de 2 seria {(2):.3f}')

