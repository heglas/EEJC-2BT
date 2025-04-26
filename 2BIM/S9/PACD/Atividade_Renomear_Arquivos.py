# Atividade prática: renomeação de arquivos

# Lista de arquivos
arquivos_na_pasta = ["trailer_fantasia", "entrevista_celebridade", "foto_perfil", "ensaio_fotografico"]

# Lista de novos nomes
novos_nomes = []

# Loop para processar cada arquivo
for arquivo in arquivos_na_pasta:
    # Converte para maiúsculo
    arquivo_maiusculo = arquivo.upper()
    
    # Define a extensão
    if "ENTREVISTA" in arquivo_maiusculo:
        novo_nome = arquivo_maiusculo + ".mp3"
    elif "TRAILER" in arquivo_maiusculo:
        novo_nome = arquivo_maiusculo + ".mp4"
    else:
        novo_nome = arquivo_maiusculo + ".jpg"
    
    novos_nomes.append(novo_nome)

# Exibe os novos nomes
print("Novos nomes de arquivos:")
for nome in novos_nomes:
    print(nome)

print("\nOrganização criativa do projeto de mídia concluída com sucesso!")