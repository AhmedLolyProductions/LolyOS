from time import sleep
from datetime import datetime

def Greeting():
    now = datetime.now()
    Current_Time = now.strftime("%a %b %d, %Y at %I:%M:%S %p") #docs.python.org/3/library datetime.html#format-codes
    sleep(0.7)
    print("Logging in...")
    sleep(0.6)
    print(f"Today is {Current_Time}")
    sleep(1.4)
    print("\n")
    import Apps
def Password():
    Password = "password"
    counter = 0
    sleep(0.6)
    print("Loading...")
    sleep(0.6)
    print("Welcome!")
    sleep(0.4)
    print("Enter password")
    Password_Input = input("Password: ")

    if Password_Input == Password:
        sleep(0.4)
        Greeting()

    else:
        while counter < 4:
            sleep(0.37)
            print("\n")
            print("Invalid password")
            Password_Input = input("Password: ")
            counter += 1
      
            if Password_Input == Password:
                sleep(0.4)
                Greeting()
        sleep(0.2)
        print("Too many inncorrect attempts, unauthorized anomoly detected")
        sleep(4)
        print("Initiating Loly Defender on full gaurd...")
        sleep(5)
        print("Warning: Loly Defender has been disabled")
        sleep(5)
        import Virus
def Startup():
    counter = 0
    sleep(1)
    print("Startup the operating system? [Y/N]")
    y_n = input("admin:/ ")

    if y_n in ['y', 'Y', 'yes', 'Yes']:
        print("Starting LolyOS")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        Password()

    elif y_n in ['n', 'N', 'no', 'No']:
        import Shutdown

    else:
        while counter < 3:
            print("\n")
            print("Please try again")
            y_n = input("admin:/ ")
            counter += 1

        if y_n in ['y', 'Y', 'yes', 'Yes']:
            print("Starting LolyOS")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            sleep(1)
            print(".")
            sleep(1)
            Password()

        elif y_n in ['n', 'N', 'no', 'No']:
            import Shutdown

        elif counter == 3 and y_n not in ['y', 'Y', 'yes', 'Yes', 'n', 'N', 'No', 'no']:
            print("Too many invalid inputs, unauthorized anomoly detected")
            sleep(4)
            print("Warning: Virus.exe has gained")
            import Shutdown
Startup()
