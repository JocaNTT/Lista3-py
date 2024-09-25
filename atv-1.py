def exibir_cardapio(cardapio):
    if not cardapio:
        print("O cardápio está vazio.")
    else:
        print(f"\nCardápio:")
        for prato, preco in cardapio.items():
            print(f"{prato}: R$ {preco:.2f}")

def gerenciar_cardapio():
    cardapio = {}

    while True:
        print(f"\nMenu:")
        print("1. Adicionar prato")
        print("2. Remover prato")
        print("3. Consultar preço de um prato")
        print("4. Exibir cardápio completo")
        print("5. Sair")
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            prato = input("Digite o nome do prato: ")
            preco = float(input("Digite o preço do prato: "))
            cardapio[prato] = preco
            print(f"Prato '{prato}' adicionado ao cardápio.")
        
        elif opcao == '2':
            prato = input("Digite o nome do prato que deseja remover: ")
            if prato in cardapio:
                del cardapio[prato]
                print(f"Prato '{prato}' removido do cardápio.")
            else:
                print(f"Prato '{prato}' não encontrado no cardápio.")

        elif opcao == '3':
            prato = input("Digite o nome do prato que deseja consultar: ")
            if prato in cardapio:
                print(f"O preço do prato '{prato}' é R$ {cardapio[prato]:.2f}.")
            else:
                print(f"Prato '{prato}' não encontrado no cardápio.")

        elif opcao == '4':
            exibir_cardapio(cardapio)

        elif opcao == '5':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

gerenciar_cardapio()