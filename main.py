from notas import buscar_notas, excluir_nota, ler_nota, listar_notas, salvar_nota


def criar_nova_nota():
    print()
    titulo = input("Titulo da nota: ")

    if not titulo.strip():
        print("\nErro: Titulo nao pode ficar vazio.")
        return

    conteudo = pedir_conteudo_da_nota()

    if not conteudo.strip():
        print("\nErro: Conteudo nao pode ficar vazio.")
        return

    try:
        caminho = salvar_nota(titulo, conteudo)
    except (FileExistsError, ValueError) as erro:
        print(f"\nErro: {erro}")
    else:
        print(f"\nSucesso: Nota salva em: {caminho}")


def pedir_conteudo_da_nota():
    print("Digite o conteudo da nota. Para finalizar, pressione Enter em uma linha vazia.")

    linhas = []

    while True:
        linha = input()

        if linha == "":
            break

        linhas.append(linha)

    return "\n".join(linhas)


def mostrar_notas():
    print()
    notas = listar_notas()
    exibir_lista_de_notas(notas)


def exibir_lista_de_notas(notas):
    if not notas:
        print("Nenhuma nota encontrada.")
        return

    print("Notas salvas:")
    for numero, nota in enumerate(notas, start=1):
        print(f"{numero} - {nota}")


def buscar_notas_por_termo():
    while True:
        print()
        termo = input("Termo de busca: ")

        try:
            resultados = buscar_notas(termo)
        except ValueError as erro:
            print(f"\nErro: {erro}")
        else:
            if not resultados:
                print("\nNenhuma nota encontrada para esse termo.")
            else:
                continuar_busca = mostrar_resultados_da_busca(resultados)

                if continuar_busca:
                    continue
                else:
                    return

        opcao = input("Deseja buscar outro termo? (s/n): ")

        if opcao.lower() != "s":
            return


def mostrar_resultados_da_busca(resultados):
    while True:
        print("\nResultados encontrados:")
        for numero, nota in enumerate(resultados, start=1):
            print(f"{numero} - {nota}")

        print("b - Buscar outro termo")
        print("v - Voltar ao menu principal")

        escolha = input("Escolha uma opcao: ")
        escolha_normalizada = escolha.lower()

        if escolha_normalizada == "b":
            return True

        if escolha_normalizada == "v":
            return False

        if not escolha.isdigit():
            print("\nErro: Opcao invalida.")
            continue

        indice = int(escolha) - 1

        if indice < 0 or indice >= len(resultados):
            print("\nErro: Opcao invalida.")
            continue

        nome_arquivo = resultados[indice]

        try:
            conteudo = ler_nota(nome_arquivo)
        except FileNotFoundError as erro:
            print(f"\nErro: {erro}")
        else:
            print()
            print(conteudo)


def mostrar_conteudo_nota():
    while True:
        print()
        notas = listar_notas()

        if not notas:
            print("Nenhuma nota encontrada.")
            return

        exibir_lista_de_notas(notas)

        escolha = input("Digite o numero da nota: ")

        if not escolha.isdigit():
            print("\nErro: Opcao invalida.")
        else:
            indice = int(escolha) - 1

            if indice < 0 or indice >= len(notas):
                print("\nErro: Opcao invalida.")
            else:
                nome_arquivo = notas[indice]

                try:
                    conteudo = ler_nota(nome_arquivo)
                except FileNotFoundError as erro:
                    print(f"\nErro: {erro}")
                else:
                    print()
                    print(conteudo)

        continuar = input("Deseja ler outra nota? (s/n): ")

        if continuar.lower() != "s":
            return


def excluir_nota_por_numero():
    print()
    notas = listar_notas()

    if not notas:
        print("Nenhuma nota encontrada.")
        return

    exibir_lista_de_notas(notas)

    escolha = input("Digite o numero da nota: ")

    if not escolha.isdigit():
        print("\nErro: Opcao invalida.")
        return

    indice = int(escolha) - 1

    if indice < 0 or indice >= len(notas):
        print("\nErro: Opcao invalida.")
        return

    nome_arquivo = notas[indice]
    confirmacao = input(f"Tem certeza que deseja excluir {nome_arquivo}? (s/n): ")

    if confirmacao.lower() != "s":
        print("\nExclusao cancelada.")
        return

    try:
        excluir_nota(nome_arquivo)
    except FileNotFoundError as erro:
        print(f"\nErro: {erro}")
    else:
        print(f"\nSucesso: Nota excluida: {nome_arquivo}")


def mostrar_menu():
    print()
    print("=== Organizador de Notas ===")
    print("1 - Criar nova nota")
    print("2 - Listar notas")
    print("3 - Ler nota")
    print("4 - Buscar notas")
    print("5 - Excluir nota")
    print("6 - Sair")


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
            buscar_notas_por_termo()
        elif opcao == "5":
            excluir_nota_por_numero()
        elif opcao == "6":
            print("\nSaindo...")
            break
        else:
            print("\nErro: Opcao invalida.")


if __name__ == "__main__":
    main()
