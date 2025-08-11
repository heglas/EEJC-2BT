# Exemplo estruturado — substituir pela lógica de extração real
reviews = [
    "Ótimo produto, estou muito satisfeito com a qualidade.",
    "O produto não atendeu às minhas expectativas, não recomendo.",
    "Produto excelente, entrega rápida, recomendo!"
]

with open('reviews.txt', 'w', encoding='utf-8') as f:
    for r in reviews:
        f.write(r + '\n')
