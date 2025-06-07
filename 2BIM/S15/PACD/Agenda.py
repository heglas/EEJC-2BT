agenda = []

def adicionar_contato():
    print("\n--- Adicionar Contato ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    renda = float(input("Renda: "))
    estado = input("Estado: ")
    contato = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "email": email,
        "renda": renda,
        "estado": estado
    }
    agenda.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")

def exibir_contatos():
    print("\n--- Lista de Contatos ---")
    for contato in agenda:
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")

def buscar_contato():
    nome = input("\nDigite o nome do contato a buscar: ")
    encontrados = [c for c in agenda if c["nome"].lower() == nome.lower()]
    if encontrados:
        print("\n--- Contato Encontrado ---")
        for c in encontrados:
            print(f"Nome: {c['nome']}, Idade: {c['idade']}, Telefone: {c['telefone']}, E-mail: {c['email']}, Renda: {c['renda']}, Estado: {c['estado']}")
    else:
        print("Contato não encontrado.")

def remover_contato():
    nome = input("\nDigite o nome do contato a remover: ")
    for i, contato in enumerate(agenda):
        if contato["nome"].lower() == nome.lower():
            agenda.pop(i)
            print(f"Contato {nome} removido com sucesso!")
            return
    print("Contato não encontrado.")

def corrigir_contato():
    nome = input("\nDigite o nome do contato a corrigir: ")
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            print("\nSelecione o campo a corrigir:")
            print("1 - Nome")
            print("2 - Idade")
            print("3 - Telefone")
            print("4 - E-mail")
            print("5 - Renda")
            print("6 - Estado")
            opcao = input("Opção: ")
            if opcao == "1":
                contato["nome"] = input("Novo nome: ")
            elif opcao == "2":
                contato["idade"] = int(input("Nova idade: "))
            elif opcao == "3":
                contato["telefone"] = input("Novo telefone: ")
            elif opcao == "4":
                contato["email"] = input("Novo e-mail: ")
            elif opcao == "5":
                contato["renda"] = float(input("Nova renda: "))
            elif opcao == "6":
                contato["estado"] = input("Novo estado: ")
            else:
                print("Opção inválida.")
            print("Contato atualizado com sucesso!")
            return
    print("Contato não encontrado.")

def quantidade_contatos():
    print(f"\nQuantidade de contatos cadastrados: {len(agenda)}")

def media_idade():
    if agenda:
        media = sum(c["idade"] for c in agenda) / len(agenda)
        print(f"\nMédia de idade dos contatos: {media:.1f} anos")
    else:
        print("\nNenhum contato cadastrado.")

def contatos_por_estado():
    estados = {}
    for contato in agenda:
        estado = contato["estado"]
        estados[estado] = estados.get(estado, 0) + 1
    print("\n--- Contatos por Estado ---")
    for estado, qtd in estados.items():
        print(f"{estado}: {qtd} contato(s)")

def menu():
    print("\n--- Agenda de Contatos ---")
    print("1 - Adicionar contato")
    print("2 - Exibir contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("5 - Corrigir contato")
    print("6 - Quantidade de contatos")
    print("7 - Média de idade")
    print("8 - Contatos por estado")
    print("9 - Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        exibir_contatos()
    elif opcao == "3":
        buscar_contato()
    elif opcao == "4":
        remover_contato()
    elif opcao == "5":
        corrigir_contato()
    elif opcao == "6":
        quantidade_contatos()
    elif opcao == "7":
        media_idade()
    elif opcao == "8":
        contatos_por_estado()
    elif opcao == "9":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
