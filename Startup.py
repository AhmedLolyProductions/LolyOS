import time
from datetime import datetime
import sys

def Greeting():
  #<settings>
  Greeting_Status = 2
  Logging = "Logging On..." #1
  Loading = "Loading..." #0.5
  Empty = "" #0
  Custom = "Logging In..." #2
  #</settings>
  
  now = datetime.now()
  Current_Time = now.strftime("%a %b %d, %Y at %I:%M:%S %p") #docs.python.org/3/library/datetime.html#format-codes
  time.sleep(0.3)
  
  if Greeting_Status in [0, 0.5, 1, 2]:
      if Greeting_Status == 1:
        time.sleep(0.4)
        print(Logging)
        time.sleep(0.6)
        print(f"Today is {Current_Time}")
        time.sleep(1.4)
        print("\n")
        import Apps
      
      elif Greeting_Status == 0.5:
        time.sleep(0.4)
        print(Loading)
        time.sleep(0.6)
        print(f"Today is {Current_Time}")
        time.sleep(1.4)
        print("\n")
        import Apps
      
      elif Greeting_Status == 0:
        time.sleep(0.4)
        print(Empty)
        time.sleep(0.6)
        print(f"Today is {Current_Time}")
        time.sleep(1.4)
        print("\n")
        import Apps
      
      elif Greeting_Status == 2:
        time.sleep(0.4)
        print(Custom)
        time.sleep(0.6)
        print(f"Today is {Current_Time}")
        time.sleep(1.4)
        print("\n")
        import Apps
  
  else:
    time.sleep(0.4)
    print("")
    time.sleep(0.6)
    print(f"Today is {Current_Time}")
def Password():
  #<settings>
  Password = "password"
  counter = 0
  time.sleep(0.6)
  print("Loading...")
  time.sleep(0.6)
  print("Welcome!")
  time.sleep(0.4)
  print("Enter password")
  Password_Input = input("Password:")
  #</settings>
  
  if Password_Input == Password:
    time.sleep(0.4)
    Greeting()
  
  else:
    while counter < 4:
      time.sleep(0.37)
      print("\n")
      print("Invalid password")
      Password_Input = input("Password:")
      counter += 1
      
      if Password_Input == Password:
        time.sleep(0.4)
        Greeting()
def Startup():
  counter = 0
  time.sleep(1)
  print("Startup the operating system? [Y/N]")
  y_n = input("admin:/")
  
  if y_n in ['y', 'Y', 'yes', 'Yes']:
    print("Starting LolyOS")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    Password()
  
  elif y_n in ['n', 'N', 'no', 'No']:
    import Logout
  
  else:
    while counter < 3:
      print("\n")
      print("Please try again")
      y_n = input("admin:/")
      counter += 1
      
      if y_n in ['y', 'Y', 'yes', 'Yes']:
        print("Starting LolyOS")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        Password()
      
      elif y_n in ['n', 'N', 'no', 'No']:
        import Logout
      
      if counter == 3 and y_n not in ['y', 'Y', 'yes', 'Yes', 'n', 'N', 'No', 'no']:
        print("Too many invalid inputs, shutting down...")
        time.sleep(1)
        import Logout
Startup()
