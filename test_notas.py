from pathlib import Path

import pytest

from notas import formatar_nome_arquivo, listar_notas, salvar_nota


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
