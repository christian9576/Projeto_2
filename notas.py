from pathlib import Path


PASTA_NOTAS = Path("notas")


def criar_pasta_notas(pasta=PASTA_NOTAS):
    pasta.mkdir(exist_ok=True)


def formatar_nome_arquivo(titulo):
    nome = titulo.strip().lower()
    nome = nome.replace(" ", "-")
    return f"{nome}.md"


def salvar_nota(titulo, conteudo, pasta=PASTA_NOTAS):
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
