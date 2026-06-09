# Projeto 2 - Organizador de notas local

Este projeto e uma mini CLI em Python para organizar notas locais em Markdown.

As notas sao salvas como arquivos `.md` dentro da pasta `notas/`.

## Funcionalidades atuais

- Criar notas em Markdown
- Escrever conteudo com varias linhas
- Listar notas
- Ler notas por numero
- Buscar notas por termo
- Ler notas encontradas na busca
- Excluir notas com confirmacao
- Editar conteudo da nota
- Editar titulo da nota
- Validar titulo e conteudo
- Evitar sobrescrever notas existentes
- Usar menu continuo ate sair

## Estrutura do projeto

```text
Projeto_de_aprendizado_2/
├── main.py
├── notas.py
├── test_notas.py
├── README.md
├── .gitignore
└── notas/
```

## Pasta de notas

A pasta `notas/` e usada para armazenar as notas localmente.

Ela e criada automaticamente quando necessario e esta ignorada pelo Git. Assim, suas notas pessoais nao entram no repositorio.

## Como rodar o programa

No terminal, execute:

```bash
python main.py
```

## Menu atual

```text
1 - Criar nova nota
2 - Listar notas
3 - Ler nota
4 - Buscar notas
5 - Excluir nota
6 - Editar nota
7 - Sair
```

## Como usar

Para criar uma nota, escolha `1`, digite o titulo e escreva o conteudo. Para finalizar o conteudo, pressione Enter em uma linha vazia.

Para ler uma nota, escolha `3`, selecione o numero da nota e veja o conteudo no terminal.

Para buscar notas, escolha `4`, digite um termo e selecione uma nota encontrada para ler.

Para excluir uma nota, escolha `5`, selecione o numero da nota e confirme a exclusao.

Para editar uma nota, escolha `6`, selecione o numero da nota e escolha se deseja editar o conteudo ou o titulo.

## Como rodar os testes

O projeto usa `pytest` para testes automatizados.

No terminal, execute:

```bash
python -m pytest
```

Os testes ficam no arquivo `test_notas.py`.

## Proximos passos

- Menu de acoes por nota
- Organizar notas em subpastas
- Melhorar nomes de arquivos
- Adicionar tags
- Exportar ou importar notas
