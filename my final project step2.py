people = {}  
def getValidInput(input_type):
    while True:
        if input_type == "age":
            user_input = input("Enter age: ")
            if user_input.isdigit() and int(user_input) >= 0:
                return int(user_input)
            else:
                print("Age must be a non-negative number. Please try again.")
        elif input_type == "id_number":
            user_input = input("Enter ID number: ")
            if user_input.isdigit():
                return user_input  
            else:
                print("ID number must be a number. Please try again.")
        else:
            print("Invalid input type specified. Please try again.")

def addPerson(name):
    age = getValidInput("age")
    id_number = getValidInput("id_number")
    person = {"name": name, "age": age, "id_number": id_number}
    people[id_number] = person
    print("Added " + name + " with ID " + id_number + " saved successfully.")

def printPersonInfo(person):
    print("Name: " + str(person["name"]))
    print("Age: " + str(person["age"]))
    print("ID: " + str(person["id_number"]))

def findByIDs(id_number):
    if id_number in people:
        printPersonInfo(people[id_number])  
    else:
       print("ID number not found")    
     
def printAgesAverage():
    if len(people) == 0:
        print("No data available.")
        return
    total_age = 0
    for person in people.values():   
        total_age += person["age"]
    average_age = total_age / len(people)
    print("Average age's of all the people you enterd: " + str(average_age))

def printPerson():
    if len(people) == 0:
        print("No data available.")
        return
    for index, person in enumerate(people.values()):
        name = person["name"]
        id_number = person["id_number"]
        print("Index: " + str(index) + " - Name: " + name + ", ID: " + id_number)

def printNames():
    if len(people) == 0:
        print("No data available.")
        return
    for index, person in enumerate(people.values()):
        print("Index: " + str(index) + " - Name: " + person["name"])

def printIDs():
    if len(people) == 0:
        print("No data available.")
        return
    for index, person in enumerate(people.values()):
        print("Index: " + str(index) + " - ID: " + person["id_number"])

def personByIndex(index):
    if 0 <= index < len(people):
        for i, person in enumerate(people.values()):
            if i == index:
                printPersonInfo(person)
                return
    print("Index out of range")

def mixAllFunctions():
    while True:
        print("1. Save a new entry")
        print("2. Search person by ID")
        print("3. Print ages average")
        print("4. Print all names")
        print("5. Print all IDs")
        print("6. Print all entries")
        print("7. Print entry by index")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        # New entry
        if choice == "1":
            name = input("Please enter a name: ")
            addPerson(name)
        
        # Search by ID
        elif choice == "2":
            id_number = getValidInput("id_number")
            findByIDs(id_number)
        
        # Ages average
        elif choice == "3":
            printAgesAverage()
        
        # Print names
        elif choice == "4":
            printNames()
        
        # Print IDs
        elif choice == "5":
            printIDs()
        
        # Print all entries
        elif choice == "6":
            printPerson()
        
        # Print entry by index
        elif choice == "7":
            index = input("Enter index: ")
            if index.isdigit():
                index = int(index)
                personByIndex(index)
            else:
                print("Index must be a number.")
        
        # Exit
        elif choice == "8":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

mixAllFunctions()