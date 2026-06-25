# Lista Básica de Cadastro

Sistema simples em Python para cadastro e listagem de pessoas, com armazenamento em arquivo de texto.

## 📁 Estrutura do projeto

```
lista-basica-cadastro/
├── .vscode/
│   └── launch.json        # Configuração de debug do VS Code
├── lista_pessoas/
│   ├── lib/
│   │   └── arquivo.py      # Funções auxiliares (manipulação de arquivo, menu, etc.)
│   └── sistema.py          # Arquivo principal do sistema
├── .gitignore
└── README.md
```

## ▶️ Como rodar o projeto

Este projeto usa imports baseados em pacote (`lista_pessoas.lib.arquivo`), então **não pode ser executado como um script solto**. Ele precisa ser rodado como módulo, a partir da pasta raiz do projeto.

### Opção 1 — Terminal
A partir da raiz do projeto (`lista-basica-cadastro`):
```bash
python -m lista_pessoas.sistema
```

### Opção 2 — VS Code (Run and Debug)
- Aperte **F5** (com debug) ou **Ctrl+F5** (sem debug).
- A configuração já está pronta no `.vscode/launch.json`.

### Opção 3 — PyCharm
Funciona normalmente ao executar `sistema.py`, pois o PyCharm marca a raiz do projeto como *Sources Root* automaticamente.

## ⚠️ Atenção

**Não use o botão "Run Python File" (▶) no canto superior direito do VS Code.**

Esse botão executa o arquivo diretamente pelo caminho (`python sistema.py`), ignorando a configuração do `launch.json`. Como o projeto depende de imports de pacote, isso resulta no erro:

```
ModuleNotFoundError: No module named 'lista_pessoas'
```

Use sempre uma das opções listadas acima (**F5**, **Ctrl+F5** ou `python -m lista_pessoas.sistema` no terminal).

## 🧩 Funcionalidades

- Ver pessoas cadastradas
- Cadastrar nova pessoa (nome e idade)
- Sair do sistema

## 🛠️ Requisitos

- Python 3.x instalado
