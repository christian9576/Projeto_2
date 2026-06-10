from pathlib import Path


PASTA_NOTAS = Path("notas")


def criar_pasta_notas(pasta=PASTA_NOTAS):
    pasta.mkdir(parents=True, exist_ok=True)


def formatar_nome_arquivo(titulo):
    nome = titulo.strip().lower()
    nome = nome.replace(" ", "-")
    return f"{nome}.md"


def formatar_categoria(categoria):
    nome = categoria.strip().lower()
    nome = nome.replace(" ", "-")
    return nome


def salvar_nota(titulo, conteudo, pasta=PASTA_NOTAS, categoria=None):
    if not titulo.strip():
        raise ValueError("Titulo nao pode ficar vazio.")

    if not conteudo.strip():
        raise ValueError("Conteudo nao pode ficar vazio.")

    pasta_destino = pasta

    if categoria and categoria.strip():
        pasta_destino = pasta / formatar_categoria(categoria)

    criar_pasta_notas(pasta_destino)

    nome_arquivo = formatar_nome_arquivo(titulo)
    caminho = pasta_destino / nome_arquivo

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


def excluir_nota(nome_arquivo, pasta=PASTA_NOTAS):
    criar_pasta_notas(pasta)

    caminho = pasta / Path(nome_arquivo).name

    if not caminho.exists():
        raise FileNotFoundError("Nota nao encontrada.")

    caminho.unlink()

    return caminho


def editar_nota(nome_arquivo, novo_conteudo, pasta=PASTA_NOTAS):
    if not novo_conteudo.strip():
        raise ValueError("Conteudo nao pode ficar vazio.")

    criar_pasta_notas(pasta)

    caminho = pasta / Path(nome_arquivo).name

    if not caminho.exists():
        raise FileNotFoundError("Nota nao encontrada.")

    conteudo_atual = caminho.read_text(encoding="utf-8")
    linhas_atuais = conteudo_atual.splitlines()
    primeira_linha = linhas_atuais[0] if linhas_atuais else f"# {caminho.stem}"
    novo_texto = f"{primeira_linha}\n\n{novo_conteudo}\n"

    caminho.write_text(novo_texto, encoding="utf-8")

    return caminho


def editar_titulo_nota(nome_arquivo_atual, novo_titulo, pasta=PASTA_NOTAS):
    if not novo_titulo.strip():
        raise ValueError("Titulo nao pode ficar vazio.")

    criar_pasta_notas(pasta)

    caminho_atual = pasta / Path(nome_arquivo_atual).name

    if not caminho_atual.exists():
        raise FileNotFoundError("Nota nao encontrada.")

    titulo_limpo = novo_titulo.strip()
    novo_nome_arquivo = formatar_nome_arquivo(titulo_limpo)
    novo_caminho = pasta / novo_nome_arquivo

    if novo_caminho != caminho_atual and novo_caminho.exists():
        raise FileExistsError("Ja existe uma nota com esse titulo.")

    conteudo_atual = caminho_atual.read_text(encoding="utf-8")
    linhas = conteudo_atual.splitlines()
    novo_titulo_markdown = f"# {titulo_limpo}"

    if linhas and linhas[0].startswith("# "):
        linhas[0] = novo_titulo_markdown
        novo_conteudo = "\n".join(linhas)
    elif conteudo_atual:
        novo_conteudo = f"{novo_titulo_markdown}\n\n{conteudo_atual}"
    else:
        novo_conteudo = novo_titulo_markdown

    caminho_atual.write_text(f"{novo_conteudo}\n", encoding="utf-8")

    if novo_caminho != caminho_atual:
        caminho_atual.rename(novo_caminho)

    return novo_caminho
