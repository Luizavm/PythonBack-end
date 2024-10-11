import os

tarefas = {}

#####################################################################

def telainic (escolha1):
    print("Bem vindo!")
    print("1-Inserir tarefas \n2-Excluir tarefas \n3-Editar tarefa \n4-Sair")
    escolha1 = int(input("O que deseja fazer? \n---> "))
    return escolha1



def if1 (tarefas):
    print("Adicionar tarefa")
    print("")
    tarefas = {
        "Tarefa":input("Nome da tarefa: "),
        "Descrição":input("Descrição: "),
        "Urgência":input("Urgência: "), 

    }
    print("Tarefa adicionada com sucesso!")
    return tarefas



def if2 (tarefas):
    print("Excluir tarefas")
    print(tarefas)
    nome_tarefa = input("Nome da tarefa que deseja excluir: ")
    
    if nome_tarefa in tarefas:
        tarefas.pop(nome_tarefa)
        print(f"Tarefa '{nome_tarefa}' excluída com sucesso!")
        os.system("cls")

    elif nome_tarefa not in tarefas:
        print(f"Tarefa '{nome_tarefa}' não encontrada.")

    else:
        print("Opção inválida...")
        print("")
        os.system("cls")
        
    return nome_tarefa



def if3 (tarefas):
    print("Editar tarefas")
    editnom = input("Nome da tarefa que deseja editar: ")
    for editnom in tarefas:
        if editnom in tarefas:
            tarefas = input("Novo nome: ")
            tarefas = input("Nova descrição: ")
            tarefas = input("Nova urgência: ")
            print(f"Tarefa {editnom} editada com sucesso!")
            os.system("cls")

        if editnom not in tarefas:
            print(f"Tarefa '{editnom}' não encontrada.")
            break

    return editnom



def if4 ():
    print("Saindo...")
    os.system("cls")
    os.system("pause")
    x = 1
    return x
