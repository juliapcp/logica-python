# Definindo a função para cadastrar um colaborador, recebendo um ID como parâmetro
def cadastrar_colaborador(id):
    while True:
        try: 
            nome = input("Entre com o nome do colaborador: ")
            setor = input("Entre com o setor do colaborador: ")
            pagamento = float(input("Entre com o pagamento do colaborador: "))
            colaborador = {"id": id, "nome": nome, "setor": setor, "pagamento": pagamento}
            lista_colaboradores.append(colaborador)  # Adicionando o colaborador à lista
            break
        except:
            print("Entrada inválida")
            continue

# Definindo a função para consultar colaboradores
def consultar_colaborador():
    try:
        opcao = int(input("Qual opção deseja? \n 1. Consultar Todos \n 2. Consultar por Id \n 3. Consultar por Setor \n 4. Retornar ao menu \n"))
        if opcao not in [1, 2, 3, 4]:
            print("Opção inválida")
            return
        if opcao == 1:  # Consultar todos os colaboradores
            print(lista_colaboradores)
        elif opcao == 2:  # Consultar por ID
            print(lista_colaboradores[int(input("Entre com o id do colaborador: ")) - 1])
        elif opcao == 3:  # Consultar por Setor
            setor = input("Entre com o setor: ").lower()
            for colaborador in lista_colaboradores:
                if colaborador["setor"].lower() == setor:
                    print(colaborador)
        elif opcao == 4:  # Retornar ao menu
            return            
    except ValueError:
        print("Opção inválida")

# Definindo a função para remover um colaborador
def remover_colaborador():
    id = int(input("Entre com o id do colaborador: "))
    for colaborador in lista_colaboradores:
        if colaborador["id"] == id:
            lista_colaboradores.remove(colaborador)
            break

# Mensagem de boas-vindas
print("Bem-vindo ao sistema de gerenciamento de pessoas da Julia Pontes Cardoso Pereira")
lista_colaboradores = []  # Inicializando a lista de colaboradores vazia
id_global = 0  # Inicializando o ID global

# Loop principal do programa
while True:
    try:
        opcao = int(input("Qual opção deseja? \n 1. Cadastrar Colaborador \n 2. Consultar Colaborador \n 3. Remover Colaborador \n 4. Encerrar Programa \n"))
        if opcao not in [1, 2, 3, 4]:
            print("Opção inválida")
            continue
        if opcao == 1:  # Cadastrar colaborador
            id_global += 1
            cadastrar_colaborador(id_global)
        elif opcao == 2:  # Consultar colaborador
            consultar_colaborador()
        elif opcao == 3:  # Remover colaborador
            remover_colaborador()
        elif opcao == 4:  # Encerrar programa
            break        
    except ValueError:
        print("Opção inválida")
        continue
