# 1. Dicionário com meses do ano e duração em dias
meses = {
    'janeiro': 31,
    'fevereiro': 28,
    'marco': 31,
    'abril': 30,
    'maio': 31,
    'junho': 30,
    'julho': 31,
    'agosto': 31,
    'setembro': 30,
    'outubro': 31,
    'novembro': 30,
    'dezembro': 31
}

# 2. Imprimir chaves e valores
for mes, dias in meses.items():
    print(f"{mes}: {dias}")

# 3. Imprimir formato "Janeiro - 31 dias"
for mes, dias in meses.items():
    print(f"{mes.capitalize()} - {dias} dias")
