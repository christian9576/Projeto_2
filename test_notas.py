from pathlib import Path

import pytest

from notas import formatar_nome_arquivo, ler_nota, listar_notas, salvar_nota


def test_formatar_nome_arquivo():
    nome = formatar_nome_arquivo("Minha Primeira Nota")

    assert nome == "minha-primeira-nota.md"


def test_salvar_nota_cria_arquivo(tmp_path):
    caminho = salvar_nota("Python Arquivos", "Conteudo da nota", tmp_path)

    assert caminho == tmp_path / "python-arquivos.md"
    assert caminho.exists()
    assert caminho.read_text(encoding="utf-8") == "# Python Arquivos\n\nConteudo da nota\n"


def test_salvar_nota_nao_sobrescreve_arquivo_existente(tmp_path):
    salvar_nota("Nota Repetida", "Primeiro conteudo", tmp_path)

    with pytest.raises(FileExistsError):
        salvar_nota("Nota Repetida", "Segundo conteudo", tmp_path)


def test_listar_notas_retorna_arquivos_md_em_ordem_alfabetica(tmp_path):
    salvar_nota("Zebra", "Conteudo", tmp_path)
    salvar_nota("Abacate", "Conteudo", tmp_path)
    Path(tmp_path / "rascunho.txt").write_text("Nao deve aparecer", encoding="utf-8")

    notas = listar_notas(tmp_path)

    assert notas == ["abacate.md", "zebra.md"]


def test_listar_notas_retorna_lista_vazia_quando_nao_ha_notas(tmp_path):
    notas = listar_notas(tmp_path)

    assert notas == []


def test_ler_nota_retorna_conteudo_de_nota_existente(tmp_path):
    salvar_nota("Nota Para Ler", "Conteudo para leitura", tmp_path)

    conteudo = ler_nota("nota-para-ler.md", tmp_path)

    assert conteudo == "# Nota Para Ler\n\nConteudo para leitura\n"


def test_ler_nota_gera_erro_para_nota_inexistente(tmp_path):
    with pytest.raises(FileNotFoundError, match="Nota nao encontrada."):
        ler_nota("nao-existe.md", tmp_path)


def test_salvar_nota_gera_erro_para_titulo_vazio(tmp_path):
    with pytest.raises(ValueError, match="Titulo nao pode ficar vazio."):
        salvar_nota("", "Conteudo valido", tmp_path)

    assert list(tmp_path.glob("*.md")) == []


def test_salvar_nota_gera_erro_para_titulo_com_espacos(tmp_path):
    with pytest.raises(ValueError, match="Titulo nao pode ficar vazio."):
        salvar_nota("   ", "Conteudo valido", tmp_path)

    assert list(tmp_path.glob("*.md")) == []


def test_salvar_nota_gera_erro_para_conteudo_vazio(tmp_path):
    with pytest.raises(ValueError, match="Conteudo nao pode ficar vazio."):
        salvar_nota("Titulo valido", "", tmp_path)

    assert list(tmp_path.glob("*.md")) == []


def test_salvar_nota_gera_erro_para_conteudo_com_espacos(tmp_path):
    with pytest.raises(ValueError, match="Conteudo nao pode ficar vazio."):
        salvar_nota("Titulo valido", "   ", tmp_path)

    assert list(tmp_path.glob("*.md")) == []
