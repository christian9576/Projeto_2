from notas import salvar_nota


def main():
    titulo = input("Titulo da nota: ")
    conteudo = input("Conteudo da nota: ")

    try:
        caminho = salvar_nota(titulo, conteudo)
    except FileExistsError as erro:
        print(f"Erro: {erro}")
    else:
        print(f"Nota salva com sucesso em: {caminho}")


if __name__ == "__main__":
    main()
