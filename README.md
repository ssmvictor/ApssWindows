# Orquestrador de Instalações

Aplicação desktop Windows para instalação automatizada de ferramentas de desenvolvimento.

## Quick Start

### 1. Verifique os pré-requisitos

```powershell
python --version   # Python 3.7+ necessário
```

### 2. Clone o repositório

```powershell
git clone https://github.com/seu-usuario/instalacoes.git
cd instalacoes
```

### 3. Execute

**Opção A — Automático** *(recomendado)*

```powershell
.\install_and_run.bat
```

**Opção B — Manual**

```powershell
pip install -r requirements.txt
python src\main.py
```

> [!TIP]
> O script `install_and_run.bat` cria automaticamente o ambiente virtual e instala as dependências.

## Ferramentas Suportadas

| Ferramenta | Descrição |
|------------|-----------|
| **Node.js** | Runtime + CLI Tools |
| **VS Code** | Editor de código |
| **Git** | Controle de versão |
| **MCP Excel** | Server para Excel |
| **Antigravity** | Gemini CLI *(em desenvolvimento)* |
| **OpenCode** | OpenCode CLI + Plugin Antigravity *(em desenvolvimento)* |

## Documentação

- [Arquitetura](docs/architecture.md) — Estrutura do projeto e componentes
- [Testes](docs/testing.md) — Como executar os testes
- [Build](docs/build.md) — Gerar executáveis

## Requisitos

- Windows 10+
- Python 3.7+
