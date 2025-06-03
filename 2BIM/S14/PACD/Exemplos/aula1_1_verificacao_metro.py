coordenadas_estacoes_metro = [
    (-23.5505, -46.6333),
    (-23.5678, -46.6522),
    (-23.5234, -46.6731),
    (-23.5489, -46.6112)
]
for indice, coordenada in enumerate(coordenadas_estacoes_metro, start=1):
    lat, lon = coordenada
    print(f"Estação {indice}: Localização - Latitude: {lat}, Longitude: {lon}")
posicao_procurada = (-23.5234, -46.6731)
if posicao_procurada in coordenadas_estacoes_metro:
    print(f"Uma estação de metrô está localizada em {posicao_procurada}")
else:
    print(f"Nenhuma estação de metrô encontrada em {posicao_procurada}")