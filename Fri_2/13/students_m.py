class Student:
    def __init__(self, id, name, score = 0):
        self.id = id
        self.name = name
        self.score = score
    def getID(self):
        return self.id
    def getName(self):
        return self.name
    def getScore(self):
        return self.score
    def setScore(self,score):
        self.score = score
class CalcScore:
    def __init__(self):
        self.students = []
    def addStudent(self, student):
        self.students.append(student)
    def ave(self):
        total = 0
        for st in self.students:
            total += st.getScore()
        ave = total / len(self.students)
        return ave