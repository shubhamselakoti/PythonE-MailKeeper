import pickle


def addUser(userName):
    with open('emailId.txt', 'rb') as file:
        try:
            mailId = pickle.load(file)
        except EOFError:
            mailId = []

    with open('domain.txt', 'rb') as file:
        try:
            domains = pickle.load(file)
        except EOFError:
            domains = []

    with open('names.txt', 'rb') as file:
        try:
            names = pickle.load(file)
        except EOFError:
            names = []

    x = userName.split("@")

    mailId.append(userName)
    domains.append(x[1])
    names.append(x[0])

    pickle.dump(mailId, open("emailId.txt", "wb"))
    pickle.dump(domains, open("domain.txt", "wb"))
    pickle.dump(names, open("names.txt", "wb"))
