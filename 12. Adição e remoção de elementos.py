# Criando um dicionário inicial
meu_dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
# Acesso a elementos
nome_da_pessoa = meu_dicionario['nome']
print(f"Nome da pessoa: {nome_da_pessoa}")
# Adição de um novo par chave-valor
meu_dicionario['profissao'] = "Programador"
# Remoção de um par chave-valor
del meu_dicionario['cidade']
# Exibindo o dicionário após as operações
print("Dicionário atualizado:", meu_dicionario)
# Saída:
# Nome da pessoa: João
# Dicionário atualizado: {'nome': 'João', 'idade': 25, 'profissao': 'Programador'}
