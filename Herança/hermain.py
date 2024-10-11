import os
from classeherança import *
from defher import *

Cadastro = []

while True:
    while True:
        try:
            menu()
            escolhamenu = int(input("O que deseja? \n--> "))
            break

        except Exception as e:
            print("Opção inválida... \nTente de novo...")
            os.system("cls")
            os.system("pause")

    match escolhamenu:
        case 1:
            while True:
                try:
                    nomecad = input("Informe seu primeiro nome: \n--> ")
                    sobnomecad = input("Informe seu sobrenome completo: \n--> ")
                    cpfcad = int(input("Informe seu CPF: \n*Somente os números sem caracteres especiais* \n--> "))
                    saldo = int(input("Informe seu saldo inicial: \n--> "))

                    if cpfcad not in Conta:
                        conta = Conta(nomecad, sobnomecad, cpfcad, saldo)
                        Cadastro.append(conta)
                        print("Cliente cadastrado com sucesso!")
                        break

                    elif cpfcad in Conta:
                        print("Conta já existente, faça login no menu...")
                        os.system("cls")
                        os.system("pause")
                        break

                    else:
                        print("Opção inválida...")
                        os.system("cls")
                        os.system("pause")

                except Exception as e:
                    print(f"Opção inválida, o erro foi: {e} \nTente de novo...")
                    os.system("cls")
                    os.system("pause")

        case 2:
            while True:
                try:
                    print("- Login -")
                    lognom = input("Informe seu nome: \n--> ")
                    logsobnom = input("Informe seu sobrenome completo: \n--> ")
                    logcpf = int(input("Informe seu CPF: \n*Somente os números sem caracteres especiais* \n--> "))

                    if logcpf in Conta:
                        print(f"Bem-vindo, {lognom}!")
                        print(f"Seu saldo: {saldo}")
                        while True:
                            while True:
                                try:
                                    escolhacont = int(input("O que deseja? \n01 - Entrar na conta corrente \n02- Entrar na conta poupança \n03- Sair \n--> "))
                                    break

                                except Exception as e:
                                    print(f"Opção inválida, o erro foi: {e} \nTente de novo...")
                                    os.system("cls")
                                    os.system("pause")

                            match escolhacont:
                                case 1:
                                    print("- Conta corrente -")
           

                except Exception as e:
                        print(f"Opção inválida, o erro foi: {e} \nTente de novo...")
                        os.system("cls")
                        os.system("pause")


        case 3:
            print("Saindo...")
            os.system("cls")
            break

        case _:
            print("Opção inválida...")
            os.system("cls")
            os.system("pause")
        