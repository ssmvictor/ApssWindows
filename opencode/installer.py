#!/usr/bin/env python3
"""
OpenCode CLI Installer - Instalador Automático
Script Python que automatiza a instalação do Bun e OpenCode CLI no Windows 10/11.
"""

import os
import sys
import subprocess
import ctypes
import platform
from pathlib import Path


def print_banner():
    """Exibe banner de boas-vindas."""
    print("=" * 60)
    print("    🚀 OpenCode CLI Installer - Instalador Automático")
    print("    Bun Runtime + OpenCode AI CLI")
    print("=" * 60)
    print()


def is_admin() -> bool:
    """Verifica se o script está sendo executado com privilégios de administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def verify_windows() -> bool:
    """Verifica se está rodando no Windows."""
    if sys.platform != "win32":
        print("❌ Erro: Este script só funciona no Windows.")
        return False
    return True


def is_bun_installed() -> bool:
    """Verifica se o Bun já está instalado."""
    try:
        result = subprocess.run(
            ["bun", "--version"],
            capture_output=True,
            text=True,
            timeout=10,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ Bun já instalado: v{version}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return False


def is_opencode_installed() -> bool:
    """Verifica se o OpenCode CLI já está instalado."""
    try:
        result = subprocess.run(
            ["opencode", "--version"],
            capture_output=True,
            text=True,
            timeout=10,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ OpenCode CLI já instalado: {version}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return False


def install_bun() -> bool:
    """
    Instala o Bun usando o script oficial do PowerShell.
    
    Returns:
        bool: True se instalação bem-sucedida
    """
    print("📥 Instalando Bun Runtime...")
    print("   Comando: irm bun.sh/install.ps1 | iex")
    print()

    try:
        # Executar o script de instalação do Bun via PowerShell
        cmd = [
            "powershell",
            "-ExecutionPolicy", "Bypass",
            "-Command",
            "irm bun.sh/install.ps1 | iex"
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=300  # 5 minutos
        )

        if result.returncode == 0:
            print("✅ Bun instalado com sucesso!")
            if result.stdout:
                # Mostrar apenas as últimas linhas relevantes
                lines = result.stdout.strip().split('\n')
                for line in lines[-5:]:
                    if line.strip():
                        print(f"   {line.strip()}")
            return True
        else:
            print(f"❌ Erro na instalação do Bun (código: {result.returncode})")
            if result.stderr:
                print(f"   Detalhes: {result.stderr[:500]}")
            return False

    except subprocess.TimeoutExpired:
        print("❌ Timeout na instalação do Bun (5 minutos)")
        return False
    except Exception as e:
        print(f"❌ Erro ao instalar Bun: {e}")
        return False


def refresh_path() -> None:
    """
    Atualiza o PATH do processo atual para incluir o Bun.
    """
    # Caminho padrão do Bun no Windows
    user_home = Path.home()
    bun_path = user_home / ".bun" / "bin"
    
    if bun_path.exists():
        current_path = os.environ.get("PATH", "")
        if str(bun_path) not in current_path:
            os.environ["PATH"] = f"{bun_path};{current_path}"
            print(f"   PATH atualizado: {bun_path}")


def install_opencode() -> bool:
    """
    Instala o OpenCode CLI usando o Bun.
    
    Returns:
        bool: True se instalação bem-sucedida
    """
    print("\n📥 Instalando OpenCode CLI...")
    print("   Comando: bun add -g opencode-ai")
    print()

    try:
        # Atualizar PATH para encontrar o Bun recém-instalado
        refresh_path()
        
        # Encontrar o executável do Bun
        user_home = Path.home()
        bun_exe = user_home / ".bun" / "bin" / "bun.exe"
        
        if not bun_exe.exists():
            # Tentar usar o bun do PATH
            bun_cmd = "bun"
        else:
            bun_cmd = str(bun_exe)

        cmd = [bun_cmd, "add", "-g", "opencode-ai"]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=180  # 3 minutos
        )

        if result.returncode == 0:
            print("✅ OpenCode CLI instalado com sucesso!")
            if result.stdout:
                lines = result.stdout.strip().split('\n')
                for line in lines[-3:]:
                    if line.strip():
                        print(f"   {line.strip()}")
            return True
        else:
            print(f"❌ Erro na instalação do OpenCode CLI (código: {result.returncode})")
            if result.stderr:
                print(f"   Detalhes: {result.stderr[:500]}")
            return False

    except FileNotFoundError:
        print("❌ Bun não encontrado. Certifique-se de que foi instalado corretamente.")
        return False
    except subprocess.TimeoutExpired:
        print("❌ Timeout na instalação do OpenCode CLI (3 minutos)")
        return False
    except Exception as e:
        print(f"❌ Erro ao instalar OpenCode CLI: {e}")
        return False


def install_antigravity_plugin() -> bool:
    """
    Instala o plugin antigravity para o OpenCode CLI.
    O plugin adiciona funcionalidades avançadas de IA ao OpenCode.
    
    Returns:
        bool: True se instalação bem-sucedida
    """
    print("\n📦 Instalando plugin antigravity para OpenCode...")
    print("   Comando: bun add -g @antigravity/opencode-plugin")
    print()

    try:
        # Atualizar PATH para encontrar o Bun
        refresh_path()
        
        # Encontrar o executável do Bun
        user_home = Path.home()
        bun_exe = user_home / ".bun" / "bin" / "bun.exe"
        
        if not bun_exe.exists():
            # Tentar usar o bun do PATH
            bun_cmd = "bun"
        else:
            bun_cmd = str(bun_exe)

        # Tentar instalar o plugin antigravity
        cmd = [bun_cmd, "add", "-g", "@antigravity/opencode-plugin"]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=120  # 2 minutos
        )

        if result.returncode == 0:
            print("✅ Plugin antigravity instalado com sucesso!")
            if result.stdout:
                lines = result.stdout.strip().split('\n')
                for line in lines[-3:]:
                    if line.strip():
                        print(f"   {line.strip()}")
            return True
        else:
            # Se falhar, pode ser que o pacote não exista ainda
            print(f"⚠️  Plugin antigravity não disponível no registro npm")
            print(f"   O OpenCode funcionará sem o plugin antigravity")
            print(f"   Código de retorno: {result.returncode}")
            if result.stderr:
                stderr_preview = result.stderr[:200]
                print(f"   Detalhes: {stderr_preview}")
            return False  # Retorna False mas não impede o fluxo

    except FileNotFoundError:
        print("⚠️  Bun não encontrado. Plugin antigravity não será instalado.")
        return False
    except subprocess.TimeoutExpired:
        print("⚠️  Timeout na instalação do plugin antigravity (2 minutos)")
        return False
    except Exception as e:
        print(f"⚠️  Aviso ao instalar plugin antigravity: {e}")
        return False



def install() -> int:
    """
    Função principal de instalação - API pública do módulo.
    
    Returns:
        int: 0 se sucesso, 1 se falha
    """
    return main()


def main() -> int:
    """Função principal que orquestra o processo de instalação."""
    # Import resiliente de configure_stdout_stderr (opcional)
    try:
        from nodeecli.modules.common import configure_stdout_stderr
    except ModuleNotFoundError:
        try:
            project_root = Path(__file__).resolve().parent.parent
            if (project_root / 'nodeecli').is_dir() and str(project_root) not in sys.path:
                sys.path.insert(0, str(project_root))
            from nodeecli.modules.common import configure_stdout_stderr
        except ModuleNotFoundError:
            def configure_stdout_stderr() -> None:
                return None

    try:
        configure_stdout_stderr()
    except Exception:
        pass
    
    print_banner()

    # Verificar se está no Windows
    if not verify_windows():
        return 1
    
    # Verificar arquitetura
    arch = platform.machine().lower()
    if arch not in ("amd64", "x86_64"):
        print("⚠️  Aviso: Bun funciona melhor em sistemas 64-bit.")
        print()

    success = True

    try:
        # Passo 1: Instalar Bun (se não estiver instalado)
        if not is_bun_installed():
            if not install_bun():
                print("\n❌ Falha na instalação do Bun.")
                return 1
            # Aguardar um momento para o PATH ser atualizado
            refresh_path()
        
        print()
        
        # Passo 2: Instalar OpenCode CLI (se não estiver instalado)
        if not is_opencode_installed():
            if not install_opencode():
                print("\n❌ Falha na instalação do OpenCode CLI.")
                success = False
        
        print()
        
        # Passo 3: Instalar plugin antigravity (opcional mas recomendado)
        if success:
            print("📌 Instalando integrações e plugins...")
            plugin_success = install_antigravity_plugin()
            # Não falhar a instalação se o plugin não estiver disponível
            if not plugin_success:
                print("   ℹ️  OpenCode instalado sem plugin antigravity")
            print()

        if success:
            print("\n🎉 Instalação concluída com sucesso!")
            print("\n📋 Próximos passos:")
            print("   1. Reinicie o terminal para atualizar o PATH")
            print("   2. Execute 'opencode' para iniciar o CLI")
            print("   3. Configure sua API key se necessário")
            if plugin_success:
                print("   4. Use 'opencode --help' para ver comandos do plugin antigravity")
            return 0
        else:
            print("\n⚠️  Instalação parcialmente concluída.")
            return 1

    except KeyboardInterrupt:
        print("\n\n⚠️  Instalação cancelada pelo usuário.")
        return 1
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
