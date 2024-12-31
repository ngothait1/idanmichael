import pandas as pd
from Person import Person
from Student import Student

csv_path = "/Users/idanmic/Desktop/Big project/people_info.csv"

def saveToCSV(people):
    data = []
    column_names = ["ID", "Name", "Age", "Is Student", "Field of Study", "Year of Study", "Avg Score"]
    for person in people:
        if person.is_student == "yes":
         data.append([person.id_number, person.name, person.age, person.is_student, person.field_of_study, person.year_of_study, person.score_avg])
        else:
         data.append([person.id_number, person.name, person.age, person.is_student])
        
    # Create DataFrame only once, out of the loop
    df = pd.DataFrame(data, columns=column_names)
    # Save the DataFrame to CSV once, out of the loop
    df.to_csv(csv_path, index=False)

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
    name = input("Please enter name: ")  
    age = getOnlyNumber("age: ")  
    id_number = getOnlyNumber("ID number: ")

    for person in people:
        if person.id_number == str(id_number):
            print("Error: This ID number already exists. Please enter another ID.")
            return
    
    is_student = input("Is this person a student? (yes or no): ")
    
    if is_student == "yes":
        field_of_study = input("Please enter the field of study: ")
        year_of_study = getOnlyNumber("Please enter the year of study: ")
        score_avg = float(input("Please enter the average score: "))
        person = Student(str(id_number), name, age, field_of_study, year_of_study, score_avg)
        person.is_student = "yes" 
    elif is_student == "no":
        person = Person(str(id_number), name, age)
        person.is_student = "no"
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return
    
    people.append(person) 
    age_avg_dict["age"] += age
    print("The last person was added successfully.")
    
def printPersonInfo(person):
    # Print the details of a person
    print("Name: " + person.name)
    print("Age: " + str(person.age))
    print("ID: " + person.id_number)


def checkEmpty(people):
    # Check if the people dictionary is empty
    if len(people) == 0:
        print("No data available.")
        return True
    return False

def findByID(people):
    id_number = getOnlyNumber("Please enter ID number: ")  
    for person in people:
        if person.id_number == str(id_number):
            person.printInfo() 
            return
    print("ID number not found.")

def printAgesAverage(age_avg_dict, people):
    # Calculate and print the average age of all people
    if checkEmpty(people):
        return
        # Calculate average age
    average_age = age_avg_dict["age"] / len(people)  
    print("Average age of all the people you entered: " + str(average_age))

def printAllPersons(people):
    for person in people:  
        person.printInfo() 
        
def printNames(people):
    # Print the names of all people
    if checkEmpty(people):
        return
    for index, person in enumerate(people):  # השתמש ב-people כאן
        print("Index: " + str(index) + " - Name: " + person.name) 

def printIDs(people):
    # Print the ID numbers of all people
    if checkEmpty(people):
        return
    for index, person in enumerate(people):
     print("Index: " + str(index) + " - ID: " + str(person.id_number))


def personByIndex(people):
    if checkEmpty(people):
        return
    index = getOnlyNumber("Enter index: ")  
    if index < 0 or index >= len(people):
        print("Error: Invalid index.")
        return
    printPersonInfo(people[index]) 

def printInvalidChoice():
    
    print("Invalid choice. Please enter a number between 1 and 8.")


def printMenu():
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
    

def runAll(): 
    # Main function to run the program
    age_avg_dict = {"age": 0}  
    people = [] 
    while True:  
        printMenu()
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