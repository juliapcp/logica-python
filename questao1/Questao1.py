print("Bem vindo a loja da Julia Pontes Cardoso Pereira")
valorUnitario = float(input("Entre com o valor do produto: "))
quantidade = float(input("Entre com a quantidade do produto: "))
valorSemDesconto = valorUnitario * quantidade

if  (quantidade >= 2000):
    desconto = valorSemDesconto * 0.15
elif (quantidade >= 1000):
    desconto = valorSemDesconto * 0.10    
elif (quantidade >= 200):
    desconto = valorSemDesconto * 0.05
else :
    desconto = 0

valorComDesconto = valorSemDesconto - desconto

print('Valor SEM DESCONTO: R$: ',valorSemDesconto)
print('Valor COM DESCONTO: R$: ',valorComDesconto)