import colors
def intro():
    print()
    print("*"*50)
    print(colors.bcolors.HEADER+"Welcome Back")
    print("How May We Help You???"+colors.bcolors.ENDC)
    while True:
        print(colors.bcolors.OKCYAN+'''
        press 1 to enter a new Mail Account
        press 2 to see the Mail Accounts
        press any other key to exit.
        '''+colors.bcolors.ENDC)
        print()

        a = input("Enter Your Choice: ")

        if a == '1':
            import Details
            print("*" * 50)
            Details.details()
        elif a == '2':
            import printData
            print("*"*50)
            print(colors.bcolors.OKCYAN+'''
            Press
            1 for Names Only
            2 for Domain Names
            3 for Both Names and Domain
            4 for Email Id
            5 for ALL
            any other key to go in previous page.
            '''+colors.bcolors.ENDC)
            choice = input("Enter Any Key: ")
            while len(choice) > 1 or choice not in '12345':
                intro()
            else:
                printData.printUser(choice)
        else:
            break

intro()