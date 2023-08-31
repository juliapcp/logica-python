# Definição da função para obter o peso do cachorro
def cachorro_peso():
    peso = 0
    while True:
        try:
            peso = float(input("Entre com o peso do cachorro: "))
            # Verifica se o peso é maior ou igual a 50 kg
            if peso >= 50:
                print("Não aceitamos cachorros tão grandes, tente novamente")
                continue
            break  # Sai do loop se o peso for válido
        except ValueError:
            print("Valor não numérico, tente novamente")
            continue
    return peso

# Definição da função para obter o multiplicador com base no tipo de pelo
def cachorro_pelo():
    while True:
        pelo = input("Entre com o pelo do cachorro (c/m/l): ").lower()
        # Verifica se a opção de pelo é válida
        if pelo not in ["c", "m", "l"]:
            print("Opção inválida, tente novamente")
            continue
        # Retorna o multiplicador correspondente ao tipo de pelo
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        else :
            return 2

# Definição da função para obter os serviços extras
def cachorro_extra():
    valorTotal = 0
    while True:
        try:
            extra = int(input("Deseja adicionar mais algum serviço? \n1 - Corte de Unhas - R$ 10,00 \n2 - Escovar Dentes - R$ 12,00 \n3 - Limpeza de Orelhas - R$ 15,00 \nO - Não desejo mais nada \n"))
            # Verifica se a opção de serviço extra é válida
            if extra not in [1, 2, 3, 0]:
                print("Opção inválida, tente novamente")
                continue
            # Acumula o valor extra correspondente ao serviço selecionado
            if extra == 1:
                valorTotal += 10
            elif extra == 2:
                valorTotal += 12
            elif extra == 3:
                valorTotal += 15
            elif extra == 0:
                break  # Sai do loop se o cliente não desejar mais serviços
        except ValueError:
            print("Opção inválida, tente novamente")
            continue    
    return valorTotal

# Mensagem de boas-vindas
print("Bem-vindo a PetShop da Julia Pontes Cardoso Pereira")

# Obtendo o peso do cachorro usando a função cachorro_peso()
peso = cachorro_peso()

# Definindo o valor base com base no peso do cachorro
base = 0
if peso < 3:
    base = 40
elif peso < 10:
    base = 50
elif peso < 30:
    base = 60
elif peso < 50:
    base = 70

# Obtendo o multiplicador usando a função cachorro_pelo()
multiplicador = cachorro_pelo()

# Obtendo os extras e acumulando o valor deles usando a função cachorro_extra()
extra = cachorro_extra()

# Calculando o valor total a pagar
total = base * multiplicador + extra 

# Exibindo o valor total e os detalhes do pedido
print("O valor total é de R$ %.2f" % total, "(peso = ", peso, "multiplicador = ", multiplicador, "extra = ", extra, ")")