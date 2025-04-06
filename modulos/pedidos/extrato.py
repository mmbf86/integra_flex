import datetime



def salvar_extrato():
    # Importação local para evitar dependência circular
    from modulos.pedidos.pedidos import todos_pedidos
    if todos_pedidos:
        nome_arquivo = f"Extrato_pedidos_{datetime.datetime.now().strftime('%Y-%m-%d')}.txt"
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write("Extrato de Pedidos do Dia:\n")
            for i, registro in enumerate(todos_pedidos, 1):
                arquivo.write(
                    f"Pedido {i} (Data e Hora: {registro['data e hora']}):\n")
                arquivo.write("\n".join(registro["pedido"]) + "\n\n")
        print(f"Extrato salvo com sucesso no arquivo: {nome_arquivo}")
    else:
        print("Nenhum pedido foi realizado ainda. Nada para salvar.")


def consultar_extrato():
    from modulos.pedidos.pedidos import todos_pedidos  # Importação local
    if todos_pedidos:
        print("\n--- EXTRATO DE PEDIDOS ---")
        for i, registro in enumerate(todos_pedidos, 1):
            print(f"Pedido {i} (Data e Hora: {registro['data e hora']}):")
            print("\n".join(registro["pedido"]))
            print()
    else:
        print("Nenhum pedido foi realizado hoje.")
