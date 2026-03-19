import time

#User Notes:
  #The password is password
  #The password can be changed in Startup.py > Password() > <settings>
  #To begin installation media instead of normal boot, set the Installation variable to 1

def Install():
  print("Please select an installation media to begin")
  time.sleep(0.2)
  print("1: LolyOS installation media")
  time.sleep(0.2)
  print("2: Uknown suspicious installation media")
  time.sleep(0.2)
  print("3: Shutdown")
  time.sleep(0.2)
  print("4: UEFI options")
  time.sleep(0.2)
  Media_Option = input("Choose an option:")
  
  if Media_Option == '1':
    print("Installing...")
    time.sleep(1)
    print("Why not get a real job while the OS is still installing?")
    time.sleep(0.4)
    print("Go to www.findarealjob.com")
    time.sleep(4)
    print("Estimated time until completion: 3000 decades")
    time.sleep(6)
    print("Installation sucess")
    print("Note: Turn off the installation setup in main.py > BIOS()")
    time.sleep(0.5)
    print("Restarting to newly installed OS")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    import Startup
  
  elif Media_Option == '2':
    print("Installing...")
    time.sleep(3)
    print("Error")
    time.sleep(2)
    print("Deleting system32...")
    time.sleep(3)
    print("Importing virus...")
    time.sleep(2)
    import Virus
  
  elif Media_Option == '3':
    import Logout
  
  elif Media_Option == '4':
    print("Error: There is no such thing as 'UEFI', restarting to available OS")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(0.5)
    import Startup
  
  else:
    print("Invalid option, try again")
    print("\n")
    BIOS()
def BIOS():
  #<settings>
  Installation = 0
  #</settings>
  
  if Installation == 1:
    Install()
  
  elif Installation == 0:
    import Startup
  
  else:
    time.sleep(0.8)
    print("Error: Startup misconfigured in main.py")
    time.sleep(2)
    print("Restarting to main OS")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(0.5)
    import Startup
BIOS()
