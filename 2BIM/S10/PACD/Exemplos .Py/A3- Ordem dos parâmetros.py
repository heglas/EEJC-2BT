def exemplo(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

exemplo('Alice', 25)
# Saída: Nome: Alice, Idade: 25
exemplo(25, 'Alice')
# Saída: Nome: 25, Idade: Alice
exemplo(nome="Alice", idade=25)
# Saída: Nome: Alice, Idade: 25
exemplo(idade=25, nome="Alice")
# Saída: Nome: Alice, Idade: 25
