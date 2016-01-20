# Програма за вкарване на поканени в лист; запазването на листа във файл; възможност за добавяне към файла още участници(лист) или данни (str)

definingInput = True
while definingInput == True:
    print("""Hello, here are our options:
    [1] Enter a list of people attanding your party
    [2] Append more people to the first list
    [3] Append data to the list
    [4] Remove a name/guest
    [5] Read the list
    [6] Exit
    """)
    userChoice = input ("Enter your choice here: ")
    if userChoice == "1":
        print("\n\n\t\tEnter a list of people attanding your party\n")
        numGuests = input("Specify how many guest would be attending the party: ")
        i = int(numGuests)
        counter = 0
        guests = []

        while counter <i:
            name = input("Enter the name here: ")
            guests.append(name)
            counter = counter +1

        guests.sort()
        print("Here is the list of all your guests: \n")
        for guest in guests:
            print(guest)

        fileName = "demo.txt"
        accessMode = "w"
        file = open(fileName, accessMode)
        file.write("Here is the list of all your guests:")
        for guest in guests:
            file.write("\n" + str(guest))
        print("Your list was successfuly saved!\n\n")
        file.close()
        definingInput = True

    elif userChoice == "2":
        print("\n\n\t\tAppend more people to the first list\n")
        numGuests = input("\nSpecify how many guest would you like to attend to the list: ")
        i = int(numGuests)
        counter = 0
        guests = []
        while counter <i:
            name = input("Enter the name here: ")
            guests.append(name)
            counter = counter +1
        guests.sort()
        fileName = "demo.txt"
        accessMode ="a"
        file = open(fileName, accessMode)
        for guest in guests:
            file.write("\n" + str(guest))
        print("Your list was successfuly saved!\n\n")
        file.close
        definingInput = True

    elif userChoice == "3":
        print("\n\n\t\tAppend data to the list\n")
        data = input("Enter your data: ")
        fileName = "demo.txt"
        accessMode ="a"
        file = open(fileName, accessMode)
        file.write("\n" + data)
        print("Your list was successfuly saved!\n\n")
        file.close
        definingInput = True

    elif userChoice == "4":
        print("\n\n\t\tRemove a name/guest\n")
        n = input("Who you want to remove? ")
        guests.remove(n)
        file = open("demo.txt", "w")
        file.write("Here is the list of all your guests:")
        for guest in guests:
            file.write("\n" + str(guest))
        print("Your list was successfuly saved!\n\n")
        definingInput = True

    elif userChoice == "5":
        print("\n\n\t\tRead the list\n")
        with open("demo.txt", "r") as file:
            printfile = file.read()
            print(printfile)
        print("\n\n")
        definingInput = True

    elif userChoice == "6":
        print("Thank you for using the programm. Exit.\n\n")
        definingInput = False