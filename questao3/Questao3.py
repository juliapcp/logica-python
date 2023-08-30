def cachorro_peso():
    peso = 0
    while True:
        try:
            peso = float(input("Entre com o peso do cachorro: "))
            if peso >= 50:
                print("Não aceitamos cachorros tão grandes, tente novamente")
                continue
            break
        except ValueError:
            print("Valor não numérico, tente novamente")
            continue
    return peso


def cachorro_pelo():
    while True:
        pelo = input("Entre com o pelo do cachorro (c/m/l): ").lower()
        if pelo not in ["c", "m", "l"]:
            print("Opção inválida, tente novamente")
            continue
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        else :
            return 2

def cachorro_extra():
    valorTotal = 0
    while True:
        try:
            extra = int(input("Deseja adicionar mais algum serviço? \n1 - Corte de Unhas - R$ 10,00 \n2 - Escovar Dentes - R$ 12,00 \n3 - Limpeza de Orelhas - R$ 15,00 \nO - Não desejo mais nada \n"))
            if extra not in [1, 2, 3, 0]:
                print("Opção inválida, tente novamente")
                continue
            if extra == 1:
                valorTotal += 10
            elif extra == 2:
                valorTotal += 12
            elif extra == 3:
                valorTotal += 15
            elif extra == 0:
                break
        except ValueError:
            print("Opção inválida, tente novamente")
            continue    

    return valorTotal
        
print("Bem-vindo a PetShop da Julia Pontes Cardoso Pereira")
peso = cachorro_peso()
base = 0
if peso < 3:
    base = 40
elif peso < 10:
    base = 50
elif peso < 30:
    base = 60
elif peso < 50:
    base = 70

multiplicador = cachorro_pelo()
extra = cachorro_extra()
total = base * multiplicador + extra 

print("O valor total é de R$ %.2f" % total, "(peso = ", peso, "multiplicador = ", multiplicador, "extra = ", extra, ")")