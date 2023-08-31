# Mensagem de boas-vindas
print("Bem-vindo a Sorveteria da Julia Pontes Cardoso Pereira")
valor_total = 0

while True:  # Loop principal do programa
    # Entrada do sabor do sorvete
    sabor = input("Entre com o sabor desejado (tr/pr/es): ")
    if(sabor not in ['tr', 'pr', 'es']):
        print("“Sabor de Sorvete Inválido")
        continue # Volta ao início do loop

    quantidade = input("Entre com o número de bolas de sorvete desejado (1/2/3): ")
    
    # Verificação da quantidade de bolas de sorvete
    if quantidade not in ['1', '2', '3']:
        print("Quantidade de Bolas de Sorvete Inválida")
        continue  # Volta ao início do loop
    else :
        quantidade = int(quantidade)
    
    # Verificação do sabor do sorvete
    if sabor not in ['tr', 'pr', 'es']:
        print("Sabor de Sorvete Inválido")
        continue  # Volta ao início do loop
    
    # Cálculo do valor total do pedido
    if quantidade == 1:
        if sabor == 'tr':
            valor_pedido = 6
        elif sabor == 'pr':
            valor_pedido = 7
        else:
            valor_pedido = 8
    elif quantidade == 2:
        if sabor == 'tr':
            valor_pedido = 11
        elif sabor == 'pr':
            valor_pedido = 13
        else:
            valor_pedido = 15
    else:
        if sabor == 'tr':
            valor_pedido = 15
        elif sabor == 'pr':
            valor_pedido = 18
        else:
            valor_pedido = 21

    print(f"Voce pediu {quantidade} bolas de sorvete do sabor {sabor}: R$ {valor_pedido:.2f}")
    valor_total += valor_pedido
    # Pergunta se o cliente quer pedir mais alguma coisa
    continuar = input("Deseja mais algum sorvete? (S/outra tecla): ")
    if continuar.lower() != 's':
        # Exibe o valor total e encerra o loop principal
        print(f"O valor total a ser pago: R$ {valor_total:.2f}")
        break  # Encerra o loop principal

    


