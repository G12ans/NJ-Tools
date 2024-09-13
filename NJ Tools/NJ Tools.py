import os
import subprocess
from pathlib import Path
import socket
import requests

# Fonction pour afficher le menu
def display_menu(page):
    os.system('cls')  # Efface l'écran avant d'afficher
    menu_ascii = '''
\033[91m
███▄▄▄▄        ▄█          ███      ▄██████▄   ▄██████▄   ▄█          ▄████████ 
███▀▀▀██▄     ███      ▀█████████▄ ███    ███ ███    ███ ███         ███    ███ 
███   ███     ███         ▀███▀▀██ ███    ███ ███    ███ ███         ███    █▀  
███   ███     ███          ███   ▀ ███    ███ ███    ███ ███         ███        
███   ███     ███          ███     ███    ███ ███    ███ ███       ▀███████████ 
███   ███     ███          ███     ███    ███ ███    ███ ███                ███ 
███   ███     ███          ███     ███    ███ ███    ███ ███▌    ▄    ▄█    ███ 
 ▀█   █▀  █▄ ▄███         ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██  ▄████████▀  
          ▀▀▀▀▀▀                                         ▀                      
\033[0m
    '''

    print(menu_ascii)
    options = [
        '\033[94m[01]\033[0m Port Scanner        ', '\033[94m[02]\033[0m WHOIS Lookup        ', '\033[94m[03]\033[0m IP Location         ', '\033[94m[04]\033[0m IP Information      ', '\033[94m[05]\033[0m SQLMap              ',
        '\033[94m[06]\033[0m Soon                ', '\033[94m[07]\033[0m Soon                ', '\033[94m[08]\033[0m Soon                ', '\033[94m[09]\033[0m Soon                ', '\033[94m[10]\033[0m Soon                ',
        '\033[94m[11]\033[0m Soon                ', '\033[94m[12]\033[0m Soon                ', '\033[94m[13]\033[0m Soon                ', '\033[94m[14]\033[0m Soon                ', '\033[94m[15]\033[0m Soon                ',
        '\033[94m[16]\033[0m Soon                ', '\033[94m[17]\033[0m Soon                ', '\033[94m[18]\033[0m Soon                ', '\033[94m[19]\033[0m Soon                ', '\033[94m[20]\033[0m Soon                ',
        '\033[94m[21]\033[0m Soon                ', '\033[94m[22]\033[0m Soon                ', '\033[94m[23]\033[0m Soon                ', '\033[94m[24]\033[0m Soon                ', '\033[94m[25]\033[0m Soon                ',
        '\033[94m[26]\033[0m Soon                ', '\033[94m[27]\033[0m Soon                ', '\033[94m[28]\033[0m Soon                ', '\033[94m[29]\033[0m Soon                ', '\033[94m[30]\033[0m Soon                '
    ]

    start = (page - 1) * 10
    end = start + 10
    for i in range(start, end):
        if i >= len(options):
            break
        print(f"\033[97m{options[i]}\033[0m")

    print("\033[94m[N] - Next \033[0m \033[94m[B] - Back \033[0m \033[94m[Q] - Quit\033[0m")
    print("\033[93mSelect an option or type 'n' for next page, 'b' for previous page, or 'q' to quit:\033[0m")

# Fonction pour scanner les ports (option 1)
def port_scanner():
    os.system('cls')  # Efface l'écran avant d'afficher
    print("\033[94mPlease enter the IP address to scan:\033[0m")
    ip = input("\033[94mIP Address: \033[0m").strip()
    
    if not ip:
        print("\033[91mNo IP address provided. Returning to menu.\033[0m")
        return

    print(f"\033[94mScanning ports for {ip}...\033[0m")
    # Ici, le code pour scanner les ports serait exécuté.

# Fonction WHOIS Lookup (option 2)
def whois_lookup():
    os.system('cls')  # Efface l'écran avant d'afficher
    print("\033[94mPlease enter the domain name or IP address for WHOIS lookup:\033[0m")
    domain = input("\033[94mDomain/IP: \033[0m").strip()
    
    if not domain:
        print("\033[91mNo domain or IP address provided. Returning to menu.\033[0m")
        return

    print(f"\033[94mPerforming WHOIS lookup for {domain}...\033[0m")
    # Ici, le code pour effectuer la recherche WHOIS serait exécuté.

# Fonction pour obtenir la localisation d'une IP (option 3)
def ip_location():
    os.system('cls')  # Efface l'écran avant d'afficher
    print("\033[94mPlease enter the IP address to get its location:\033[0m")
    ip = input("\033[94mIP Address: \033[0m").strip()
    
    if not ip:
        print("\033[91mNo IP address provided. Returning to menu.\033[0m")
        return

    print(f"\033[94mGetting location for IP {ip}...\033[0m")
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        data = response.json()
        location_info = (f"IP: {data.get('ip')}\n"
                         f"City: {data.get('city')}\n"
                         f"Region: {data.get('region')}\n"
                         f"Country: {data.get('country_name')}\n"
                         f"Latitude: {data.get('latitude')}\n"
                         f"Longitude: {data.get('longitude')}")
        print(f"\033[92m{location_info}\033[0m")
    except Exception as e:
        print(f"\033[91mError getting location: {e}\033[0m")

# Fonction pour obtenir les informations d'une IP (option 4)
def ip_info():
    os.system('cls')  # Efface l'écran avant d'afficher
    print("\033[94mPlease enter the IP address to get its information:\033[0m")
    ip = input("\033[94mIP Address: \033[0m").strip()
    
    if not ip:
        print("\033[91mNo IP address provided. Returning to menu.\033[0m")
        return

    print(f"\033[94mGetting information for IP {ip}...\033[0m")
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        data = response.json()
        info = (f"IP: {data.get('ip')}\n"
                f"City: {data.get('city')}\n"
                f"Region: {data.get('region')}\n"
                f"Country: {data.get('country_name')}\n"
                f"Latitude: {data.get('latitude')}\n"
                f"Longitude: {data.get('longitude')}\n"
                f"Org: {data.get('org')}")
        print(f"\033[92m{info}\033[0m")
    except Exception as e:
        print(f"\033[91mError getting IP information: {e}\033[0m")

# Fonction pour lancer SQLMap (option 5)
def sqlmap_test():
    os.system('cls')  # Efface l'écran avant d'afficher
    print("\033[94mPlease enter the target URL for SQLMap testing:\033[0m")
    target = input("\033[94mTarget URL: \033[0m").strip()

    if not target:
        print("\033[91mNo URL provided. Returning to menu.\033[0m")
        return

    print(f"\033[94mLaunching SQLMap against {target}...\033[0m")
    try:
        sqlmap_path = Path.home() / 'sqlmap' / 'sqlmap.py'
        if sqlmap_path.exists():
            subprocess.run(['python', str(sqlmap_path), '-u', target], check=True)
        else:
            print("\033[91mSQLMap not found. Please install SQLMap first.\033[0m")
    except subprocess.CalledProcessError as e:
        print(f"\033[91mError executing SQLMap: {e}\033[0m")

# Fonction d'interaction avec les choix du menu
def handle_choice(choice):
    if choice == '1':
        port_scanner()
    elif choice == '2':
        whois_lookup()
    elif choice == '3':
        ip_location()
    elif choice == '4':
        ip_info()
    elif choice == '5':
        sqlmap_test()
    else:
        print(f"\033[91mOption {choice} is not implemented yet.\033[0m")

# Fonction principale
def main():
    page = 1
    while True:
        display_menu(page)
        choice = input().strip().lower()
        if choice == 'q':
            break
        elif choice == 'n':
            if page < (30 // 10):
                page += 1
        elif choice == 'b':
            if page > 1:
                page -= 1
        elif choice.isdigit() and 1 <= int(choice) <= 30:
            handle_choice(choice)
            input("\033[93mPress Enter to return to the menu...\033[0m")
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")

if __name__ == '__main__':
    main()
