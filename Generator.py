import os
import time

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
print("_____________________"+Colours.Cyan+"Menu"+Colours.green+"_____________________")
print("|                     |                      |")
print("|"+"["+Colours.Cyan+"1"+Colours.green+"]"+Colours.Cyan+"_________"+Colours.red+"ViRuSeS  |"+Colours.green+" For Windows          |")
print("|_____________________|______________________|")
print("|                     |                      |")
print("|"+"["+Colours.Cyan+"2"+Colours.green+"]"+Colours.Cyan+"_________"+Colours.red+"PaYlOaDs |"+Colours.green+" For Android & Windows|")
print("|_____________________|______________________|")
print("")
print("")
time.sleep(0.2)
chooser = int(input(Colours.green+"Enter" +Colours.red+ " a " +Colours.yellow+ "number "+Colours.Cyan+"====> "+Colours.green))
if chooser ==1:
    time.sleep(2)
    try:
        fake5 = "."
        while fake5 <= ".....":
            fake5 = fake5 + "."
            print(
                "\r" + Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "Please Wait" + str(fake5), end="")
            time.sleep(0.5)
        print("")
        os.system("python3 Venom.py")
    except KeyboardInterrupt:
        print("Hey Dude, see you next time")
if chooser ==2:
    print(Colours.red + "[" + Colours.green + "1" + Colours.red + "]" + Colours.yellow +"       Android")
    print(Colours.red + "[" + Colours.green + "2" + Colours.red + "]" + Colours.yellow +"       Windows_pc")
    print("")
    selector = int(input(Colours.green+"Enter" +Colours.red+ " a " +Colours.yellow+ "number "+Colours.Cyan+"====> "+Colours.green))
    if selector == 1:
        time.sleep(2)
        try:
           fake = "."
           while fake <= ".....":
               fake = fake + "."
               print("\r"+Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "Please Wait"+str(fake), end="")
               time.sleep(0.5)
           print("")
           os.system("python3 Android.py")
        except KeyboardInterrupt:
            print("Hey Dude, see you next time")
    if selector == 2:
        time.sleep(2)
        try:
            fake = "."
            while fake <= ".....":
                fake = fake + "."
                print("\r" + Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "Please Wait" + str(fake), end="")
                time.sleep(0.5)
            print("")
            os.system("python3 peril.py")
        except KeyboardInterrupt:
            print("Hey Dude, see you next time")


if chooser >=3:
    print(Colours.green + "[" + Colours.red + "-" + Colours.green+"]" +Colours.red + "   What the hell Man! you didn't see the menu -.+'"+Colours.green)