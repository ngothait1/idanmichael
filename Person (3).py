class Person:
    def __init__(self, id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age
    
    def getAge(self):
     return self.age

    def getInfo(self):
        return "Name: " + self.name + ", Age: " + str(self.age) + ", ID: " + self.id_number
    
    def printInfo(self):
        print(self.getInfo())




