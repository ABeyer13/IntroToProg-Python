# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <ABEYER>,<5/12/2020>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

lstTable.append({"Task": 'Test', "Priority": '000'})
print(lstTable)

# -- Input/Output -- #
#- Display a menu of choices to the user-
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

# - Show the current items in the table -
    if (strChoice.strip() == '1'):
        print("Would you like to see your saved data or the unsaved data you entered?")
        Saved = input("Enter 's' for saved data and 'u' for all data: ")
        if Saved == 's':
            objFile = open("ToDoList.txt", "r")
            for rows in objFile:
                t, p = rows.split(",")
                dicRow = {"Task": t, "Priority": p.strip()}
                print(dicRow["Task"] + " | " + dicRow["Priority"])
                continue

        elif Saved == 'u':
            for items in lstTable:
                print(items)
            continue

        else:
            print("Please enter the letter 's' or 'u'. ")
            continue
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        while (True):
            Task = input("Enter the Task here: ")
            Priority = input("Enter the Priority number here: ")
            lstTable.append({"Task": Task, "Priority": Priority})
            print()
            print("Do you want to Exit?")
            print()
            leave = input("Type either 'y' for yes and 'n' to continue: ")
            if leave == 'y':
                break
            else:
                continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
            while (True):
                TaskRemove = input("Which task would you like to delete?: ")
                print()
                for dicRow in lstTable:
                    if dicRow["Task"].lower() == TaskRemove.lower():
                        lstTable.remove(dicRow)
                        print()
                        print(TaskRemove + ' was removed from your To Do list')
                        print("This is your updated list: " )
                        for dicRow in lstTable:
                            print(dicRow['Task'] + ',' + dicRow['Priority'])
                print()
                print("Do you want to Exit?")
                print()
                leave = input("Type either 'y' for yes and 'n' to continue: ")
                if leave == 'y':
                    break

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        print()
        for dicRow in lstTable:
            objFile.write(str(dicRow["Task"]) + " , " + str(dicRow["Priority"]) + "\n")
            print(dicRow["Task"] + ' , ' + dicRow["Priority"] + " : Saved To Memory!")
        objFile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Would you like to exit the program?")
        print()
        Exit = input("Type in 'y' for yes and 'n' for no: ")
        if Exit == 'y':
            break
        else:
            continue

input("Press the 'enter' key to exit the program.") #  Exit the program