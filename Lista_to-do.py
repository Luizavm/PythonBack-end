import os
from secondcode import *

x = 0 

while x == 0:
    Escini = telainic("escolha1")

    if Escini == 1:
        add = if1("tarefas")
        print("")

    elif Escini == 2: 
        add2 = if2("tarefas")

    elif Escini == 3:
        add3 = if3("tarefas")

    elif Escini == 4:
        add4 = if4()
    
    else:
        print("Essa escolha não existe...")
        os.system("cls")

        