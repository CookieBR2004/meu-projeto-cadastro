# Teste

Cadastro = []

def CadastrarCliente():
    Nome = input("Nome do cliente: ")
    Email = input("Email do cliente: ")
    Phone = input("Telefone do cliente: ")

    while True: 
        print("--- OPÇÕES DE PLANO ---")
        print("1 - Mensal")
        print("2 - Anual")
        print("3 - Plano Black")

        Plano1 = input("Escolha o número do Plano do cliente: ")

        if Plano1 == "1":
            Plano = "Mensal R$49,99/mês"
            break
        elif Plano1 == "2":
            Plano = "Anual R$599,99/anual"
            break
        elif Plano1 == "3":
            Plano = "Plano Black R$199,99/anual"
            break
        else:
            print("❌ Opção de plano inválida! Tente novamente.")

    Cadastro.append({
        "Nome": Nome,
        "Email": Email,
        "Phone": Phone,
        "Plano": Plano
    })

    print("✔️ Cliente cadastrado com sucesso!")
    print(" ")

def Listar():
    if not Cadastro:
        print("Nenhum cliente cadastrado.")
        return

    print("--- LISTA DE CLIENTES ---")
    for A in Cadastro:
        print(f"{A['Nome']} - {A['Email']} - {A['Phone']} - {A['Plano']}")

def menu():
    while True:
        print(" ")
        print(" ")
        print(" ")
        print("------------------------------------------------------")
        print("1 - Cadastrar cliente / 2 - Listar clientes / 3 - Sair")
        print(" ")

        B = input("Escolha: ")

        if B == "1":
            CadastrarCliente()
        elif B == "2":
            Listar()
        elif B == "3":
            print("Saindo...")
            print("💠 Criado por Mateus")
            print("💠 RA: 5425735")
            print("💠 Curso: Eng. de Software")
            break
        else:
            print("Opção inválida!")

menu()
