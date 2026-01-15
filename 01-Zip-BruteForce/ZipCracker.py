#!/usr/bin/env python3
import zipfile
import os

def crack_zip():
    print("--- ZIP CRACKER CONFIGURADO ---")
    zip_file = input("Nome do arquivo ZIP: ")

    # Sugere o caminho padrão da RockYou
    default_wl = "/usr/share/wordlists/rockyou.txt"
    wordlist = input(f"Caminho da wordlist [Padrão: {default_wl}]: ") or default_wl

    if not os.path.exists(zip_file):
        print(f"\n[!] Erro: O arquivo '{zip_file}' não foi encontrado nesta pasta.")
        return

    try:
        with zipfile.ZipFile(zip_file) as zf:
            with open(wordlist, 'rb') as f:
                print(f"[*] Iniciando ataque em {zip_file}...")
                for line in f:
                    password = line.strip()
                    try:
                        zf.extractall(pwd=password)
                        print(f"\n[+] SENHA ENCONTRADA: {password.decode()}")
                        return
                    except:
                        continue
        print("\n[-] Senha não encontrada na lista.")
    except Exception as e:
        print(f"\n[!] Erro: {e}")

if __name__ == "__main__":
    crack_zip()
