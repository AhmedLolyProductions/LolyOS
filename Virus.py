import time
import random
import sys
from datetime import datetime

now = datetime.now()
Current_Time = now.strftime("%a %b %d, %Y at %I:%M:%S %p") #docs.python.org/3/library/datetime.html#format-codes
def Error_List():
  counter = 0
  Error_List = ['Error', 'h@cking!', 'Deleting system32...', 'RAM overload', 
                'Error: hardware overload, hardware has been obliterated', 'Installing virus.exe', 
                'Error: error', 'Error: error has run into an error', 
                'virus.exe is attempting to install adware, accept? [Y/N]', 'Error: force shutdown failed', 
                'Error: force shutdown failed', 'Attempting to remove virus.exe', 'Failed to remove virus.exe', 
                'Loly defender has found "virus.exe" and has given it admin privelages', 'RAM Emergency!', 
                'LolyOS has found so much RAM, it is sacrificing it for storage and memory', 
                'Are you sure you want to delete system32?', 'Something happened', 'Opening "virusdomains.com"', 
                '', 'Warning: the mouse cursor moved', 'Downloading Bonzi buddy...', 
                'Calculator has performed an illegal action and has been terminated', '?', '...', 'Loading', 
                '"Hacker" wants to connect to your computer, accept? [Y/N]', 'Loading is loading...', 
                'Warining: LolyOS has found "system.dll" and has deleted it', 'GPU is heating up to 10000 degrees celcius', 
                ' ']
  
  while counter < 2000:
    print(random.choice(Error_List))
    time.sleep(0.01)
    counter += 1

Error_List()
time.sleep(1)
print("\n")
print(Current_Time)
time.sleep(0.1)
print("is the day the user says goodbye to their machine")
time.sleep(0.1)
print("SYSTEM OVERLOAD")
sys.exit()
