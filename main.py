import time
import os

def main():
    action = 1

    while True:
        clearTerminal()
        print("Ação: ", action)
        if action == 1:
            action = menu()
        elif action == 2:
            print("Ação 2")
        elif action == 3:
            print("Ação 3")
        elif action == 0:
            close()

    
def clearTerminal():
    os.system('cls||clear')


def menu():
    print("---------------------------------------------")
    print("  Bem-vindo(a) a Cliníca de Consultas Ágil!  ")
    print("---------------------------------------------\n")
    
    option = -1
    while True:
        print("Essas são as ações possíveis:\n")
        print("1 - Cadastrar um paciente")
        print("2 - Marcar uma consulta")
        print("3 - Cancelar uma consultas")
        print("0 - Sair\n")

        try:
            option = int(input("Digite o número da ação desejada: "))
            if option >= 0 and option <= 3:
                break
            else:
                print("Opção inválida! Tente novamente.")
                time.sleep(2)
                clearTerminal()

        except ValueError:
            print("\nDigite apenas números!\n")
            time.sleep(2)
            clearTerminal()
    
    if option == 0:
        return 0
    else:
        return option + 1
    

def registerPatient():
    name = ""
    phone = ""


def scheduleAppointment():


def close():
    print("\nObrigado por usar o sistema!\n")
    time.sleep(2)
    exit()


main()