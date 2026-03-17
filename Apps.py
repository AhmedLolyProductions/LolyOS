import time
import math
import sys

def App_List():
  counter = 0
  while True:
    print("Choose an app to excecute")
    time.sleep(0.2)
    print("Shutdown")
    time.sleep(0.2)
    print("Calculator.exe")
    time.sleep(0.2)
    print("cmd.exe")
    time.sleep(0.2)
    print("virus.exe")
    time.sleep(0.2)
    print("Shutdown")
    time.sleep(0.2)
    App_Chosen = input("admin:/")
    
    if App_Chosen in ['cmd.exe', 'cmd']:
      cmd()
    
    elif App_Chosen in ['calc', 'calculator.exe', 'calc.exe', 'calculator', 'Calculator', 'Calculator.exe']:
      Calc()
    
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
    
    elif App_Chosen in ['shutdown', 'Shutdown', 'quit', 'exit']:
      import Logout
    
    else:
      if counter < 7:
        print("Too many invalid inputs")
        time.sleep(2)
        print("Shutting down")
        time.sleep(1)
        import Logout
      print("\n")
      print("Invalid program, try again")
      time.sleep(0.2)
      counter += 1
def cmd():
  print("\n" * 41)
  time.sleep(3)
  print("Hello! This is the command prompt where you can run commands")
  time.sleep(0.4)
  print("To exit cmd, enter quit or exit")
  
  empty_line_count = 0
  
  while True:
    Command_Input = input("admin:/ $")
      
    if Command_Input == 'quit' or 'exit':
      print("\n" * 41)
      return App_List()
    
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
    
    elif Command_Input == '':
      Command_Input = input("admin:/ $")
    
    else:
      if Command_Input:
        print("Invalid command")
def Calc():
  while True:
    print("\n" * 41)
    print("Sorry, but calulator is under construction! Math equations entered will not work")
    time.sleep(0.3)
    print("To exit the calculator, enter quit or exit")
    time.sleep(0.3)
    User_Input = input()
    
    if User_Input in ['quit', 'exit', 'Quit', 'Exit']:
      print("\n" * 41)
      App_List()
    
    else:
      print("Invalid equation or command")
      print("\n")
      User_Input = input()
