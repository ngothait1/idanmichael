def getValidInput(message):
    # Make sure it's a number
    while True:
        user_input = input(message)
        if user_input.isdigit():
            return int(user_input)
        else:
            print(user_input + " should be a number. Please try again.")

def addPerson(people, avg):
    # avg is a dictionary; we use it in this function to update the person's age anytime
    name = input("Enter name: ")
    age = getValidInput("Enter age: ")
    id_number = input("Enter ID number: ") 

    person = {"name": name, "age": age, "id_number": id_number}
    people[id_number] = person
    avg["age"] += age
    avg["count"] += 1

    print("The last person was added successfully.")

def printPersonInfo(person):
    print("Name: " + person["name"])
    print("Age: " + str(person["age"]))
    print("ID: " + str(person["id_number"]))

def findByIDs(id_number, people):
    # Checking if the ID entered by the user is in the dictionary 
    if id_number in people:
        # Using only the ID number 
        printPersonInfo(people[id_number])
    else:
        print("ID number not found.")

def printAgesAverage(avg, people):
    if len(people) == 0:
        print("No data available.")
        return
    # Here we are taking the total age and dividing by the number of people
    average_age = avg["age"] / len(people)
    print("Average age of all the people you entered: " + str(average_age))

def printPerson(people):
    if len(people) == 0:
        print("No data available.")
        return
    for index, person in enumerate(people.values()):
        print("Index: " + str(index) + " - Name: " + person["name"] + ", ID: " + str(person["id_number"]))

def printNames(people):
    if len(people) == 0:
        print("No data available.")
        return
    for index, person in enumerate(people.values()):
        print("Index: " + str(index) + " - Name: " + person["name"])

def printIDs(people):
    if len(people) == 0:
        print("No data available.")
        return
    for index, person in enumerate(people.values()):
        print("Index: " + str(index) + " - ID: " + str(person["id_number"]))

def personByIndex(people):
    index = getValidInput("Enter index: ")
    # Checking if the index provided by the user is valid
    for i, person in enumerate(people.values()):
        if i == index:
            printPersonInfo(person)
            return
    
    print("Index out of range.")

def main(): 
    avg = {"age": 0, "count": 0}
    people = {}
    while True:  
        print("\n1. Save a new entry")
        print("2. Search person by ID")
        print("3. Print average age")
        print("4. Print all names")
        print("5. Print all IDs")
        print("6. Print all entries")
        print("7. Print entry by index")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        # The selection must be a number between 1 and 8 
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                addPerson(people, avg)
            elif choice == 2:
                id_number = input("Please enter ID number: ")
                findByIDs(id_number, people)
            elif choice == 3:
                printAgesAverage(avg, people)
            elif choice == 4:
                printNames(people)
            elif choice == 5:
                printIDs(people)
            elif choice == 6:
                printPerson(people)
            elif choice == 7:
                personByIndex(people)
            elif choice == 8:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

main()