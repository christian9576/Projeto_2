# Projeto 2 - Organizador de notas local

Este projeto e uma mini CLI em Python para criar, listar e ler notas locais.

As notas sao salvas como arquivos `.md` dentro da pasta `notas/`.

## Funcionalidades atuais

- Criar nota
- Listar notas salvas
- Ler o conteudo de uma nota
- Evitar sobrescrever uma nota existente com o mesmo nome
- Manter o menu aberto ate o usuario escolher sair

## Estrutura do projeto

```text
Projeto_de_aprendizado_2/
├── main.py
├── notas.py
├── test_notas.py
├── README.md
├── .gitignore
└── notas/
    └── arquivos .md das notas locais
```

## Como rodar o programa

No terminal, execute:

```bash
python main.py
```

## Como usar o menu

Ao iniciar o programa, o menu mostra as opcoes:

```text
1 - Criar nova nota
2 - Listar notas
3 - Ler nota
4 - Sair
```

Use `1` para criar uma nova nota.

Use `2` para listar os arquivos `.md` salvos.

Use `3` para ler uma nota. Nesse caso, informe o nome do arquivo, por exemplo:

```text
git-basico.md
```

Use `4` para sair do programa.

## Pasta de notas

A pasta `notas/` e usada para armazenar as notas localmente no seu computador.

Ela esta ignorada pelo Git, entao as suas notas pessoais nao entram no repositorio.

## Como rodar os testes

O projeto usa `pytest` para testes automatizados.

No terminal, execute:

```bash
python -m pytest
```

Os testes ficam no arquivo `test_notas.py`.

## Proximos passos

- Escolher nota por numero
- Validar titulo vazio
- Permitir conteudo com varias linhas
- Editar nota
- Excluir nota
- Buscar notas
