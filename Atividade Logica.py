def bem_vindo():
    print("Bem vindo a sua doaçao de sangue!")
    print("Aqui você aprendera mais sobre a inportancia da sua doação de sangue.\n")

def verificacao():
    print("\nVerificação de Elegibilidade:")
    idade=int(input("Insira sua idade: "))
    peso=int(input("Insira seu (peso em KG): "))
    if idade >= 18 and idade <= 69 and peso >= 50:
        print("Você é apto para doação de sangue")
    elif idade <= 18 and peso >= 50:
        print ("Você precisa de um responsalvel legal o acompanhando.\n")
    else:
        print("Infelizmente, você não atende aos critérios para doação de sangue.")

def locais_doacao():
    print("\nLocais de doalçao:")
    print("1. HEMOCE SEDE - Av. José Bastos, 3390 – Rodolfo Teófilo\n 7h às 17h30min, de segunda a sexta-feira\n 7h às 16h, aos sábados\n 7h às 13h, aos domingos\n ") 
    print("2. HEMOCE PRAÇA DAS FLORES Av. Desembargador Moreira, sn – Aldeota\n 7h às 12h30 e 14h às 16h, de terça a sábado\n ")
    print("3. FUJISAN - Av. Barão de Studart 2626 - Dionisio Torres\n Sangue: Segunda à Sexta das 7:30h às 16:30h e aos Sábados das 7:30h às 13:00h.\n")

def procedimentos():
    print("\nProcedimentos de Doação de Sangue:")
    print("1. Preparação: Hidrate-se e alimente-se bem antes da doação.")
    print("2. Coleta: A coleta dura cerca de 10 a 15 minutos.")
    print("3. Cuidados pós-doação: Descanse por 15 minutos e evite exercícios intensos.\n")

def menu():
    while True:
        print("\nMenu:")
        print("1. Verificação de Elegibilidade")
        print("2. Locais de Doação")
        print("3. Procedimentos de Doação")
        print("4. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            verificacao()
        elif opcao == 2:
            locais_doacao()
        elif opcao == 3:
            procedimentos()
        elif opcao == 4:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

def main():
    bem_vindo()
    menu()

main()