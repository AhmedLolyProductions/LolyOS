from time import sleep

def App_List():
    print("Choose an app or function to execute")
    sleep(0.3)
    print("Shutdown")
    sleep(0.3)
    print("About LolyOS")
    sleep(0.3)
    print("cmd.exe")
    sleep(0.3)
    print("virus.exe")
    User_Input = input("admin:/ ").lower()
    if User_Input == 'shutdown':
        sleep(0.3)
        import Shutdown
    elif User_Input in ['about lolyos', 'lolyos', 'about']:
        About_LolyOS()
    elif User_Input in ['cmd', 'cmd.exe']:
        cmd()
    elif User_Input in ['virus', 'virus.exe']:
        import Virus
def About_LolyOS():
    print("\n")
    sleep(1)
    print("This is a fun little project maintained in free time (just for fun)")
    sleep(3)
    print("It is maintained at github.com/AhmedLolyProductions/LolyOS")
    sleep(3)
    print("The old version of LolyOS that's archived is github.com/AhmedLolyProductions/LolyOS-old")
    sleep(3)
    print("LolyOS v1.0.3")
    sleep(0.6)
    print("To go back to the app list, click 'enter'")
    input()
    print("\n" * 2)
    App_List()
def cmd():
    print("\n" * 41)
    sleep(3)
    print("LolyOS  Copyright (C) 2026  AhmedLolyProductions")
    sleep(0.4)
    print("To exit cmd, enter 'quit' or 'exit'")
    sleep(0.4)
    print("Type 'help' for a list of commands")
    while True:
        Command_Input = input("admin:/ $ ").lower()
        if Command_Input == 'help':
            print("\n")
            sleep(0.2)
            print("RMDIR: delete a directory")
            sleep(0.5)
            print("dir: display directorys")
            sleep(0.5)
            print("cls: clears the screen")
        elif Command_Input == 'rmdir':
            print("\n" + "please choose a directory to delete; for a list of directorys, type 'dir'")
        elif Command_Input == 'cls':
            print("\n" * 41)
        elif Command_Input == 'dir':
            print("\n" + "folder: LolyOS")
            sleep(0.2)
            print("folder: system")
            sleep(0.2)
            print("folder: user")
            sleep(0.2)
            print("folder: admin")
            sleep(0.2)
            print("file: virus.exe")
        elif Command_Input in ['rmdir lolyos', 'rmdir system', 'rmdir user', 'rmdir admin', 'rmdir virus.exe', 'rmdir virus']:
            import Virus
App_List()
