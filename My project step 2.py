people = []

def addPerson(name, age, id_number):
    # Create a dictionary with all the variables
    person = {'name': name, 'age': age, 'id_number': id_number}
    people.append(person)
    print("Added " + name + " with ID " + str(id_number) + " saved successfully.")

def findById():
    # Getting ID from the user
    id_number = input("Please enter ID number: ")
    for person in people:
        # Check if the selection is inside the variable:
        if person["id_number"] == id_number:
            return person
    return "ID number not found"

def printAgeAverage():
    if len(people) == 0:
        print("No data available.")
        return
    total_age = 0
    for person in people:
        # Sum of ages
        total_age += person["age"]
    average_age = total_age / len(people)
    print("Average age: " + str(average_age))

def printPerson():
    if len(people) == 0:
        print("No data available.")
        return
    for index, person in enumerate(people):
        print("Index: " + str(index) + " - Name: " + person['name'] + ", ID: " + person['id_number'])

def printNames():
    if len(people) == 0:
        print("No data available.")
        return
    for index, person in enumerate(people):
        print("Index: " + str(index) + " - Name: " + person["name"])

def printID():
    if len(people) == 0:
        print("No data available.")
        return
    for index, person in enumerate(people):
        print("Index: " + str(index) + " - ID: " + person["id_number"])

def personByIndex(index):
    if 0 <= index < len(people):
        person = people[index]
        print("Name: " + person["name"] + ", Age: " + str(person["age"]) + ", ID: " + person["id_number"])
    else:
        print("Index out of range")

# Using all the last 7 functions in one main function
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
            age = int(input("Enter age: "))
            id_number = input("Enter ID number: ")
            # This function gets all these variables - name, age, and id_number
            addPerson(name, age, id_number)
        
        # Search by ID
        elif choice == "2":
            person = findById()
            if person == "ID number not found":
                print(person)
            else:
                print("Name: " + person['name'] + ", Age: " + str(person['age']) + ", ID: " + person['id_number'])
        
        # Ages average
        elif choice == "3":
            printAgeAverage()
        
        # Print names
        elif choice == "4":
            printNames()
        
        # Print IDs
        elif choice == "5":
            printID()
        
        # Print all entries
        elif choice == "6":
            printPerson()
        
        # Print entry by index
        elif choice == "7":
            index = int(input("Enter index: "))
            personByIndex(index)
        
        # Exit
        elif choice == "8":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

mixAllFunctions()
   
        