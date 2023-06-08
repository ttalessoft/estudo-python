import datetime


def calculaIdade(ano:int)-> int:
    return datetime.date.today().year - int(ano)

def imprimeIdade(nome: str, ano:int):
    idade = calculaIdade(ano)
    print(f'{nome} sua idade é.: {idade}')

imprimeIdade('john doe', 1988)

imprimeIdade('john lee', 1985)