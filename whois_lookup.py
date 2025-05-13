#Tool Make By : Ariyan Rabbi(Dʌʀĸ-Nɘt)
#Don't Use My coded File And copy
#Are Your use copy my file Your Father 100 man
#use this tool and give me star
#Don't Copy my file

import whois
import pyfiglet
import time
import sys
import os
from termcolor import colored

from colorama import Fore, init

init(autoreset=True)

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Typewriter effect
def type_print(text, color="white", delay=0.01):
    for char in text:
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Underlined Info
def show_line(title, data):
    if isinstance(data, list):
        data = ', '.join(str(i) for i in data if isinstance(i, str))
    if isinstance(data, str) and data.strip():
        type_print(f"{title}: ", "cyan", 0.01)
        type_print(f"{data}", "white", 0.005)
        print(colored("━" * 50, "green"))

# Stylish Input Prompt
def prompt_input(prompt_text):
    print(f"{Fore.MAGENTA}┌─🌐 {prompt_text}")
    return input(f"{Fore.MAGENTA}└──╼ {Fore.WHITE}")

# Start
clear()

logo = pyfiglet.figlet_format("WHOIS LOOKUP", font="slant")
print(colored(logo, "cyan"))

print(colored("╔══════════════════════════════════════════════╗", "green"))
print(colored("║  Coded by: Ariyan Rabbi (Dʌʀĸ-Nɘt)           ║", "green"))
print(colored("║  Facebook : facebook.com/share/12Ju91Lznxb/  ║", "green"))
print(colored("║  Telegram : t.me/DARK_NET_40                 ║", "green"))
print(colored("║  GitHub   : github.com/DARK-NET-403          ║", "green"))
print(colored("╚══════════════════════════════════════════════╝", "green"))

# Take domain input with style
domain = prompt_input("Enter a domain (e.g. google.com)")

type_print("\n[~] Performing WHOIS lookup...\n", "blue", 0.02)
time.sleep(1)
clear()

try:
    w = whois.whois(domain)

    logo = pyfiglet.figlet_format("WHOIS INFO", font="slant")
    print(colored(logo, "cyan"))
    print(colored("╔══════════════════════════════════════════════╗", "green"))
    print(colored("║  Coded by: Ariyan Rabbi (Dʌʀĸ-Nɘt)           ║", "green"))
    print(colored("║  Facebook : facebook.com/share/12Ju91Lznxb/  ║", "green"))
    print(colored("║  Telegram : t.me/DARK_NET_40                 ║", "green"))
    print(colored("║  GitHub   : github.com/DARK-NET-403          ║", "green"))
    print(colored("╚══════════════════════════════════════════════╝", "green"))

    print(colored("=== DOMAIN INFORMATION ===\n", "magenta", attrs=["bold"]))

    show_line("Domain Name", str(w.domain_name).upper())
    show_line("Registrar", w.registrar)
    show_line("WHOIS Server", w.whois_server)

    if isinstance(w.creation_date, str):
        show_line("Creation Date", w.creation_date)
    elif hasattr(w.creation_date, 'strftime'):
        show_line("Creation Date", w.creation_date.strftime('%Y-%m-%d'))

    if hasattr(w.expiration_date, 'strftime'):
        show_line("Expiration Date", w.expiration_date.strftime('%Y-%m-%d'))

    if hasattr(w.updated_date, 'strftime'):
        show_line("Last Updated", w.updated_date.strftime('%Y-%m-%d'))

    show_line("Name Servers", w.name_servers)

    if isinstance(w.status, list):
        filtered = [s.split(' ')[0] for s in w.status if isinstance(s, str)]
        show_line("Status", ', '.join(filtered))

except Exception as e:
    print(colored("\n[!] Error fetching WHOIS data: ", "red"), e)
