from notas import listar_notas, salvar_nota


def criar_nova_nota():
    titulo = input("Titulo da nota: ")
    conteudo = input("Conteudo da nota: ")

    try:
        caminho = salvar_nota(titulo, conteudo)
    except FileExistsError as erro:
        print(f"Erro: {erro}")
    else:
        print(f"Nota salva com sucesso em: {caminho}")


def mostrar_notas():
    notas = listar_notas()

    if not notas:
        print("Nenhuma nota encontrada.")
        return

    print("Notas salvas:")
    for nota in notas:
        print(f"- {nota}")


def main():
    while True:
        print("1 - Criar nova nota")
        print("2 - Listar notas")
        print("3 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            criar_nova_nota()
        elif opcao == "2":
            mostrar_notas()
        elif opcao == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
