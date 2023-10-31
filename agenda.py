def salvar_contatos(lista):
    arquivo = open("contatos.txt", "w")

    for contato in lista:
        arquivo.write("{}#{}#{}\n".format(contato['nome'], contato['email'], contato['telefone']))
        
    arquivo.close()

def carregar_contatos():
    lista = []

    try:
        with open("contatos.txt", "r") as arquivo:
    
            for linha in arquivo.readlines():
                coluna = linha.strip().split("#")
                if len(coluna) == 3:
                    contato = {
                    "email": coluna[1],
                    "nome": coluna[0],
                    "telefone": coluna[2]
                }

                lista.append(contato)

    except FileNotFoundError:
        pass

    return lista

def email_usado(lista, email):
    if len(lista) > 0:
        for contato in lista:
            if contato ['email'] == email:
                return True
    
    return False

def adicionar(lista):
    
    while True:
        email = input("Digite o e-mail do contato:")
    
        if not email_usado(lista, email):
            break
        else:
            print("Esse email já foi utilizado.")
            print("Por favor, tente um novo e-mail")
    
    contato = {
        "email": email,
        "nome": input("Digite o nome:"),
        "telefone": input("Digite o telefone:")
    }

    lista.append(contato)
    
    print("\nO contato {} foi cadastrado com sucesso\n".format(contato['nome']))

def alterar(lista):
    print("## ALTERAR CONTATO ##")
    if len(lista) > 0:   
        email = input("Digite o email do contato para ser alterado:")
        email = email.lower()
        found = False
        for contato in lista:
            if contato['email'].lower() == email:
                print("\nO seu contato foi encontrado. Informações abaixo:\n")
                print("="*33)
                print("Nome: {}".format(contato['nome']))
                print("Email: {}".format(contato['email']))
                print("Telefone: {}".format(contato['telefone']))
                print("="*33)

                contato['nome'] = input("Digite o novo nome do contato:")
                contato['telefone'] = input("Digite o novo telefone do contato:")

                print("\nOs dados do contato com o email {} foram alterados com sucesso!\n".format(contato['email']))
                found = True
                break
        if not found:
            print("Não existe nenhum contato cadastrado no sistema com o email {}\n".format(email))
    
    else:
        print("Não existe nenhum contato cadastrado no sistema\n")

def excluir(lista):
    print("## EXCLUIR CONTATO ##")
    if len(lista) > 0:   
        email = input("Digite o email do contato para ser excluído:")
        email = email.lower()
        found = False
        for i, contato in enumerate(lista):
            if contato['email'].lower() == email:
                print("="*33)
                print("\nO seu contato foi encontrado. Informações abaixo:\n")
                print("="*33)
                print("Nome: {}".format(contato['nome']))
                print("Email: {}".format(contato['email']))
                print("Telefone: {}\n".format(contato['telefone']))
                
                del lista[i]

                print("O contato foi apagado com sucesso!\n")
                print("="*33)
                
                found = True
                break
        if not found:
            print("Não existe nenhum contato cadastrado no sistema com o email {}\n".format(email))
    
    else:
        print("Não existe nenhum contato cadastrado no sistema\n")

def buscar(lista):
    print("## Buscar Contato ##")
    if len(lista) > 0:   
        email = input("Digite o email do contato para ser encontrado:")
        email = email.lower()
        found = False
        for contato in lista:
            if contato['email'].lower() == email:
                print("="*33)
                print("\nO seu contato foi encontrado. Informações abaixo:\n")
                print("Nome: {}".format(contato['nome']))
                print("Email: {}".format(contato['email']))
                print("Telefone: {}".format(contato['telefone']))
                print("="*33)
                found = True
                break
        if not found:
            print("Não existe nenhum contato cadastrado no sistema com o email {}\n".format(email))
    
    else:
        print("Não existe nenhum contato cadastrado no sistema\n")

       
def listar(lista):
    print("## Listar Contatos ##")
    if len(lista) > 0:
        for i, contato in enumerate(lista):
            print("Contato: {}".format(i+1))
            print("\tNome: {}".format(contato['nome']))
            print("\tEmail: {}".format(contato['email']))
            print("\tTelefone: {}".format(contato['telefone']))
        
        print("Quantidade de contatos: {}\n".format(len(lista)))
    else:
        print("Não exite nenhum contato cadastrado no sistema.\n")   


def principal():

    lista = carregar_contatos()
    
    while True:
        print("\nAGENDA DE CONTATOS")
        print("")
        print(" 1 - Adicionar Contato")
        print(" 2 - Alterar Contato")
        print(" 3 - Excluir Contato")
        print(" 4 - Buscar Contato")
        print(" 5 - Listar Contatos")
        print(" 6 - Sair")
        
        while True:
            try:
                opção = int(input("\nEscolha uma das opções acima:"))
                if opção in (1, 2, 3, 4, 5, 6):
                    break 
                else:
                    print("Opção inválida. Por favor, tente novamente.")
            except ValueError:
                print("Opção inválida. Por favor, tente novamente.")

        if opção == 1:
            adicionar(lista)
            salvar_contatos(lista)
        elif opção == 2:
            alterar(lista)
            salvar_contatos(lista)
        elif opção == 3:
            excluir(lista)
            salvar_contatos(lista)
        elif opção == 4:
            buscar(lista)
        elif opção == 5:
            listar(lista)
        elif opção == 6:
            print("Saindo do programa...")
            break
        else: 
            print("\nOpção inválida. Por favor, tente novamente.")
        
        while True:
            continuar = input("Deseja continuar (S) ou sair (N)?").strip().lower()
            if continuar == 's':
                break
            elif continuar =='n':
                print("Saindo da agenda, até logo...")
                return
            else:
                print("Opção inválida. Digite 'S' para continuar ou 'N' para sair.")

principal()