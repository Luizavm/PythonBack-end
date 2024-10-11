import os
from animaisdef import *

x = 0

while x == 0:
    print("Cadastro de animais")
    escolha = int(input("que animal deseja cadastrar? \n1- Gatos \n2- Cachorros \n3- Alteração de informações \n4- Sair\n-->"))

    if escolha == 1:
        print("--Cadastro de gatos--")
        nome = input("Informe o nome do gato: ")
        raça = input("Informe a raça do gato: ")
        idade = input("Informe a idade do gato: ")
        dono = input("Informe o dono do gato: ")
        celdono = input("Informe o telefone com o id do dono do gato:  ")
        proce_medic = input("Informe o procedimento médico: ")
        Paciente = Gato(nome, raça, dono, idade, proce_medic)
        Pacientes_gatos.append(Paciente)
        print(Paciente)

    elif escolha == 2:
        print("--Cadastro de cachorros--")
        nome = input("Informe o nome do cachorro: ")
        raça = input("Informe a raça do cachorro: ")
        idade = input("Informe a idade do cachorro: ")
        dono = input("Informe o dono do cachorro: ")
        celdono = input("Informe o telefone com o id do dono do cachorro:  ")
        proce_medic = input("Informe o procedimento médico: ")
        Paciente = Cachorro(nome, raça, dono, idade, proce_medic)
        Pacientes_cachorros.append(Paciente)
        print(Paciente)

    elif escolha == 3:
        print("--Alteração de informações--")
        escolha1 = int(input("O que deseja? \n1- Alterar procedimentos de gatos \n2- Alterar procedimentos de cachorros \n3- Sair \n-->"))

        if escolha1 == 1:
            print("--Alteração do procedimento--")
            escolha3 = input("Digite o número de telefone do dono para identificarmos o gato: ")

            if escolha3 in Pacientes_gatos:
                print(Paciente)
            
            elif escolha3 not in Pacientes_gatos:
                print("Paciente não existente...")

            else:
                print("Saindo...")
                os.system("cls")
        
        elif escolha3 == 2:
            print("--Alteração do procedimento--")
            escolha3 = input("Digite o número de telefone do dono para identificarmos o cachorro: ")

            if escolha3 in Pacientes_cachorros:
                print(Paciente)
            
            elif escolha3 not in Pacientes_cachorros:
                print("Esse paciente não existente...")

            else:
                print("Saindo...")
                os.system("cls")
        
        elif escolha == 3:
            print("Saindo...")
            os.system("cls")
            os.system("pause")

        else:
            print("Opção inválida...")
        
    elif escolha == 4:
        print("Saindo...")
        os.system("cls")
        os.system("pause")
        

    else:
        print("Opção inválida...")
        

#Errado

