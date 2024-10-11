import os
from classeherança import contacorrente, contapoupanca 

def menu():
    print("Conta no banco \nBem-vindo!")
    print("01 - Cadastrar conta")
    print("02 - Já tenho uma conta")
    print("03 - SAIR")
    print("")

def login():
    escolhacorr = int(input("Insira o valor  que você deseja sacar:"))
                                    
    if escolhacorr <= saldo:
        saldo -= escolhacorr
        print(f"Saque de R$ {escolhacorr:.2f} realizado com sucesso.")
                                    
    else:
        print("Saldo insuficiente...")
        os.system("cls")
        os.system("pause")




        
    






