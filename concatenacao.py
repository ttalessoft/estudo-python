nome = 'ttales r g s silva'
cpf = '000.000.000-00'
nascimento = 1985
ano_atual = 2023
idade = ano_atual-nascimento

# forma 1
print( 
    'Meu nome é.: ' + nome 
    + ', meu documento pessoal é.: '+ cpf
    + ' e minha idade é.: '+ str(idade))

print('\n')

# forma 1
print('Olá '+ nome + ', sua idade é '+str((ano_atual-nascimento)) + '.')
print('\n')

# forma 2
print('Olá {}, sua idade é {}.'.format(nome, str((ano_atual-nascimento))))
print('\n')

# forma 3 (a partir do python 3.6 apenas)
print(f'Olá {nome}, sua idade é {idade}.')
print('\n')