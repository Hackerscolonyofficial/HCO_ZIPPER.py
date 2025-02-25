import os
import time
import zipfile
import itertools
import string
import webbrowser

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()
print("""
*************************************
* H C O   TEAM                      *
* Hacker Colony Official            *
* ZIP CRACKER TOOL                  *
* Coded By ALI                      *
*************************************
THIS TOOL IS PAID AND IF YOU WANT TO USE IT FOR FREE THEN YOU NEED TO SUBSCRIBE OUR YOUTUBE CHANNELS""")
time.sleep(5)  # 5 second ka delay

os.system("termux-open https://youtube.com/@hackers_colony_tech?si=wCnZaEpBli_UTxHj")  # apna pehla YouTube channel link dalen
time.sleep(5)  # 5 second ka delay

os.system("termux-open https://youtube.com/@hackers_colony_linux?si=KKyF-IcPy6euHsYe")  # apna dusra YouTube channel link dalen
time.sleep(5)  # 5 second ka delay

os.system("termux-open https://youtube.com/@hackers_colony_termux?si=JNuROi6AStGjZtkE")  # apna teesra YouTube channel link dalen
time.sleep(5)  # 5 second ka delay

def banner():
    print("""************************************* 
* MMMMMMMMMMMMMMMMMMMMMMMMM         *
* M                       M         *
* M HCO ZIP CRACKER TOOL  M         *
* M                       M         *
* MMMMMMMMMMMMMMMMMMMMMMMMM         *
* CODED BY ALI                      *
************************************* """)

def crack_zip(zip_file, max_length):
    start_time = time.time()
    chars = string.ascii_letters + string.digits + string.punctuation
    found = False
    password = None
    for length in range(1, max_length + 1):
        print(f"Trying passwords of length {length}...")
        for attempt in itertools.product(chars, repeat=length):
            password = ''.join(attempt)
            print(f"Trying password: {password}", end='\r')
            try:
                with zipfile.ZipFile(zip_file) as zip_file_ref:
                    zip_file_ref.extractall(pwd=password.encode('utf-8'))
                found = True
                end_time = time.time()
                print(f"\nPassword found: {password}")
                print(f"Time taken: {end_time - start_time} seconds")
                return
            except Exception as e:
                pass
    if not found:
        print("\nPassword not found")

def crack_zip_wordlist(zip_file, wordlist):
    print(f"\nCracking ZIP file: {zip_file}\n")
    print(f"Using wordlist: {wordlist}\n")
    start_time = time.time()
    with open(wordlist, 'r') as f:
        for line in f:
            password = line.strip()
            print(f"Trying password: {password}", end='\r')
            try:
                with zipfile.ZipFile(zip_file) as zip_file_ref:
                    zip_file_ref.extractall(pwd=password.encode())
                end_time = time.time()
                print(f"\nPassword found: {password}")
                print(f"Time taken: {end_time - start_time} seconds")
                return
            except Exception as e:
                pass
    print("\nPassword not found")

def main():
    banner()
    print("Choose a method:")
    print("1. Crack ZIP without wordlist")
    print("2. Crack ZIP with wordlist")
    choice = input("Enter your choice (1/2): ")
    zip_file = input("Enter ZIP file path: ")
    if choice == '1':
        max_length = int(input("Enter maximum password length: "))
        crack_zip(zip_file, max_length)
    elif choice == '2':
        wordlist = input("Enter wordlist file path: ")
        crack_zip_wordlist(zip_file, wordlist)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
