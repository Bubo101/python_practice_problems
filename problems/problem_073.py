# Write a class that meets these requirements.
#
# Name:       Student
#
# Required state:
#    * name, a string
#
# Behavior:
#    * add_score(score)   # Adds a score to their list of scores
#    * get_average()      # Gets the average of the student's scores
#
# Example:
#    student = Student("Malik")
#
#    print(student.get_average())    # Prints None
#    student.add_score(80)
#    print(student.get_average())    # Prints 80
#    student.add_score(90)
#    student.add_score(82)
#    print(student.get_average())    # Prints 84
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

class Student:
    def __init__(self, name):
        self.name = name
        self.score_list = []

    def add_score(self, score):
        self.score_list.append(score)
    
    def get_average(self):
        sum = 0
        for score in self.score_list:
            sum += score
        return sum / len(self.score_list)


stu = Student ("Boden")
stu.add_score(80)
stu.add_score(85)
stu.add_score(95)

print(stu.get_average())
