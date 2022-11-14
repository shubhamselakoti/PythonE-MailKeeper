import validator
import storage
import colors

def details():
    userName = 'q'
    cnt = 0
    while not validator.check(userName):
        userName = input("Enter Email Id (or enter q to exit): ")
        if userName.lower() == 'q':
            return
        if validator.check(userName):
            name = userName.split("@")
            print(colors.bcolors.OKGREEN+userName, "registered...."+colors.bcolors.ENDC)
            print("="*50)
            storage.addUser(userName)
            details()
        else:
            print(colors.bcolors.WARNING+"Sorry, This Email Id Is Incorrect !!!!!"+colors.bcolors.ENDC)
        cnt += 1
        if cnt == 3:
            print("*"*50)
            print("You Have Entered Incorrect Mail Id Many Times, Please Try Again Later.")
            break
        print("-"*50)
