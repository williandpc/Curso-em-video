# modificação de texto

# ## texto de exemplo "Curso em Vídeo Python"

frase = 'Curso em Vídeo Python'

print('ex:1', frase[9])  # ## mostra somente o caracter de indice 9(o indice inicia de 0 e conta com os espaços)
print('ex:2', frase[9:13])
# ## mostra o range de caracteres escolhidos deixando em aberto o último valor do range
# matematicamente seria um sistema de final aberto tendo como exemplo [9:13[
# se apoia no 13, mas somente como indicação
print('ex:3', frase[9:14])
print('ex:4', frase[9:])  # #fatia inicialmente do range indicado ate o final da frase
print('ex:5', frase[:9])  # #fatia inicialmente começo ate o final do range
print('ex:6', frase[9::2])  # ##o ultimo valor é feito para questão de pular N indices(no caso vai pular uma letra e
# pegar a segunda

# Analise da string
print('ex:7', len(frase))  # mostra a quantidade de letras na frase
print('ex:8', frase.count('o'))  # mostra a quantidade de 'o' na ‘string’
print('ex:9', frase.count('o', 0, 13))  # mostra a quantidade de 'o' na ‘string’ do indice 0 ate o indice 13 sem incluir o 13
print('ex:10', frase.find('deo'))  # mostra fechadamente em qual indice começa a frase
print('ex:11', frase.find('Android'))  # trecho que nao existe na frase(neste caso ele sempre vai retornar -1
print('ex:12', 'curso' in frase)  # pedi para verificar se existe 'curso' na frase (nao tem curso, tem Curso)
print('ex:13', 'curso' in frase.lower())  # pedi para verificar se existe 'curso' na frase com tudo minusculo (deu certo)
print('ex:14', 'curso'.title() in frase)  # pedi para verificar se existe 'curso' com a primeira maiuscula na frase
print('ex:15', 'curso'.capitalize() in frase)  # pedi para verificar se existe 'curso' capitalizada na frase
print('ex:16', frase.replace('Python', 'Android'))  # bem objetivo o texto ja indica tudo eu substitui 'Python' por 'Android'
# replace não altera a string, mas pode alterar a variavel como "frase4 = frase.replace(tananan)
print('ex:17', len(frase.replace('Python', 'Android')))  # pedi para indicar a quantidade de letras na frase alterada
print('ex:18', frase.replace('Curso', 'Android'))  # Brincando com as modificações
print('ex:19', frase.upper())  # Para deixar todas as letras em maiusculo = upper
print('ex:20', frase.lower())  # para deixar todas as letras em minusculo = lower
print('ex:21', frase.capitalize())  # para deixar so a primeira LETRA da FRASE INTEIRA em maiusculo
print('ex:22', frase.title())  # para deixar a primeira  LETRA de CADA PALAVRA em maisuculo

frase2 = '   Aprenda Python  '
print('ex:23', frase2)
print('ex:24', frase2.strip())  # remove os espaços adicionais que nao separam palavras
print('ex:25', frase2.rstrip())  # remove os espaços adicionais À DIREITA que não separam palavras
print('ex:26', frase2.lstrip())  # remove os espaços adicionais À ESQUERDA que não separam palavras

# voltando para a frase 1 e trabalhando com divisão.
print('ex:27', frase.split())  # dividiu a frase em palavras e formou uma lista (nesse caso):,
# a lista tem 4 elementos com um indice que tambem inicia de 0
frase3 = frase.split()  # dividi a frase na sua variavel nao somente para apresentação
print('ex:28', frase3[0])  # apos separar as palavras e numeralas com indices,
# eu estou a pesquisar qual a primeira palavra, a de indice = 0
print('ex:29', frase3[0][0])  # Quero saber qual a primeira letra( letra de indice 0)
# da primeira palavra (palabra de indice 0)
frase3 = '-'.join(frase3)  # Aqui eu juntei novamente a frase so que juntei ela com traços ('-') ao inves de espaços
print('ex:30', frase3)
print('ex:31', '.'.join(frase3))  # aqui eu juntei uma frase que nao estava separada,
# ele acrescentou antes de cada letra um '.'

# print com texto grande utilizar 3 aspas duplas (""") para abrir e 3 para fechar
