import os
import time
import zipfile
import itertools
import string
import webbrowser

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
P = '\033[95m'
C = '\033[96m'
W = '\033[97m'
N = '\033[0m'

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(f"""
{R}***********************************
{G}*           H C O TEAM            *
{B}*       Hacker Colony Official    *
{P}*          ZIP CRACKER TOOL       *
{C}*           Coded By ALI          *
{R}***********************************
{N}""")

def banner2():
    clear()
    print(f"""
{Y}***************************************
{G}* MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM     *
{B}* M                             M     *
{P}* M HCO ZIP CRACKER TOOL        M     *
{C}* M                             M     *
{R}* MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM     *
{G}* {B}CODED BY ALI{G}                        *
{N}***************************************
{N}""")

    print(f"{Y}Choose a method:{N}")
    print(f"{G}1.{N} Crack ZIP without wordlist")
    print(f"{B}2.{N} Crack ZIP with wordlist")
    choice = input(f"{C}Enter your choice (1/2): {N}")
    return choice

def crack_zip(zip_file, max_length):
    start_time = time.time()
    chars = string.ascii_letters + string.digits + string.punctuation
    found = False
    password = None
    for length in range(1, max_length + 1):
        print(f"{Y}Trying passwords of length {length}...{N}")
        for attempt in itertools.product(chars, repeat=length):
            password = ''.join(attempt)
            print(f"{G}Trying password: {password}{N}", end='\r')
            try:
                with zipfile.ZipFile(zip_file) as zip_file_ref:
                    zip_file_ref.extractall(pwd=password.encode('utf-8'))
                found = True
                end_time = time.time()
                print(f"{P}\nPassword found: {password}{N}")
                print(f"{C}Time taken: {end_time - start_time} seconds{N}")
                return
            except Exception as e:
                pass
    if not found:
        print(f"{R}\nPassword not found{N}")

def crack_zip_wordlist(zip_file, wordlist):
    print(f"{Y}\nCracking ZIP file: {zip_file}\n{N}")
    print(f"{G}Using wordlist: {wordlist}\n{N}")
    start_time = time.time()
    with open(wordlist, 'r') as f:
        for line in f:
            password = line.strip()
            print(f"{B}Trying password: {password}{N}", end='\r')
            try:
                with zipfile.ZipFile(zip_file) as zip_file_ref:
                    zip_file_ref.extractall(pwd=password.encode())
                end_time = time.time()
                print(f"{P}\nPassword found: {password}{N}")
                print(f"{C}Time taken: {end_time - start_time} seconds{N}")
                return
            except Exception as e:
                pass
    print(f"{R}\nPassword not found{N}")

def main():
    banner()
    print(f"{Y}THIS TOOL IS PAID AND IF YOU WANT TO USE IT FOR FREE THEN YOU HAVE TO SUBSCRIBE OUR CHANNEL:{N}")
    os.system("termux-open https://youtube.com/@hackers_colony_tech?si=wCnZaEpBli_UTxHj")
    time.sleep(5)
    clear()
    choice = banner2()
    zip_file = input(f"{Y}Enter ZIP file path: {N}")
    if choice == '1':
        max_length = int(input(f"{G}Enter maximum password length: {N}"))
        crack_zip(zip_file, max_length)
    elif choice == '2':
        wordlist = input(f"{B}Enter wordlist file path: {N}")
        crack_zip_wordlist(zip_file, wordlist)
    else:
        print(f"{R}Invalid choice{N}")

if __name__ == "__main__":
    main()
