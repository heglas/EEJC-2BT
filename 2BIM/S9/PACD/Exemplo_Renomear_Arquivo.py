# Exemplo de renomear um único arquivo

import os

# Nome atual e nome novo
nome_antigo = "antigo.txt"
nome_novo = "novo.txt"

# Renomeando o arquivo
os.rename(nome_antigo, nome_novo)

print(f"Arquivo '{nome_antigo}' foi renomeado para '{nome_novo}'.")