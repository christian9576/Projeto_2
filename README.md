# Projeto 2 - Organizador de notas local

Este projeto e uma mini CLI em Python para organizar notas locais em Markdown.

As notas sao salvas como arquivos `.md` dentro da pasta `notas/`.

## Funcionalidades atuais

- Criar notas em Markdown
- Escrever conteudo com varias linhas
- Criar nota com categoria opcional
- Listar notas
- Buscar notas por termo
- Ler notas
- Editar titulo e conteudo
- Excluir notas com confirmacao
- Evitar sobrescrever notas existentes
- Validar titulo e conteudo
- Usar menu principal simplificado

## Categorias

O projeto tem suporte inicial a categorias/subpastas ao criar notas.

Se o usuario informar uma categoria, a nota e salva em uma subpasta dentro de `notas/`.

Exemplo:

```text
Categoria: Python Basico
Pasta criada: notas/python-basico/
```

Por enquanto, os fluxos de listar, buscar, ler, editar e excluir ainda focam nas notas salvas diretamente no diretorio principal `notas/`.

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

## Menu principal

```text
1 - Criar nova nota
2 - Listar notas
3 - Buscar notas
4 - Sair
```

As acoes de ler, editar e excluir ficam dentro dos fluxos de listar e buscar.

## Como rodar os testes

O projeto usa `pytest` para testes automatizados.

No terminal, execute:

```bash
python -m pytest
```

Os testes ficam no arquivo `test_notas.py`.

## O que aprendi neste projeto

- Persistencia com arquivos
- Criacao de pastas pelo Python
- Leitura e escrita de arquivos
- Validacoes
- Testes com pytest
- Refatoracao
- Uso de Git/GitHub
- Uso de Codex por fatias pequenas

## Possiveis proximos passos

- Expandir suporte a categorias
- Adicionar tags
- Melhorar nomes de arquivos
- Exportar/importar notas
- Transformar em app com interface
