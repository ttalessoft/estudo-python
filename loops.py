num_magico = 101

max_tentativas = 3
tentativas = 0

while tentativas < max_tentativas:
    num_informado = int(input('Informe um valor:'))

    if num_informado == num_magico:
        print('Parabéns, vc acertou!!!')
        break
    elif num_informado > num_magico:
        print('Errooou, informe um número menor!')
        tentativas+=1
    else:
        print('Errooou, informe um número maior!')
        tentativas+=1
