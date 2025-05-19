print("Fase de preparação:")
for t in range(10, 0, -1):
    print(f"Tempo restante: {t} segundos")

print("\nFase de ignição:")
for t in range(10, -1, -1):
    print(f"Ignição ocorrida!" if t == 0 else f"Contagem: {t}")