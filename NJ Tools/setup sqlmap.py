import os
import subprocess
import sys
import shutil
from pathlib import Path

# URL du dépôt GitHub de SQLMap
SQLMAP_REPO_URL = 'https://github.com/sqlmapproject/sqlmap.git'
SQLMAP_DIR = Path.home() / 'sqlmap'

# Vérifier si git est installé
def check_git():
    try:
        subprocess.run(['git', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("\033[92mGit is installed.\033[0m")
    except subprocess.CalledProcessError:
        print("\033[91mGit is not installed. Please install Git to proceed.\033[0m")
        sys.exit(1)

# Cloner le dépôt SQLMap
def clone_sqlmap():
    if SQLMAP_DIR.exists():
        print(f"\033[93mSQLMap directory already exists at {SQLMAP_DIR}. Removing...\033[0m")
        shutil.rmtree(SQLMAP_DIR)
    
    print(f"\033[94mCloning SQLMap repository from {SQLMAP_REPO_URL}...\033[0m")
    try:
        subprocess.run(['git', 'clone', SQLMAP_REPO_URL, str(SQLMAP_DIR)], check=True)
        print(f"\033[92mSuccessfully cloned SQLMap to {SQLMAP_DIR}\033[0m")
    except subprocess.CalledProcessError as e:
        print(f"\033[91mFailed to clone SQLMap: {e}\033[0m")
        sys.exit(1)

# Installer les dépendances Python
def install_dependencies():
    print("\033[94mInstalling Python dependencies...\033[0m")
    try:
        subprocess.run(['pip', 'install', '-r', str(SQLMAP_DIR / 'requirements.txt')], check=True)
        print("\033[92mSuccessfully installed Python dependencies.\033[0m")
    except subprocess.CalledProcessError as e:
        print(f"\033[91mFailed to install Python dependencies: {e}\033[0m")
        sys.exit(1)

# Fonction principale
def main():
    check_git()
    clone_sqlmap()
    install_dependencies()
    print("\033[92mSQLMap setup is complete.\033[0m")

if __name__ == '__main__':
    main()
