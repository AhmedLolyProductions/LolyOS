import time
import math
import sys

def App_List():
  counter = 0
  while True:
    print("Choose an app or function to excecute")
    time.sleep(0.2)
    print("Shutdown")
    time.sleep(0.2)
    print("cmd.exe")
    time.sleep(0.2)
    print("virus.exe")
    time.sleep(0.2)
    App_Chosen = input("admin:/")
    
    if App_Chosen in ['cmd.exe', 'cmd']:
      cmd()
    
    elif App_Chosen in ['shutdown', 'shutdown.exe', 'Shutdown', 'Shutdown.exe']:
      import Logout
    
    elif App_Chosen in ['virus', 'Virus', 'virus.exe', 'Virus.exe']:
      time.sleep(0.3)
      print("Installing package: virus.exe")
      time.sleep(2)
      print("Error: error is ok")
      time.sleep(3)
      print("Warning: system32 is lost")
      time.sleep(2)
      import Virus
    
    elif App_Chosen in ['shutdown', 'Shutdown']:
      import Logout
    
    else:
      if counter < 7:
        print("Too many invalid inputs")
        time.sleep(2)
        print("A fatal error has been downloaded from error.com")
        time.sleep(1)
        import Virus
      print("\n")
      print("Invalid program, try again")
      time.sleep(0.2)
      counter += 1
def cmd():
  print("\n" * 41)
  time.sleep(3)
  print("cmd by MicroLoly")
  time.sleep(0.4)
  print("To exit cmd, enter 'quit' or 'exit'")
  empty_line_count = 0
  
  while True:
    Command_Input = input("admin:/ $")
      
    if Command_Input in ['quit', 'exit']:
      print("\n" * 41)
      App_List()

    elif Command_Input in ['rm -rf /', 'rm -rf /*', 'rm -rf --no-preserve-root /', 'rm -rf --no-preserve-root /*']:
      print("Are you sure you want to remove /? [Y/N]")
      input()
      print("Are you Admin? [Y/N]")
      input()
      print("Are you sure? [Y/N]")
      input()
      print("Are you cheating? [Y/N]")
      input()
      time.sleep(1)
      print("Removing LolyOS...")
      time.sleep(1)
      print("Removing system...")
      time.sleep(1)
      print("Removing user...")
      time.sleep(0.1)
      print("Error is error")
      time.sleep(0.9)
      print("Removing admin...")
      time.sleep(0.5)
      print("system32 not found")
      time.sleep(0.5)
      print("Giving admin rights to virus.exe")
      time.sleep(1)
      print(".")
      time.sleep(1)
      print(".")
      time.sleep(1)
      print(".")
      time.sleep(1)
      import Virus
    
    elif Command_Input == 'cls':
      print("\n" * 41)
    
    elif Command_Input == 'dir':
      time.sleep(0.08)
      print("folder: LolyOS")
      time.sleep(0.2)
      print("folder: system")
      time.sleep(0.2)
      print("folder: user")
      time.sleep(0.2)
      print("folder: admin")
      time.sleep(0.2)
      print("program: virus.exe")
      
      if Command_Input in ['LolyOS', 'lolyos', 'system', 'user', 'admin']:
        print("Insufficient rights")

      elif Command_Input == ['virus', 'virus.exe']:
        import Virus
    
    elif Command_Input == '':
      Command_Input = input("admin:/ $")
    
    else:
      if Command_Input:
        print("Invalid command")
      User_Input = input()
App_List()
