# Mensagem de boas-vindas
print("Bem vindo a loja da Julia Pontes Cardoso Pereira")

# Solicitação de entrada do valor unitário e quantidade do produto
valorUnitario = float(input("Entre com o valor do produto: "))
quantidade = float(input("Entre com a quantidade do produto: "))

# Cálculo do valor total sem desconto
valorSemDesconto = valorUnitario * quantidade

# Utilizando estruturas condicionais para aplicar descontos com base na quantidade
if quantidade >= 2000:
    desconto = valorSemDesconto * 0.15
elif quantidade >= 1000:
    desconto = valorSemDesconto * 0.10    
elif quantidade >= 200:
    desconto = valorSemDesconto * 0.05
else:
    desconto = 0

# Cálculo do valor total com desconto
valorComDesconto = valorSemDesconto - desconto

# Apresentação dos valores calculados na saída de console
print('Valor SEM DESCONTO: R$', valorSemDesconto)
print('Valor COM DESCONTO: R$', valorComDesconto)