def horario(hora):
    if hora < 12:
        print('Bom dia')
    elif hora < 18:
        print('Boa tarde')
    else:
        print('Boa noite')

horario(10)  # Saída: Bom dia
horario(15)  # Saída: Boa tarde
horario(19)  # Saída: Boa noite
