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


if __name__ == "__main__":
    main()