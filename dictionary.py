produtos = {
    '111': 'produto 111',
    '222': 'produto 222',
    '333': 'produto 333',
    '444': 'produto 444',
}

print(produtos)

produtos.update({'999':'produto 999'})

print(produtos.get('111'))
print(produtos.keys())
print(produtos.values())

print(produtos)