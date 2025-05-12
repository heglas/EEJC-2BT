# 1. Verificar vida dos personagens
def verificar_vida(pontos_vida):
    for indice, vida in enumerate(pontos_vida, start=1):
        status = 'vivo' if vida > 0 else 'morto'
        print(f'Personagem {indice} está {status}')

pontos_vida_personagens = [100, 0, 50, 75]
verificar_vida(pontos_vida_personagens)

# 2. Converter Celsius para Fahrenheit
def converter_para_fahrenheit(temperaturas_celsius):
    return [(temp * 9/5) + 32 for temp in temperaturas_celsius]

temperaturas_celsius = [20, 25, 30]
temperaturas_fahrenheit = converter_para_fahrenheit(temperaturas_celsius)
print(f'Temperaturas em Fahrenheit: {temperaturas_fahrenheit}')

# 3. Verificar aprovação dos alunos
def verificar_aprovacao(notas):
    for indice, nota in enumerate(notas, start=1):
        status = 'aprovado' if nota >= 6 else 'reprovado'
        print(f'Aluno {indice} está {status}')

notas_alunos = [7, 5, 8, 4, 6]
verificar_aprovacao(notas_alunos)

# 4. Mostrar mesas disponíveis
def mostrar_mesas_disponiveis(mesas_reservadas, total_mesas=10):
    for mesa in range(1, total_mesas + 1):
        if mesa not in mesas_reservadas:
            print(f'Mesa {mesa} está disponível')

mesas_reservadas = [2, 4, 6]
mostrar_mesas_disponiveis(mesas_reservadas)

# 5. Imprimir tarefas com índice
def imprimir_tarefas(tarefas):
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f'Tarefa {indice}: {tarefa}')

tarefas = ['Estudar Python', 'Fazer compras', 'Enviar e-mails']
imprimir_tarefas(tarefas)

# 6. Calcular total de preços
def calcular_total(precos):
    return sum(precos)

precos = [10.5, 5.2, 8.0, 12.99]
total = calcular_total(precos)
print(f'Total dos preços: {total}')

# 7. Contar letras nas palavras
def contar_letras(palavras):
    for indice, palavra in enumerate(palavras, start=1):
        print(f'Palavra {indice} tem {len(palavra)} letras')

palavras = ['python', 'exemplo', 'programacao']
contar_letras(palavras)

# 8. Converter temperaturas Kelvin e Fahrenheit para Celsius
def converter_temperaturas(temperaturas_kelvin, temperaturas_fahrenheit):
    for indice, temp_k in enumerate(temperaturas_kelvin, start=1):
        celsius = temp_k - 273.15
        print(f'Temperatura {indice} em Kelvin: {temp_k}K = {celsius:.2f}°C')
    for indice, temp_f in enumerate(temperaturas_fahrenheit, start=1):
        celsius = (temp_f - 32) * 5/9
        print(f'Temperatura {indice} em Fahrenheit: {temp_f}F = {celsius:.2f}°C')

# Exemplo de uso
converter_temperaturas([300, 280, 310], [86, 95, 104])
