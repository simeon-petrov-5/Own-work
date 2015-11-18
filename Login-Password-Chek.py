#Programm for checking your password.

un=["Simo"]
pw=["123"]


def registering():
    defa=False
    while defa is False:
        userName=input("Enter your username: ")
        if userName in un:
            print("This username is already taken. Please choose a new one.")
            defa=False
        else:
                defa=True
    passWord=input("Enter your password: ")
    un.append(userName)
    pw.append(passWord)


def loggin():
    defb=False
    while defb is False:
        print("\nLogin stage")
        unEnter=input("Please enter your username: ")
        pwEnter=input("Please enter your password: ")
        if unEnter in un:
            if pwEnter in pw:
                print("Logging in. Please wait.")
                print("Welcome to the system.")
                defb=True
            else:
                print("Error. Incorrect password.Try again.")
                defb=False
        else:
            print("Error. Incorrect username.Try again.")
            defb=False


print("""Welcome to our system.
For Loggin choose 1.
For registering choose 2.""")
choose=int(input("Enter your decision here: "))
if choose is 1:
    loggin()
elif choose is 2:
    registering()
else:
    print("Error.")



#-----------------------------------------------------
#With files, appending and password chek

un=open("Username.txt", "w")
un.write("simo")
un.close()
pw=open("Password.txt", "w")
pw.write("123")
pw.close()
variableforpassing = False


def passwordChek(passWord):
        if any(p.islower() for p in passWord)==True:
            print("LowerCase chek - OK")
            if any(p.isupper() for p in passWord)==True:
                print("UpperCase chek - OK")
                if any(p.isdigit() for p in passWord)==True:
                    print("DigitChek chek - OK")
                    print("\nYour password is perfect!")
                    global variableforpassing
                    variableforpassing = True
                else:
                    print("Add some numbers to your password for greater security!")
            else:
                if any(p.isdigit() for p in passWord)==True:
                    print("DigitChek chek - OK")
                    print("\nYour password is good!")
                    print("Add some upper case characters to your password!")
                    variableforpassing = True
                else:
                    print("Add some upper case characters to your password!")
                    print("Add some numbers to your password!")
        else:
            print("Mix lower and upper case character for better result!")


def registering():
    defa=False
    while defa is False:
        userName=input("Enter your username: ")
        if userName in open("Username.txt").read():
            print("This username is already taken. Please choose a new one.")
            defa=False
        else:
                defa=True
    passWord=input("Enter your password: ")
    un=open("Username.txt", "a")
    un.write(userName)
    un.close()
    passwordChek(passWord)
    if variableforpassing is True:
        pw=open("Password.txt", "a")
        pw.write(passWord)
        pw.close()


def loggin():
    defb=False
    while defb is False:
        print("\nLogin stage")
        unEnter=input("Please enter your username: ")
        pwEnter=input("Please enter your password: ")
        if unEnter in open("Username.txt").read():
            if pwEnter in open("Password.txt").read():
                print("Logging in. Please wait.")
                print("Welcome to the system.")
                defb=True
            else:
                print("Error. Incorrect password.Try again.")
                defb=False
        else:
            print("Error. Incorrect username.Try again.")
            defb=False

defc=False
while defc is False:
    print("""Welcome to our system.
    For Loggin choose 1.
    For registering choose 2.
    For exit choose 3""")
    choose=int(input("Enter your decision here: "))
    if choose is 1:
        loggin()
        print("\n")
    elif choose is 2:
        registering()
        print("\n")
    elif choose is 3:
        defc=True
    else:
        print("Error.")
        print("\n")
