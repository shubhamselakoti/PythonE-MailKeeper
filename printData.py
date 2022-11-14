import pickle


def printDomain():
    with open('domain.txt', 'rb') as file:
        try:
            domains = pickle.load(file)
        except EOFError:
            domains = []
            print("Domain File Is Empty... Please Insert Some Ids First!!!")
            return
    print(domains)


def printNames():
    with open('names.txt', 'rb') as file:
        try:
            names = pickle.load(file)
        except EOFError:
            names = []
            print("Names File Is Empty... Please Insert Some Ids First!!!")
            return
    print(names)


def printMail():
    with open('emailId.txt', 'rb') as file:
        try:
            mailId = pickle.load(file)
        except EOFError:
            mailId = []
            print("Mail File Is Empty... Please Insert Some Ids First!!!")
            return
    print(mailId)


def printUser(a):
    if a == '1':
        printNames()
    elif a == '2':
        printDomain()
    elif a == '3':
        printNames()
        printDomain()
    elif a == '4':
        printMail()
    else:
        printNames()
        printDomain()
        printMail()
