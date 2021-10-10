def printLinhas():
    print("-=" * 30)


def menu():
    while True:
        try:
            printLinhas()
            op = int(input("""O que deseja fazer?
[ 1 ] Cadastrar um novo usuário
[ 2 ] Exibir usuários por ordem de cadastro
[ 3 ] Exibir usuários por ordem alfabética
[ 4 ] Pesquisar usuário pelo nome
[ 5 ] Remover usuário
[ 6 ] Atualizar cadastro de um usuário
[ 7 ] Finalizar programa
Sua opção: """))
            printLinhas()
            if op >= 1 and op <= 7:
                return op
            print("Insira um valor entre 1 e 7.")
        except ValueError:
            print("Insira um valor numérico inteiro!")

def postUsuario(usuarios):
    printLinhas()
    nome = input("Informe o nome completo: ").strip().capitalize()
    email = input(f"Informe o email de {nome.split()[0]}: ").strip()
    while True:
        if any(i['email'] == email for i in usuarios):
            print("Email já cadastrado!")
            email = input("Informe o email a ser cadastrado: ").strip()
        else:
            break
    print('Usuário cadastrado com sucesso!')
    printLinhas()
    return {"nome": nome, "email": email}


def getAllUsuarios(usuarios):
    printLinhas()
    for i in usuarios:
        print(i['nome'], end = ' -> ')
        print(i['email'])
    printLinhas()

    
if __name__ == "__main__":
    main()