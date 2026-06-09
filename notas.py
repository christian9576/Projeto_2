from pathlib import Path


PASTA_NOTAS = Path("notas")


def criar_pasta_notas():
    PASTA_NOTAS.mkdir(exist_ok=True)


def formatar_nome_arquivo(titulo):
    nome = titulo.strip().lower()
    nome = nome.replace(" ", "-")
    return f"{nome}.md"


def salvar_nota(titulo, conteudo):
    criar_pasta_notas()

    nome_arquivo = formatar_nome_arquivo(titulo)
    caminho = PASTA_NOTAS / nome_arquivo

    if caminho.exists():
        raise FileExistsError("Ja existe uma nota com esse titulo.")

    texto_da_nota = f"# {titulo}\n\n{conteudo}\n"
    caminho.write_text(texto_da_nota, encoding="utf-8")

    return caminho


def listar_notas():
    criar_pasta_notas()

    arquivos = PASTA_NOTAS.glob("*.md")
    nomes_das_notas = [arquivo.name for arquivo in arquivos]

    return sorted(nomes_das_notas)
