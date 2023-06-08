# declara e atribui valores
numeros = [88, 41, 35, 67, 89, 11]
print(numeros)

# adicionar
numeros.append(1)
print(numeros)

# fatiamento
listaFatiada = numeros[2:5]
print(f'lista fatiada = {listaFatiada}')

# percorre o array de trás para frente com fatiamento
print(listaFatiada[::-1])

# acessar elementos
print(numeros[3])

# acessar a última possição
print(numeros[int(len(numeros)-1)])
print(numeros[-1])

# percorrer os elementos da lista
for i in numeros:
    print(i)

for i in range(len(numeros)):
    print(numeros[i])

# copia todos os elementos de uma lista
copyList = numeros.copy();
print(f'copyList = {copyList}')

# limpa todos os items de uma lista
copyList.clear()
print(f'copyList = {copyList}')

# retorna o número de elementos de uma lista
print(f'numeros = {numeros.count(1)}')

# adiciona no final de uma lista os elementos de uma outra lista
newList = [41, 42, 43]
numeros.extend(newList)
print(f'nova lista = {numeros}')

# retorna o indice do primeiro elementro contratro com aquele atributo
print(f'indice do primeiro elemento = {numeros.index(67)}')

# adiciona um elemento em uma posição espevifica
numeros.insert(2, 9999)
print(f'numeros = {numeros}')

# remove um elemento em uma posição especifica
numeros.pop(2)
print(f'numeros = {numeros}')

# remove um elemento pelo valor do atributo
numeros.remove(11)
print(f'numeros = {numeros}')

# ordena de forma asc uma lista
numeros.sort()
print(f'numeros order asc = {numeros}')

# ordena de forma desc uma lista
numeros.reverse()
print(f'numeros order desc = {numeros}')

