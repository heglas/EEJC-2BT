def saudacao_horario(nome, hora):
    if hora < 12:
        print(f"Bom dia, {nome}")
    elif hora < 18:
        print(f"Boa Tarde, {nome}")
    else:
        print(f"Boa noite, {nome}")
