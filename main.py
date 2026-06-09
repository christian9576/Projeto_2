from notas import (
    buscar_notas,
    editar_nota,
    editar_titulo_nota,
    excluir_nota,
    formatar_nome_arquivo,
    ler_nota,
    listar_notas,
    salvar_nota,
)


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
                confirmacao = input(f"Tem certeza que deseja excluir {nome_arquivo}? (s/n): ")

                if confirmacao.lower() != "s":
                    print("\nExclusao cancelada.")
                else:
                    try:
                        excluir_nota(nome_arquivo)
                    except FileNotFoundError as erro:
                        print(f"\nErro: {erro}")
                    else:
                        print(f"\nSucesso: Nota excluida: {nome_arquivo}")

        continuar = input("Deseja excluir outra nota? (s/n): ")

        if continuar.lower() != "s":
            return


def editar_nota_por_numero():
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

    try:
        conteudo_atual = ler_nota(nome_arquivo)
    except FileNotFoundError as erro:
        print(f"\nErro: {erro}")
        return

    print("\nConteudo atual:")
    print(conteudo_atual)

    novo_conteudo = pedir_conteudo_da_nota()

    if not novo_conteudo.strip():
        print("\nErro: Conteudo nao pode ficar vazio.")
        return

    confirmacao = input(f"Tem certeza que deseja substituir o conteudo de {nome_arquivo}? (s/n): ")

    if confirmacao.lower() != "s":
        print("\nEdicao cancelada.")
        return

    try:
        editar_nota(nome_arquivo, novo_conteudo)
    except (FileNotFoundError, ValueError) as erro:
        print(f"\nErro: {erro}")
    else:
        print(f"\nSucesso: Nota editada: {nome_arquivo}")


def editar_titulo_nota_por_numero():
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

    nome_atual = notas[indice]
    novo_titulo = input("Novo titulo da nota: ")

    if not novo_titulo.strip():
        print("\nErro: Titulo nao pode ficar vazio.")
        return

    novo_nome = formatar_nome_arquivo(novo_titulo)
    confirmacao = input(f"Tem certeza que deseja renomear {nome_atual} para {novo_nome}? (s/n): ")

    if confirmacao.lower() != "s":
        print("\nRenomeacao cancelada.")
        return

    try:
        novo_caminho = editar_titulo_nota(nome_atual, novo_titulo)
    except (FileExistsError, FileNotFoundError, ValueError) as erro:
        print(f"\nErro: {erro}")
    else:
        print(f"\nSucesso: Nota renomeada para: {novo_caminho.name}")


def mostrar_menu():
    print()
    print("=== Organizador de Notas ===")
    print("1 - Criar nova nota")
    print("2 - Listar notas")
    print("3 - Ler nota")
    print("4 - Buscar notas")
    print("5 - Excluir nota")
    print("6 - Editar nota")
    print("7 - Editar titulo da nota")
    print("8 - Sair")


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
            editar_nota_por_numero()
        elif opcao == "7":
            editar_titulo_nota_por_numero()
        elif opcao == "8":
            print("\nSaindo...")
            break
        else:
            print("\nErro: Opcao invalida.")


if __name__ == "__main__":
    main()
