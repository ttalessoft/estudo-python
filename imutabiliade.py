nome = 'john'.upper()

nome2 = nome.upper()

print(nome == nome2) # sim os nomes são iguais

print(nome is nome2) # não os objetos são diferentes

# mas

nome = 'john'
nome2 = 'john'

print(nome == nome2) # sim os nomes são iguais
print(nome is nome2) # sim os objetos são iguais por definição de referência

# agora analise

c = [10,20,30]
d = [10,20,30]

print(c==d) # sim o conteúdo é igual
print(c is d) # não os objetos não são iguais, por definição de referência