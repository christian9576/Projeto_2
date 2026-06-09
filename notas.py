from pathlib import Path


PASTA_NOTAS = Path("notas")


def criar_pasta_notas(pasta=PASTA_NOTAS):
    pasta.mkdir(exist_ok=True)


def formatar_nome_arquivo(titulo):
    nome = titulo.strip().lower()
    nome = nome.replace(" ", "-")
    return f"{nome}.md"


def salvar_nota(titulo, conteudo, pasta=PASTA_NOTAS):
    if not titulo.strip():
        raise ValueError("Titulo nao pode ficar vazio.")

    if not conteudo.strip():
        raise ValueError("Conteudo nao pode ficar vazio.")

    criar_pasta_notas(pasta)

    nome_arquivo = formatar_nome_arquivo(titulo)
    caminho = pasta / nome_arquivo

    if caminho.exists():
        raise FileExistsError("Ja existe uma nota com esse titulo.")

    texto_da_nota = f"# {titulo}\n\n{conteudo}\n"
    caminho.write_text(texto_da_nota, encoding="utf-8")

    return caminho


def listar_notas(pasta=PASTA_NOTAS):
    criar_pasta_notas(pasta)

    arquivos = pasta.glob("*.md")
    nomes_das_notas = [arquivo.name for arquivo in arquivos]

    return sorted(nomes_das_notas)


def ler_nota(nome_arquivo, pasta=PASTA_NOTAS):
    criar_pasta_notas(pasta)

    caminho = pasta / Path(nome_arquivo).name

    if not caminho.exists():
        raise FileNotFoundError("Nota nao encontrada.")

    return caminho.read_text(encoding="utf-8")


def buscar_notas(termo, pasta=PASTA_NOTAS):
    if not termo.strip():
        raise ValueError("Termo de busca nao pode ficar vazio.")

    criar_pasta_notas(pasta)

    termo_normalizado = termo.strip().lower()
    notas_encontradas = []

    for caminho in pasta.glob("*.md"):
        nome_normalizado = caminho.name.lower()
        conteudo_normalizado = caminho.read_text(encoding="utf-8").lower()

        if termo_normalizado in nome_normalizado or termo_normalizado in conteudo_normalizado:
            notas_encontradas.append(caminho.name)

    return sorted(notas_encontradas)
