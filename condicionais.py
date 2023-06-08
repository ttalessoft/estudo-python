numero_magico = 115

def isNumeroMagico(num):
    if num == numero_magico:
        print(f'Parabéns esse é o número mágico.: {numero_magico}')
    else:
        print(f'Errrrrrrroooou!!!')

numero_informado = int(input('Informe o seu número mágico.: '))

isNumeroMagico(numero_informado)

