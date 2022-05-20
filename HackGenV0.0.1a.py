#By Leodeng 
#2022 The Interstellar Programmers
#Under the CC-BY-NC Licence
#OS: Mac
#Environment: Python 3

#****NOTES****
#Use Python 3 as the interpreter, Python 2 will not load the progress bar


#Citations :3: 
#https://www.jb51.net/article/203570.htm(PROGRESS BAR)
#https://tools.kalvinbg.cn/



#LIBS
import time
import os
import sys
import random

cmdweather = "curl wttr.in/"

downloadlistb = {1: '.NET Framework', 2: 'Python 3.7', 3: 'Kernel_TASK.dat', 4: '', 5: 'brew_install.sh', 6: 'Dogecoin-Core.app', 7: 'Apple_kit_framework', 8: 'AppleCoreServices', 9: 'DriverExtensions', 10: 'Crashes.log', 11: 'Backup.dat', 12: '_config.yml', 13: 'ApacheV2', 14: 'XAMPP.dat', 15: 'VBoxNetDHCP', 16: 'NAS.dll', 17: 'VBOX', 18: 'Wifi-Config.yaml', 19: 'php.exe', 20: 'mscvrtISPcontrol.dll', 21: 'BearWWW-NAT-Bridge.exe', 22: 'WindowsDefender-UNKNOWN SOURCES APPS.dll', 23: 'WDharddrive.bundle', 24: 'sshkey.rsa', 25: 'sshkey1.rsa.pub', 26: 'libGLESv2.dll', 27: 'd3dcompiler_47.dll', 28: 'retryfail.log', 29: 'flashdriver3.20.exe', 30: 'calclisthistory.txt'}
downloadlista = {1: '.NET Framework', 2: 'Python 3.7', 3: 'Kernel_TASK.dat', 4: '', 5: 'brew_install.sh', 6: 'Dogecoin-Core.app', 7: 'Apple_kit_framework', 8: 'AppleCoreServices', 9: 'DriverExtensions', 10: 'Crashes.log', 11: 'Backup.dat', 12: '_config.yml', 13: 'ApacheV2', 14: 'XAMPP.dat', 15: 'VBoxNetDHCP', 16: 'NAS.dll', 17: 'VBOX', 18: 'Wifi-Config.yaml', 19: 'php.exe', 20: 'mscvrtISPcontrol.dll', 21: 'BearWWW-NAT-Bridge.exe', 22: 'WindowsDefender-UNKNOWN SOURCES APPS.dll', 23: 'WDharddrive.bundle', 24: 'sshkey.rsa', 25: 'sshkey1.rsa.pub', 26: 'libGLESv2.dll', 27: 'd3dcompiler_47.dll', 28: 'retryfail.log', 29: 'flashdriver3.20.exe', 30: 'calclisthistory.txt'}
for c in downloadlistb.keys():
    a = random.sample(downloadlista.keys(), 1)  
    b = a[0] 



def d_progress_bar():
  for i in range(1, 101):
    print("\r", end = "")
    print("Downloading",downloadlista[b], "{}%: ".format(i), "▋" * (i // 1), end="")
    sys.stdout.flush()
    time.sleep(0.1)
 
    
 

#Loading screen
def progress_bar():
  for i in range(1, 101):
    os.system("clear")
    print("\r", end = "")
    print("Loading Necessary Components: {}%: ".format(i), "▋" * (i // 2), end="")
    sys.stdout.flush()
    time.sleep(0.007)
 
if __name__ == '__main__':
  progress_bar()
  time.sleep(1)

name = input("\n\n\n\nYour Display Name:")
username = name + "@" + name +".local>>>"
time.sleep(1)

#Main Menu (Loop after choice program is done running)
while True:
 os.system("clear")
 #Titles HackGen: English Version || ZBSQ: Chinese version || (All ascii text are generated from kalvintools in the citation area.) 
 time.sleep(0.01)
 print(" _   _            _     ____              ")
 time.sleep(0.01)
 print("| | | | __ _  ___| | __/ ___| ___ _ __    ")
 time.sleep(0.01)
 print("| |_| |/ _` |/ __| |/ / |  _ / _ \ '_ \   ")
 time.sleep(0.01)
 print("|  _  | (_| | (__|   <| |_| |  __/ | | |  ")
 time.sleep(0.01)
 print('|_| |_|\__,_|\___|_|\_\\\____|\___|_| |_| \n')
 time.sleep(0.01)
 print("Hacking/Programming Generator - Use code to AMAZE your friends!\n\n")
 time.sleep(0.01)
 print("---------------------------------------------------------------------------------------------------------")
 print(" _________ ____   ___    ______                               ____  _   ____  _                   ___  _ ")
 time.sleep(0.01)
 print("|__  / __ ) ___| / _ \  |__  / |__  _   _  __ _ _ __   __ _  | __ )(_) / ___|| |__   ___ _ __    / _ \(_)")
 time.sleep(0.01)
 print("  / /|  _ \___ \| | | |   / /| '_ \| | | |/ _` | '_ \ / _` | |  _ \| | \___ \| '_ \ / _ \ '_ \  | | | | |")
 time.sleep(0.01)
 print(" / /_| |_) |__) | |_| |  / /_| | | | |_| | (_| | | | | (_| | | |_) | |  ___) | | | |  __/ | | | | |_| | |")
 time.sleep(0.01)
 print("/____|____/____/ \__\_\ /____|_| |_|\__,_|\__,_|_| |_|\__, | |____/|_| |____/|_| |_|\___|_| |_|  \__\_\_|")
 time.sleep(0.01)
 print("                                                      |___/                                              \n ")
 time.sleep(0.01)
 print("装逼神器 —— 用代码秀翻你的朋友们!\n\n\n")
 #Choices for HackGEN
 logintime = time.asctime( time.localtime(time.time()) )
 print("HackGen Terminal V1.0.0 || Login Time:", logintime)
 print("ZBSQ 命令指示符 V1.0.0 || 登陆时间:", logintime)
 print("Enter 'help' for a list of commands...")

 userInput = input(username)

 if userInput == "help":
   print("\nCommands:")
   print("  cmd_rain - Hacker rain (101010101)")
   print("  cmd_weather - Command line weather, Must have Internet connection, consists of a 'curl' command")
   print("  d_parrot - Dancin Parrot, INTERNET CONNECTION REQUIRED!!!")
   print("  d_gen - Download command generator, fake a hacker...")
   print("")
   input("Press ENTER to continue...")
   continue

 if userInput == "cmd_rain":
   print("\nRemeber to press Ctrl+C to exit hacker rain, then press ENTER to reload\n\n\n")
   time.sleep(2)
   os.system('echo -e "1"; while $t; do for i in `seq 1 30`;do r="$[($RANDOM % 2)]";h="$[($RANDOM % 4)]";if [ $h -eq 1 ]; then v="0 $r";else v="1 $r";fi;v2="$v2 $v";done;echo  $v2;v2="";done;')
   input("Press ENTER to continue...")
   continue

 if userInput == "cmd_weather":
   wi = input("\nWhich city's weather do you need to look up for? (MUST BE REAL, CHINESE CITIES MUST USE PINYIN NAME, SPACE KEY IS NOT GOING TO WORK!):")
   curlw = cmdweather+wi
   os.system(curlw)
   input("Press ENTER to continue...")
   continue

 if userInput == "d_parrot":
   print("\nPress Ctrl+C to exit Dancin Parrot, then press ENTER to reload\n\n\n")
   time.sleep(2)
   os.system("curl parrot.live")
   input("Press ENTER to continue...")
   continue
 
 if userInput == "d_gen":
   print("\nPress Ctrl+C to exit Download command Generator...\n\n\n")
   time.sleep(2)
   os.system("clear")
   while True:
    if __name__ == '__main__':
      a = random.sample(downloadlista.keys(), 1) 
      b = a[0]
      d_progress_bar()
      print("\n")
      time.sleep(1)
   input("Press ENTER to continue...")
   continue
 
 
 if userInput != "help" or "cmd_weather" or "cmd_rain" or "d_parrot" or "hidehackgen":
   print("\nUnknown Command, please type 'Help' for a list of commands")
   input("Press ENTER to continue...")
   continue




