from projeto_classes import *
import os

x = 0

while x == 0:
    print("Bem-vindo!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Menu:")
    escolhamenu = int(input("1- Cadastro do cliente \n2- Login do cliente \n3- Cadastrar livros \n4- Excluir cadastro de cliente \n5- Sair \n--> "))
    # Menu para escolher o cadastro, login, cadastrar livros, listar livros, sair 
    

    if escolhamenu == 1:
        while True:
            print("~Cadastro de clientes~")
            nome = input("Informe o nome completo do cliente: ")
            cpf = int(input("Informe o CPF do cliente sem caracteres especiais: "))
            email = input("Informe o email do cliente: ")
            #Cadastrando as informações cliente.
                
            if cpf in clientes:
                print("CPF já cadastrado. \nCliente não registrado...")
                os.system("cls")
                #cpf já é cadastrado e volta para a opção de cadastrar

            elif cpf not in clientes:
                Cliente = Cadastro(nome, cpf, email)
                clientes.append(cpf)
                print("Cliente cadastrado com sucesso!")
                os.system("cls")
                os.system("pause")
                break
                #Cadastrar cliente na classe criando uma instância e cadastrando o cpf na lista
            
            else:
                print("Opção inválida...")
                os.system("cls")
                os.system("pause")
                #Se não for nenhuma das opções voltará para o menu

    elif escolhamenu == 2:
        print("~Login do cliente~")
        nome = input("Informe o nome completo do cliente: ")
        cpf = int(input("Informe o CPF do cliente sem caracteres especiais: "))
        #Se a escolha for 2 vamos para o login do cliente
        
        if cpf in clientes:
            while True:
                print("~Menu do cliente~")
                escolhamenulog = int(input("1- Empréstimo \n2- Devolução \n3- Informações do cliente \n4- Voltar ao menu inicial \n---> "))
                #Se o CPF estiver cadastrado o menu se abre em loop

                if escolhamenulog == 1:
                    while True:
                        print("~Empréstimo~")
                        cpf2 = cpf
                        livro = input("Informe o nome do livro: ")

                        if livro in todoslivros:
                            print(f"Livros emprestados: {emprestados} \nTodos os livros: {todoslivros}")
                            emprestados.append(cpf2, livro)  # Cadastra o empréstimo
                            print(f"Empréstimo do livro '{livro}' realizado com sucesso para o CPF: {cpf2}! \nO cliente tem 15 dias para devolver.")
                            escolhacad = int(input("Deseja fazer o empréstimo de outro livro? \n1- Sim \n2- Não \n---> "))

                            if escolhacad == 1:
                                os.system("pause")  # Pausa até o usuário pressionar uma tecla
                                
                            elif escolhacad == 2:
                                print("Voltando ao menu inicial...")
                                os.system("cls")  # Limpa a tela (correção da digitação)
                                break  
                                
                            else:
                                print("Opção inválida...")
                                os.system("pause")  # Pausa para o usuário ler a mensagem

                        elif livro not in todoslivros:
                            print("Livro inexistente...")
                            os.system("pause")
                        
                        else: 
                            print("Opção inválida...")
                            os.system("pause")  # Pausa para o usuário ler a mensagem


                elif escolhamenulog == 2:
                    while True:
                        print("~Devolução~")
                        livroesc = int(input("O que deseja? \n1- Informar o livro \n2- Sair \n---> "))

                        if livroesc == 1:
                            namelivre = input("Informe o nome do livro a ser devolvido: ")

                        # Verificar se o livro está emprestado
                            if namelivre in emprestados:
                                while True:
                                    print(f"Livro '{livro}' devolvido com sucesso! Estava emprestado ao CPF: {cpf}")
                                    emprestados.pop(cpf2, livro)
                                    escolhadevol = int(input("Deseja devolver outro livro? \n1- Sim \n2- Não \n---> "))

                                    if escolhadevol == 1:
                                        os.system("pause")  # Pausa até o usuário pressionar uma tecla e volta ao loop

                                    elif escolhadevol == 2:
                                        print("Voltando ao menu inicial...")
                                        os.system("cls")  # Limpa a tela e sai do loop
                                        break 

                                    else:
                                        print("Opção inválida...")
                                        os.system("pause")  # Pausa para o usuário ler a mensagem

                            elif namelivre not in emprestados:
                                print(f"O livro '{livro}' não está marcado como emprestado. \nVeja se digitou o nome corretamente.")
                                os.system("pause")

                            else:
                                print("Opção inválida...")
                                os.system("pause")

                        elif livroesc == 2:
                            print("Saindo...")
                            os.system("cls")
                            break

                        else:
                            print("Opção inválida...")
                            os.system("pause")
                                    
                elif escolhamenulog == 3:
                    print("~Informações do cliente~")
                    Cliente.retorna
                
                elif escolhamenulog == 4:
                    print("Voltando ao menu inicial...")
                    os.system("cls")
                    break

                else:
                    print("Opção inválida...")
                    os.system("pause")

        elif cpf not in clientes:
            print("Cpf incorreto ou inexistentes. \nCorrija ou cadastre o CPF...")
            escolhasair = int(input("O que deseja? \n1- Digitar novamente \n2- Sair do menu \n--->"))
            #Se o cpf não estiver na lista o menu do login não abre

            if escolhasair == 1:
                print("Voltando...")
                os.system("pause")

            elif escolhasair == 2:
                print("Saindo...")
                os.system("cls")
                break

            else:
                print("Opção inválida...")
                os.system("pause")
        
        else:
            print("Opção inválida...")
            os.system("pause")

    elif escolhamenu == 3:
        while True:
            print("~Cadastro de livros~")
            escolhalivro = int(input("O que deseja? \n1- Ver a lista de livros do sistema que estão emprestados \n2- Cadastrar um novo livro no sistema \n3- Ver todos os livros da biblioteca \n4- Voltar ao menu inicial \n---> "))

            if escolhalivro == 1:
                print(emprestados)
                os.system("pause")

            elif escolhalivro == 2:
                while True:
                    print("~Cadastro de livros~")
                    nomelivro = input("Informe o nome do livro: ")
                    genero = input("Informe o gênero do livro: ")

                    if nomelivro in todoslivros:
                        print("Este livro já existe... \nInsira um livro válido")
                        os.system("pause")

                    elif nomelivro not in todoslivros:
                        print("Livro cadastrado!")
                        novolivro = Cadastro_livro(nomelivro, genero)
                        todoslivros.append(novolivro)
                        break

            elif escolhalivro == 3:
                print(todoslivros)
                os.sytem("pause")

            elif escolhalivro == 4:
                print("Voltando...")
                os.system("cls")
                break
            
            else:
                print("Opção inválida...")
                os.system("cls")
                os.system("pause")

    elif escolhamenu == 4:
        while True:
            escolhadel = int(input("O que deseja? \n1- Deletar o usuário \n2-Sair"))
            
            if escolhadel == 1:
                print("~Deletar usuário~")
                nome = input("Informe o nome completo do cliente: ")
                cpf = int(input("Informe o CPF do cliente: "))
            
                if cpf in clientes:
                    while True:
                        print("~Excluindo Cliente~")
                        clientes.pop(Cliente)
                        #Se o CPF estiver na lista o cliente é excluído
                        break

                elif cpf not in clientes:
                    print("Cpf incorreto ou inexistente.")
                    os.system("pause")
                    #Se o cpf não estiver na lista nada é feito

            elif escolhadel == 2:
                print("Saindo...")
                os.system("cls")
                break

    elif escolhamenu == 5:
        print("Saindo...")
        x == 1
        os.system("pause")

    else:
        print("Opção inválida...")
        os.system("cls")
        os.system("pause")