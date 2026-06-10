# Guia Modulo 2 - Projeto 2

## Objetivo do projeto

O Projeto 2 foi uma mini CLI local em Python para organizar notas.

O objetivo principal foi aprender persistencia de dados usando arquivos: criar, salvar, ler, listar, buscar, editar e excluir notas `.md` no computador.

## Principais conceitos aprendidos

### Persistencia de dados

Persistencia significa guardar informacoes para que elas continuem existindo depois que o programa termina.

Neste projeto, as notas foram persistidas como arquivos `.md` dentro da pasta `notas/`.

### Criacao de pastas com Python

Foi usado `pathlib.Path` para trabalhar com caminhos.

A pasta `notas/` e criada automaticamente quando necessario.

Tambem foi iniciado o suporte a categorias, criando subpastas dentro de `notas/`.

### Salvar arquivos `.md`

Cada nota e salva como um arquivo Markdown.

O titulo vira o nome do arquivo, e o conteudo fica dentro do arquivo.

### Ler arquivos

O programa consegue abrir uma nota existente e mostrar seu conteudo no terminal.

### Listar arquivos

O programa consegue procurar arquivos `.md` dentro da pasta `notas/` e mostrar uma lista numerada.

### Buscar em arquivos

A busca procura um termo no nome do arquivo e no conteudo da nota.

A busca ignora diferenca entre letras maiusculas e minusculas.

### Editar arquivos

O projeto permite editar o conteudo da nota e tambem editar o titulo.

Editar titulo envolve renomear o arquivo e atualizar a primeira linha Markdown.

### Excluir arquivos

Excluir nota remove o arquivo do computador.

Como e uma acao destrutiva, o programa pede confirmacao antes.

### Evitar sobrescrever arquivos

Antes de salvar uma nota, o programa verifica se ja existe um arquivo com o mesmo nome.

Se existir, mostra erro em vez de sobrescrever.

### Validacoes

O programa valida entradas importantes, como:

- titulo vazio;
- conteudo vazio;
- termo de busca vazio;
- opcao invalida no menu;
- numero fora da lista.

### Tratamento de erros

Foram usados erros como `ValueError`, `FileNotFoundError` e `FileExistsError`.

O `notas.py` gera os erros, e o `main.py` mostra mensagens amigaveis para o usuario.

### Testes com pytest

O projeto usa `pytest` para testar as funcoes principais.

Os testes ajudam a garantir que salvar, listar, ler, buscar, editar e excluir continuam funcionando depois de mudancas.

### `tmp_path`

Nos testes, `tmp_path` cria uma pasta temporaria.

Isso permite testar arquivos sem mexer nas notas reais do projeto.

### Refatoracao

Refatorar e reorganizar o codigo sem mudar o comportamento.

No projeto, o `main.py` foi reorganizado para reduzir repeticao e deixar os fluxos mais faceis de manter.

### Git/GitHub

Git foi usado para acompanhar mudancas no projeto.

GitHub serve para guardar o repositorio online e mostrar a evolucao do trabalho.

### Codex em fatias pequenas

O projeto evoluiu por pequenas entregas.

Cada prompt pediu uma melhoria clara, com limites bem definidos. Isso ajudou a evitar complexidade cedo demais.

## Fluxo de desenvolvimento usado

1. Definir um MVP pequeno.
2. Criar um prompt claro para o Codex.
3. Revisar o diff das mudancas.
4. Testar manualmente no terminal.
5. Rodar os testes com:

```bash
python -m pytest
```

6. Fazer commit com uma mensagem clara.
7. Fazer push para o GitHub.

## Modelos mentais importantes

### `main.py`

Cuida da interacao com o usuario.

Ele mostra menus, pede entradas e exibe mensagens no terminal.

### `notas.py`

Cuida da logica de arquivos.

Ele salva, lista, le, busca, edita e exclui notas.

### `test_notas.py`

Protege o comportamento do projeto.

Se uma mudanca quebrar algo importante, os testes ajudam a perceber cedo.

### `README.md`

Explica o projeto para quem abre o repositorio no GitHub.

### `GUIA_MODULO_2.md`

Explica o aprendizado por tras do projeto.

Serve como consulta pessoal.

## Boas praticas aprendidas

- Fazer commits pequenos.
- Nao implementar tudo de uma vez.
- Evitar complexidade prematura.
- Testar antes de commitar.
- Usar funcoes reutilizaveis.
- Separar logica de interface.
- Manter mensagens simples para o usuario.
- Evoluir o projeto em fatias pequenas.

## Limitacoes atuais

- Categorias/subpastas ainda sao suporte inicial.
- Listar, buscar, ler, editar e excluir ainda focam nas notas do diretorio principal.
- Ainda nao ha banco de dados.
- Ainda nao ha interface grafica.
- Ainda nao ha API.
- O app e local e simples.

## Proximos caminhos possiveis

- Expandir categorias para todos os fluxos.
- Criar app com interface.
- Usar banco de dados.
- Criar uma API.
- Criar automacoes reais com as notas.

## Resumo final

Este projeto ensinou como transformar dados digitados pelo usuario em arquivos reais no computador.

Tambem mostrou como evoluir um programa aos poucos, testando cada etapa e mantendo o codigo organizado.
