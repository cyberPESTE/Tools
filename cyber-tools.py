# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import os, time

if os.getuid() != 0:
	print("\033[1;31m\nError:\033[0;m Este script requer uso de root (sudo)")
	sys.exit()

os.system("clear")

def banner():
	print("""
                
\033[;1m

⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄
⠄⠄⠄⠄⣴⣿⣿⡿⣿⢿⣟⣿⣻⣟⡿⣟⣿⣟⡿⣟⣿⣻⣟⣿⣻⢿⣻⡿⣿⢿⣷⣆⠄⠄⠄
⠄⠄⠄⢘⣿⢯⣷⡿⡿⡿⢿⢿⣷⣯⡿⣽⣞⣷⣻⢯⣷⣻⣾⡿⡿⢿⢿⢿⢯⣟⣞⡮⡀⠄⠄
⠄⠄⠄⢸⢞⠟⠃⣉⢉⠉⠉⠓⠫⢿⣿⣷⢷⣻⣞⣿⣾⡟⠽⠚⠊⠉⠉⠉⠙⠻⣞⢵⠂⠄⠄
⠄⠄⠄⢜⢯⣺⢿⣻⣿⣿⣷⣔⡄⠄⠈⠛⣿⣿⡾⠋⠁⠄⠄⣄⣶⣾⣿⡿⣿⡳⡌⡗⡅⠄⠄
⠄⠄⠄⢽⢱⢳⢹⡪⡞⠮⠯⢯⡻⡬⡐⢨⢿⣿⣿⢀⠐⡥⣻⡻⠯⡳⢳⢹⢜⢜⢜⢎⠆⠄⠄
⠄⠄⠠⣻⢌⠘⠌⡂⠈⠁⠉⠁⠘⠑⢧⣕⣿⣿⣿⢤⡪⠚⠂⠈⠁⠁⠁⠂⡑⠡⡈⢮⠅⠄⠄
⠄⠄⠠⣳⣿⣿⣽⣭⣶⣶⣶⣶⣶⣺⣟⣾⣻⣿⣯⢯⢿⣳⣶⣶⣶⣖⣶⣮⣭⣷⣽⣗⠍⠄⠄
⠄⠄⢀⢻⡿⡿⣟⣿⣻⣽⣟⣿⢯⣟⣞⡷⣿⣿⣯⢿⢽⢯⣿⣻⣟⣿⣻⣟⣿⣻⢿⣿⢀⠄⠄
⠄⠄⠄⡑⡏⠯⡯⡳⡯⣗⢯⢟⡽⣗⣯⣟⣿⣿⣾⣫⢿⣽⠾⡽⣺⢳⡫⡞⡗⡝⢕⠕⠄⠄⠄
⠄⠄⠄⢂⡎⠅⡃⢇⠇⠇⣃⣧⡺⡻⡳⡫⣿⡿⣟⠞⠽⠯⢧⣅⣃⠣⠱⡑⡑⠨⢐⢌⠂⠄⠄
⠄⠄⠄⠐⠼⣦⢀⠄⣶⣿⢿⣿⣧⣄⡌⠂⠢⠩⠂⠑⣁⣅⣾⢿⣟⣷⠦⠄⠄⡤⡇⡪⠄⠄⠄
⠄⠄⠄⠄⠨⢻⣧⡅⡈⠛⠿⠿⠿⠛⠁⠄⢀⡀⠄⠄⠘⠻⠿⠿⠯⠓⠁⢠⣱⡿⢑⠄⠄⠄⠄
⠄⠄⠄⠄⠈⢌⢿⣷⡐⠤⣀⣀⣂⣀⢀⢀⡓⠝⡂⡀⢀⢀⢀⣀⣀⠤⢊⣼⡟⡡⡁⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠈⢢⠚⣿⣄⠈⠉⠛⠛⠟⠿⠿⠟⠿⠻⠻⠛⠛⠉⠄⣠⠾⢑⠰⠈⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠑⢌⠿⣦⡡⣱⣸⣸⣆⠄⠄⠄⣰⣕⢔⢔⠡⣼⠞⡡⠁⠁⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢝⢷⣕⡷⣿⡿⠄⠄⠠⣿⣯⣯⡳⡽@cyberPESTE
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢮⣿⣽⣯⠄⠄⢨⣿⣿⡷⡫⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠙⠝⠂⠄⢘⠋⠃⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄


 """)
banner()


def menu():
	print("""
\033[1;37m(1)\033[0;m \033[0;32mNmap\033[0;m               \033[1;37m(11)\033[0;m \033[0;32mWireshark\033[0;m     \033[1;37m(21)\033[0;m \033[0;32mAutopsy\033[0;m        \033[1;37m(31)\033[0;m \033[0;32mAnonsurf\033[0;m
\033[1;37m(2)\033[0;m \033[0;32mNikto\033[0;m              \033[1;37m(12)\033[0;m \033[0;32mCrunch\033[0;m        \033[1;37m(22)\033[0;m \033[0;32mPipal\033[0;m          \033[1;37m(32)\033[0;m \033[0;32mBettercap\033[0;m
\033[1;37m(3)\033[0;m \033[0;32mJohn the Ripper\033[0;m    \033[1;37m(13)\033[0;m \033[0;32mCewl\033[0;m          \033[1;37m(23)\033[0;m \033[0;32mMasscan\033[0;m        \033[1;37m(33)\033[0;m \033[0;32mKismet\033[0;m
\033[1;37m(4)\033[0;m \033[0;32mWifite\033[0;m             \033[1;37m(14)\033[0;m \033[0;32mMedusa\033[0;m        \033[1;37m(24)\033[0;m \033[0;32mWhatWeb\033[0;m        \033[1;37m(34)\033[0;m \033[0;32mSkipFish\033[0;m
\033[1;37m(5)\033[0;m \033[0;32mMetasploit\033[0;m         \033[1;37m(15)\033[0;m \033[0;32mReaver\033[0;m        \033[1;37m(25)\033[0;m \033[0;32mMaltego\033[0;m        \033[1;37m(35)\033[0;m \033[0;32mNetsniff-ng\033[0;m
\033[1;37m(6)\033[0;m \033[0;32mSQLmap\033[0;m             \033[1;37m(16)\033[0;m \033[0;32mNcrack\033[0;m        \033[1;37m(26)\033[0;m \033[0;32mArmitage\033[0;m       \033[1;37m(36)\033[0;m \033[0;32mMITMproxy\033[0;m
\033[1;37m(7)\033[0;m \033[0;32mAircrack-ng\033[0;m        \033[1;37m(17)\033[0;m \033[0;32mHydra\033[0;m         \033[1;37m(27)\033[0;m \033[0;32mArping\033[0;m         \033[1;37m(37)\033[0;m \033[0;32mHashDeep\033[0;m
\033[1;37m(8)\033[0;m \033[0;32mHashCat\033[0;m            \033[1;37m(18)\033[0;m \033[0;32mEttercap\033[0;m      \033[1;37m(28)\033[0;m \033[0;32mProxyChains\033[0;m    \033[1;37m(38)\033[0;m \033[0;32mPixieWPS\033[0;m
\033[1;37m(9)\033[0;m \033[0;32mLegion\033[0;m             \033[1;37m(19)\033[0;m \033[0;32mMACchanger\033[0;m    \033[1;37m(29)\033[0;m \033[0;32mTor-Browser\033[0;m    \033[1;37m(39)\033[0;m \033[0;32mOphcrack\033[0;m
\033[1;37m(10)\033[0;m \033[0;32mWPScan\033[0;m            \033[1;37m(20)\033[0;m \033[0;32mDNSchef\033[0;m       \033[1;37m(30)\033[0;m \033[0;32mTorGhost\033[0;m       \033[1;37m(40)\033[0;m \033[0;32mSearchSploit\033[0;m
\033[1;37m(0)\033[0;m \033[0;31mSalir\033[0;m\033[0;37m/\033[0;m\033[0;31mExit\033[0;m                                                                                                                                                              
""")
menu()

def restart():
    if input("\033[1;37m¿DESEJA VOLTAR PARA O MENU PRICIPAL? \033[0;32my\033[1;37m/\033[0;31mn\033[0;m\n\033[1;36m>\033[0;m ").upper() != "Y":
        time.sleep(1)
        print("\n\033[1;32mOBRIGADO POR USAR ESTE SCRIPT, volte novavamente\033[0;m\033[1;37m!\033[0;m")
        tool = exit(0)
    tool = os.system("python3 kali-tools.py")    

X = int(input("\033[1;44;37m escolha uma ferramenta :\033[0;m \033[1;36m\n\n>\033[0;m "))

if X == 1:
    tool = os.system("apt-get install nmap")
    restart()    
elif X == 2:
    tool = os.system("apt-get install nikto -y")
    restart()
elif X == 3:
    tool = os.system("apt-get install john")
    restart()
elif X == 4:
    tool = os.system("apt-get install wifite")
    restart()
elif X == 5:
    tool = os.system("apt-get install metasploit-framework")
    restart()
elif X == 6:
    tool = os.system("apt-get install sqlmap")
    restart()
elif X == 7:
    tool = os.system("apt-get install aircrack-ng")
    restart()
elif X == 8:
    tool = os.system("apt-get install hashcat")
    restart()
elif X == 9:
    tool = os.system("apt-get install legion -y")
    restart()
elif X == 10:
    tool = os.system("apt-get install wpscan")
    restart()
elif X == 11:
    tool = os.system("apt-get install wireshark")
    restart()
elif X == 12:
    tool = os.system("apt-get install crunch -y")
    restart()
elif X == 13:
    tool = os.system("apt-get install cewl")
    restart()
elif X == 14:
    tool = os.system("apt-get install medusa")
    restart()
elif X == 15:
    tool = os.system("apt-get install reaver")
    restart()
elif X == 16:
    tool = os.system("apt-get install ncrack")
    restart()
elif X == 17:
    tool = os.system("apt-get install hydra-gtk")
    restart()
elif X == 18:
    tool = os.system("apt-get install ettercap")
    tool = os.system("apt-get install ettercap-graphical")
    restart()
elif X == 19:
    tool = os.system("apt-get install macchanger -y")
    restart()
elif X == 20:
    tool = os.system("apt-get install dnschef")
    restart()
elif X == 21:
    tool = os.system("apt-get install autopsy")
    restart()
elif X == 22:
    tool = os.system("apt-get install pipal")
    restart()
elif X == 23:
    tool = os.system("apt-get --assume-yes install git make gcc")
    tool = os.system("git clone https://github.com/robertdavidgraham/masscan")
    tool = os.system("cd masscan")
    tool = os.system("make install")
    restart()
elif X == 24:
    tool = os.system("apt-get install whatweb -y")
    restart()
elif X == 25:
    tool = os.system("apt-get install maltego-teeth")
    restart()
elif X == 26:
    tool = os.system("apt-get install armitage")
    restart()
elif X == 27:
    tool = os.system("apt-get install arping")
    restart()
elif X == 28:
    tool = os.system("apt-get install proxychains -y")
    restart()
elif X == 29:
    tool = os.system("apt-get install tor torbrowser-launcher")
    restart()
elif X == 30:
    tool = os.system("git clone https://github.com/SusmithKrishnan/torghost")
    restart()
elif X == 31:
    tool = os.system("git clone https://github.com/Und3rf10w/kali-anonsurf")
    restart()
elif X == 32:
    tool = os.system("sudo apt-get install build-essential ruby-dev libpcap-dev")
    tool = os.system("apt-get update")
    tool = os.system("apt-get install bettercap")
    restart()
elif X == 33:
    tool = os.system("sudo apt-get install -y kismet")
    restart()
elif X == 34:
    tool = os.system("sudo apt-get install -y skipfish")
    restart()
elif X == 35:
    tool = os.system("sudo apt-get install -y netsniff-ng")
    restart()
elif X == 36:
    tool = os.system("sudo apt-get install -y mitmproxy")
    restart()
elif X == 37:
    tool = os.system("sudo apt install hashdeep")
    restart()
elif X == 38:
    tool = os.system("sudo apt-get install pixiewps")
    restart()
elif X == 39:
    tool = os.system("sudo apt-get install ophcrack")
    restart()
elif X == 40:
    tool = os.system("sudo apt update && sudo apt -y install exploitdb")
    restart()                                             
elif X == 0:
    tool = os.system("exit")
    time.sleep(1)
    print("\n\033[1;32mOBRIGADO POR USAR ESTE SCRIPT\033[0;m\033[1;37m!\033[0;m")
else:
    print("\033[1;31m\nError:\033[0;m Opción inválida, intente nuevamente") 
