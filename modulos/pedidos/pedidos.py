import datetime

todos_pedidos = []

def adicionar_item(pedidos):
    item = input("Digite o nome do item que deseja adicionar ao pedido: ")
    if item:
        pedidos.append(item)
        print(f"Item '{item}' adicionado ao pedido!")
    else:
        print("Nome do item não pode ser vazio.")
    return pedidos

def listar_itens(pedidos):
    if pedidos:
        print("\nItens no pedido:")
        for i, item in enumerate(pedidos, 1):
            print(f"{i}. {item}")
    else:
        print("\nO pedido está vazio.")

def remover_item(pedidos):
    listar_itens(pedidos)
    if pedidos:
        try:
            indice = int(input("\nDigite o número do item que deseja remover: "))
            if 1 <= indice <= len(pedidos):
                item_removido = pedidos.pop(indice - 1)
                print(f"Item '{item_removido}' removido do pedido!")
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    return pedidos

def finalizar_pedido(pedidos):
    print("\nFinalizando o pedido...")
    listar_itens(pedidos)
    total_itens = len(pedidos)
    print(f"Total de itens no pedido: {total_itens}")

    if pedidos:
        data_hora_pedido = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        todos_pedidos.append({"pedido": pedidos[:], "data e hora": data_hora_pedido})

    print("Pedido finalizado com sucesso!")
    return True