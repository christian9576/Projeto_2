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

    categoria = input("Categoria (opcional, pressione Enter para nenhuma): ")

    conteudo = pedir_conteudo_da_nota()

    if not conteudo.strip():
        print("\nErro: Conteudo nao pode ficar vazio.")
        return

    try:
        caminho = salvar_nota(titulo, conteudo, categoria=categoria)
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


def confirmar(mensagem):
    resposta = input(mensagem)
    return resposta.lower() == "s"


def obter_indice_da_escolha(escolha, quantidade):
    if not escolha.isdigit():
        print("\nErro: Opcao invalida.")
        return None

    indice = int(escolha) - 1

    if indice < 0 or indice >= quantidade:
        print("\nErro: Opcao invalida.")
        return None

    return indice


def mostrar_notas():
    while True:
        print()
        notas = listar_notas()

        if not notas:
            print("Nenhuma nota encontrada.")
            return

        exibir_lista_de_notas(notas)
        print("v - Voltar ao menu principal")

        escolha = input("Escolha uma nota: ")

        if escolha.lower() == "v":
            return

        indice = obter_indice_da_escolha(escolha, len(notas))

        if indice is None:
            continue

        nome_arquivo = notas[indice]
        nota_excluida = mostrar_acoes_da_nota(nome_arquivo)

        if nota_excluida:
            continue


def exibir_lista_de_notas(notas, titulo="Notas salvas:"):
    if not notas:
        print("Nenhuma nota encontrada.")
        return

    print(titulo)
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
                continuar_busca = mostrar_resultados_da_busca(termo)

                if continuar_busca:
                    continue
                else:
                    return

        opcao = input("Digite b para buscar outro termo ou v para voltar: ")

        if opcao.lower() != "b":
            return


def mostrar_resultados_da_busca(termo):
    while True:
        resultados = buscar_notas(termo)

        if not resultados:
            print("\nNenhuma nota encontrada para esse termo.")
            return True

        print()
        exibir_lista_de_notas(resultados, "Resultados encontrados:")
        print("b - Buscar outro termo")
        print("v - Voltar ao menu principal")

        escolha = input("Escolha uma opcao: ")
        escolha_normalizada = escolha.lower()

        if escolha_normalizada == "b":
            return True

        if escolha_normalizada == "v":
            return False

        indice = obter_indice_da_escolha(escolha, len(resultados))

        if indice is None:
            continue

        nome_arquivo = resultados[indice]
        mostrar_acoes_da_nota(nome_arquivo)


def editar_conteudo_da_nota(nome_arquivo):
    try:
        conteudo_atual = ler_nota(nome_arquivo)
    except FileNotFoundError as erro:
        print(f"\nErro: {erro}")
        return False

    print("\nConteudo atual:")
    print(conteudo_atual)

    novo_conteudo = pedir_conteudo_da_nota()

    if not novo_conteudo.strip():
        print("\nErro: Conteudo nao pode ficar vazio.")
        return False

    if not confirmar(f"Tem certeza que deseja substituir o conteudo de {nome_arquivo}? (s/n): "):
        print("\nEdicao cancelada.")
        return False

    try:
        editar_nota(nome_arquivo, novo_conteudo)
    except (FileNotFoundError, ValueError) as erro:
        print(f"\nErro: {erro}")
        return False
    else:
        print(f"\nSucesso: Nota editada: {nome_arquivo}")
        return True


def editar_titulo_da_nota(nome_atual):
    novo_titulo = input("Novo titulo da nota: ")

    if not novo_titulo.strip():
        print("\nErro: Titulo nao pode ficar vazio.")
        return None

    novo_nome = formatar_nome_arquivo(novo_titulo)
    if not confirmar(f"Tem certeza que deseja renomear {nome_atual} para {novo_nome}? (s/n): "):
        print("\nRenomeacao cancelada.")
        return None

    try:
        novo_caminho = editar_titulo_nota(nome_atual, novo_titulo)
    except (FileExistsError, FileNotFoundError, ValueError) as erro:
        print(f"\nErro: {erro}")
        return None
    else:
        print(f"\nSucesso: Nota renomeada para: {novo_caminho.name}")
        return novo_caminho.name


def mostrar_submenu_edicao():
    print()
    print("1 - Editar conteudo")
    print("2 - Editar titulo")
    print("3 - Voltar")


def executar_edicao_da_nota(nome_arquivo):
    mostrar_submenu_edicao()
    opcao_edicao = input("Escolha uma opcao: ")

    if opcao_edicao == "1":
        conteudo_editado = editar_conteudo_da_nota(nome_arquivo)

        if conteudo_editado:
            editar_titulo = input("Deseja editar o titulo desta nota tambem? (s/n): ")

            if editar_titulo.lower() == "s":
                novo_nome = editar_titulo_da_nota(nome_arquivo)

                if novo_nome:
                    return novo_nome
    elif opcao_edicao == "2":
        novo_nome = editar_titulo_da_nota(nome_arquivo)

        if novo_nome:
            nome_arquivo = novo_nome
            editar_conteudo = input("Deseja editar o conteudo desta nota tambem? (s/n): ")

            if editar_conteudo.lower() == "s":
                editar_conteudo_da_nota(nome_arquivo)
    elif opcao_edicao == "3":
        pass
    else:
        print("\nErro: Opcao invalida.")

    return nome_arquivo


def mostrar_submenu_acoes_da_nota():
    print()
    print("1 - Ler nota")
    print("2 - Editar nota")
    print("3 - Excluir nota")
    print("4 - Voltar")


def ler_nota_selecionada(nome_arquivo):
    try:
        conteudo = ler_nota(nome_arquivo)
    except FileNotFoundError as erro:
        print(f"\nErro: {erro}")
    else:
        print()
        print(conteudo)


def excluir_nota_selecionada(nome_arquivo):
    if not confirmar(f"Tem certeza que deseja excluir {nome_arquivo}? (s/n): "):
        print("\nExclusao cancelada.")
        return False

    try:
        excluir_nota(nome_arquivo)
    except FileNotFoundError as erro:
        print(f"\nErro: {erro}")
        return False
    else:
        print(f"\nSucesso: Nota excluida: {nome_arquivo}")
        return True


def mostrar_acoes_da_nota(nome_arquivo):
    while True:
        mostrar_submenu_acoes_da_nota()
        escolha = input("Escolha uma opcao: ")

        if escolha == "1":
            ler_nota_selecionada(nome_arquivo)
        elif escolha == "2":
            nome_arquivo = executar_edicao_da_nota(nome_arquivo)
        elif escolha == "3":
            nota_excluida = excluir_nota_selecionada(nome_arquivo)

            if nota_excluida:
                return True
        elif escolha == "4":
            return False
        else:
            print("\nErro: Opcao invalida.")


def mostrar_menu():
    print()
    print("=== Organizador de Notas ===")
    print("1 - Criar nova nota")
    print("2 - Listar notas")
    print("3 - Buscar notas")
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
            buscar_notas_por_termo()
        elif opcao == "4":
            print("\nSaindo...")
            break
        else:
            print("\nErro: Opcao invalida.")


if __name__ == "__main__":
    main()
