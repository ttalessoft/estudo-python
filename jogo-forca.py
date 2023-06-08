lib_palavras = ['banana', 'carro', 'computador', 'macaco', 'dipirona', 'eclesiastico']
indice = int(input(f'Informe um número de 0 até {len(lib_palavras)}:'))
palavra_secreta = lib_palavras[indice]

print(palavra_secreta)

gabarito = []

for i in range(0, len(palavra_secreta), 1):
    gabarito.append('_')

print(gabarito)