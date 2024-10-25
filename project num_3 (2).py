import pandas as pd
import json

def loadColumnNames():
    #path for json
    with open("/Users/idanmic/Desktop/project csv/project 3.json", "r") as json_dict: 
        data_json = json.load(json_dict)["columns"]
        return data_json
        
def saveToCSV(people):
     data = []
     column_names = loadColumnNames()
     for id_number, person in people.items():
        data.append({"ID": id_number, "Name": person["name"], "Age": person["age"]})
        #Create DataFrame
        df = pd.DataFrame(data, columns = column_names)
        #saving data to CSV 
        df.to_csv("/Users/idanmic/Desktop/project csv/people_info.csv", index = False)

def isNumber(num, description):
    # Check if the input is a non-negative integer
    if num.isdigit() and int(num) >= 0:
        return True
    else:
        print("Error: you tried to enter " + description + ", but it is not valid. Please enter only positive numbers.") 
        return False

def getOnlyNumber(message):
    #Make sure the user enter a valid number
    while True:
        user_input = input("Please enter " + message)
        if isNumber(user_input, message) and int(user_input) >= 0:
            # Return the valid input as an integer
            return int(user_input)  
        else:
            print("Your select: " + user_input + " - should be a non-negative number. Please try again.")

def addPerson(people, age_avg_dict):
    # Add a new person to the dictionary by inputs by the user
    name = input("Please enter name: ")  
    age = getOnlyNumber("age: ")  
    id_number = getOnlyNumber("ID number: ") 

    # Check for duplicate ID
    if str(id_number) in people:
        print("Error: This ID number already exists. Please enter another ID.")
        return

    # Create a dictionary for the person with their name and age
    person = {"name": name, "age": age}
    # Use the ID number as the key in the people dictionary
    people[str(id_number)] = person  

    # Update the total age for calculating average later
    age_avg_dict["age"] += age

    print("The last person was added successfully.")
    
def printPersonInfo(person, id_number):
    # Print the details of a person
    print("Name: " + person["name"])
    print("Age: " + str(person["age"]))
    print("ID: " + str(id_number))

def checkEmpty(people):
    # Check if the people dictionary is empty
    if len(people) == 0:
        print("No data available.")
        return True
    return False

def findByID(people):
    # Find and display a person by their ID number
    if checkEmpty(people):
        return
    id_number = getOnlyNumber("Please enter ID number: ")  
    if str(id_number) in people:
        printPersonInfo(people[str(id_number)], id_number)  
    else:
        print("ID number not found.")  

def printAgesAverage(age_avg_dict, people):
    # Calculate and print the average age of all people
    if checkEmpty(people):
        return
        # Calculate average age
    average_age = age_avg_dict["age"] / len(people)  
    print("Average age of all the people you entered: " + str(average_age))

def printAllPersons(people):
    # Print all persons in the people dictionary
    if checkEmpty(people):
        return
    for index, (id_number, person) in enumerate(people.items()):
        # Print the index of the person
        print("Index: " + str(index))  
        # Print the person's information
        printPersonInfo(person, id_number)  
        
def printNames(people):
    # Print the names of all people
    if checkEmpty(people):
        return
    for index, person in enumerate(people.values()):
        print("Index: " + str(index) + " - Name: " + person["name"])

def printIDs(people):
    # Print the ID numbers of all people
    if checkEmpty(people):
        return
    for index, id_number in enumerate(people.keys()):
        print("Index: " + str(index) + " - ID: " + str(id_number))

def personByIndex(people):
    if checkEmpty(people):
        return
    index = getOnlyNumber("Enter index: ")  
    if index < 0:
        print("Error: Negative numbers can't be used as an index.")  #
    else:
        # Check if the provided index is valid and print the corresponding person's info
        for i, (id_number, person) in enumerate(people.items()):
            if i == index:
                printPersonInfo(person, id_number)  
                return
    print("Index out of range.")  

def printInvalidChoice():
    
    print("Invalid choice. Please enter a number between 1 and 8.")

def runAll(): 
    # Main function to run the program
    age_avg_dict = {"age": 0}  
    people = {} 
    
    while True:  
        # All the options to the user
        print("1. Save a new entry")
        print("2. Search person by ID")
        print("3. Print average age")
        print("4. Print all names")
        print("5. Print all IDs")
        print("6. Print all entries")
        print("7. Print entry by index")
        print("8. Save all data")
        print("9. Exit")
        
        choice = input("Enter your choice (1-8): ")  
        if isNumber(choice, "choice"):  
            choice = int(choice)
            if choice == 1:
                addPerson(people, age_avg_dict)  
            elif choice == 2:
                findByID(people) 
            elif choice == 3:
                printAgesAverage(age_avg_dict, people)  
            elif choice == 4:
                printNames(people)  
            elif choice == 5:
                printIDs(people)  
            elif choice == 6:
                printAllPersons(people)  
            elif choice == 7:
                personByIndex(people)  
            elif choice == 8:
                saveToCSV(people)
                print("Data Saved successfully") 
            elif choice == 9:
                print("Exiting...")    
                break
            else:
                printInvalidChoice()  
        else:
            printInvalidChoice() 

        input("Press enter to continue...")  

# Run the main function to start the program
runAll()