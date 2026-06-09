# Projeto 2 - Organizador de notas local

Este projeto e uma mini CLI em Python para organizar notas locais em Markdown.

As notas sao salvas como arquivos `.md` dentro da pasta `notas/`.

## Funcionalidades atuais

- Criar nota em Markdown
- Escrever conteudo com varias linhas
- Listar notas salvas
- Ler nota escolhendo pelo numero
- Ler varias notas em sequencia
- Validar titulo e conteudo
- Evitar sobrescrever notas existentes
- Sair pelo menu

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

## Como rodar os testes

O projeto usa `pytest` para testes automatizados.

No terminal, execute:

```bash
python -m pytest
```

Os testes ficam no arquivo `test_notas.py`.

## Proximos passos

- Buscar notas por termo
- Editar nota
- Excluir nota
- Melhorar nomes de arquivos
- Adicionar tags
