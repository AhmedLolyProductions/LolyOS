from time import sleep

def BIOS():
    def CreditsAndVersion():
        sleep(1)
        print("github.com/AhmedLolyProductions")
        sleep(0.5)
        print("LolyOS v0.0.0-alpha")
        sleep(2)
        Boot()
    def ReBoot():
        sleep(1)
        print("Invalid Input")
        sleep(0.8)
        Boot()
    def Boot():
        print("\n" * 2, "Boot into 'LolyOS'? [Y/N]")
        User_Input = input("admin:/ $ ").lower()
        if User_Input in ['y', 'yes']:
            import Startup
        elif User_Input in ['n', 'no']:
            import Shutdown
        else:
            ReBoot()
    CreditsAndVersion()
BIOS()
if __name__ == "__main__":
    BIOS()
