from Person import Person
class Student(Person):
    def __init__(self, id_number, name, age, field_of_study, year_of_study, score_avg):
        super().__init__(id_number, name, age)
        self.is_student = "yes"
        self.field_of_study = field_of_study
        self.year_of_study = year_of_study
        self.score_avg = score_avg

    def getFieldOfStudy(self):
        return self.field_of_study

    def getYearOfStudy(self):
        return self.year_of_study

    def getScoreAvg(self):
        return self.score_avg

    def printStudent(self):
        self.printInfo()
        print("The field of study is " + str(self.getFieldOfStudy()) + 
              ", the year of study is " + str(self.getYearOfStudy()) + 
              ", the average score is " + str(self.getScoreAvg()))