# OpenCode CLI (Bun + OpenCode AI)

Módulo de instalação automatizada do **Bun Runtime** e **OpenCode CLI**.

## Status

✅ **Implementado** — pronto para uso.

## O que é instalado?

### 1. Bun Runtime
- Runtime JavaScript/TypeScript ultrarrápido
- Gerenciador de pacotes integrado
- Instalado via script oficial: `irm bun.sh/install.ps1 | iex`

### 2. OpenCode CLI
- CLI de IA para desenvolvimento
- Instalado via Bun: `bun add -g opencode-ai`

### 3. Plugin Antigravity (Opcional)
- Plugin de integração com Antigravity IDE
- Adiciona funcionalidades avançadas de IA ao OpenCode
- Instalado via Bun: `bun add -g @antigravity/opencode-plugin`
- **Nota:** Se o pacote não estiver disponível no npm, a instalação continua sem o plugin

## Requisitos

- **Windows 10 ou superior** (64-bit recomendado)
- **PowerShell** (para instalação do Bun)
- **Conexão com internet**

## Uso

### Via Python

```python
from opencode import installer

# Executa a instalação completa (Bun + OpenCode)
installer.install()
```

### Via Linha de Comando

```bash
python -m opencode.installer
```

### Standalone

```bash
python opencode/installer.py
```

## Instalação Manual

Se preferir instalar manualmente:

```powershell
# 1. Instalar Bun
powershell -c "irm bun.sh/install.ps1|iex"

# 2. Reiniciar terminal, depois instalar OpenCode
bun add -g opencode-ai

# 3. Executar
opencode
```

## Após a Instalação

1. **Reinicie o terminal** para atualizar o PATH
2. Execute `bun --version` para verificar o Bun
3. Execute `opencode` para iniciar o CLI
4. Configure sua API key se necessário
5. Se o plugin antigravity foi instalado, use `opencode --help` para ver comandos adicionais

## Links Úteis

- [Bun](https://bun.sh/)
- [OpenCode AI](https://opencode.ai/)
