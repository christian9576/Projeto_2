from notas import ler_nota, listar_notas, salvar_nota


def criar_nova_nota():
    print()
    titulo = input("Titulo da nota: ")
    conteudo = input("Conteudo da nota: ")

    try:
        caminho = salvar_nota(titulo, conteudo)
    except FileExistsError as erro:
        print(f"\nErro: {erro}")
    else:
        print(f"\nNota salva com sucesso em: {caminho}")


def mostrar_notas():
    print()
    notas = listar_notas()

    if not notas:
        print("Nenhuma nota encontrada.")
        return

    print("Notas salvas:")
    for nota in notas:
        print(f"- {nota}")


def mostrar_conteudo_nota():
    print()
    nome_arquivo = input("Nome do arquivo da nota: ")

    try:
        conteudo = ler_nota(nome_arquivo)
    except FileNotFoundError as erro:
        print(f"\nErro: {erro}")
    else:
        print()
        print(conteudo)


def mostrar_menu():
    print()
    print("=== Organizador de Notas ===")
    print("1 - Criar nova nota")
    print("2 - Listar notas")
    print("3 - Ler nota")
    print("4 - Sair")


def main():
    while True:
        mostrar_menu()

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            criar_nova_nota()
        elif opcao == "2":
            mostrar_notas()
        elif opcao == "3":
            mostrar_conteudo_nota()
        elif opcao == "4":
            print("\nSaindo do programa.")
            break
        else:
            print("\nOpcao invalida.")


if __name__ == "__main__":
    main()
