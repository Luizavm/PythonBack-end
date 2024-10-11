import os
from funções import *

animais = []

while True:
    while True:
        try:
            escolha = menu()
            os.system("cls")
            break

        except Exception as e:
            print(f"Valor incorreto, erro {e}")
            os.system("pause")
            os.system("cls")

    match escolha:
        case 1:
            while True:
                while True:
                    try:
                        cadastro_ = cadastro()
                        os.system("cls")
                        break

                    except Exception as e:
                        print(f"Valor incorreto, erro {e}")
                        os.system("pause")
                        os.system("cls")

                match cadastro_:
                    case 1:
                        animal1()
                        os.system("pause")
                        break
                    case 2:
                        animal2()
                        os.system("pause")
                        break
                    case 3:
                        print("Voltando...")
                        os.system("cls")
                        os.system("pause")
                        break
                    case _:
                        print("Opção inválida")
                        os.system("pause")
        
        case 2:
            while True:
                while True:
                    try:
                        listarani = listar()
                        os.system("cls")
                        break

                    except Exception as e:
                        print(f"Valor incorreto, erro {e}")
                        os.system("pause")
                        os.system("cls")

                match listarani:
                    case 1:
                        todosanimais()
                        os.system("pause")
                        break
                    case 2:
                        listdog()
                        os.system("pause")
                        break
                    case 3:
                        listcat()
                        os.system("pause")
                        break
                    case 4:
                        print("Voltando...")
                        os.system("cls")
                        os.system("pause")
                        break
                    case _:
                        print("Opção inválida")
                        os.system("pause")

        case 3:
            while True:
                while True:
                    try:
                        consultani1 = consultani()
                        os.system("cls")
                        break

                    except Exception as e:
                        print(f"Valor incorreto, erro {e}")
                        os.system("pause")
                        os.system("cls")

                match consultani1:
                    case 1:
                        digani()
                        os.system("pause")
                        break
                    case 2:
                        verificdig()
                        os.system("pause")
                        break
                    case 3:
                        print("Voltando...")
                        os.system("cls")
                        os.system("pause")
                        break
                    case _:
                        print("Opção inválida")
                        os.system("pause")





