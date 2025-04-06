from modulos.pedidos.pedidos import adicionar_item, listar_itens, remover_item, finalizar_pedido
from modulos.pedidos.extrato import salvar_extrato, consultar_extrato


def exibir_menu_inicial():
    while True:
        print("\n--- MENU INICIAL ---")
        print("1. Abrir pedido")
        print("2. Extrato do dia")
        print("3. Sair do programa")

        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                exibir_menu_pedido()
            elif opcao == 2:
                exibir_submenu_extrato()
            elif opcao == 3:
                print("Saindo do programa. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


def exibir_menu_pedido():
    pedidos = []
    while True:
        print("\n--- MENU DE PEDIDO ---")
        print("1. Adicionar item")
        print("2. Listar itens")
        print("3. Remover item")
        print("4. Finalizar pedido e voltar ao menu inicial")

        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                pedidos = adicionar_item(pedidos)
            elif opcao == 2:
                listar_itens(pedidos)
            elif opcao == 3:
                pedidos = remover_item(pedidos)
            elif opcao == 4:
                if finalizar_pedido(pedidos):
                    break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


def exibir_submenu_extrato():
    while True:
        print("\n--- EXTRATO ---")
        print("1. Consultar extrato")
        print("2. Salvar extrato")
        print("3. Voltar ao menu inicial")

        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                consultar_extrato()
            elif opcao == 2:
                salvar_extrato()
            elif opcao == 3:
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
