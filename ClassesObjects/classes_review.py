class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = {}
    
  def set_attendance(self, date, value):
    self.attendance[date] = value
   
  def get_attendance(self, date):
    if date not in self.attendance:
      return None
    return self.attendance[date]
    
  def add_grade(self, grade):
    if type(grade) == Grade:
      (self.grades).append(grade)

  def get_average(self):
    sum = 0
    for grade in self.grades:
      sum += grade.score
      return sum/len(self.grades)

roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(self):
    return Grade.score > minimum_passing

pieter.add_grade(Grade(100))
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(40))
print(pieter.get_average())
pieter.set_attendance('2020-04-13', True)
print(pieter.get_attendance('2020-04-13'))
print(pieter.get_attendance('2020-04-12'))


#Write a Grade method .is_passing() that returns whether a Grade has a passing .score.
#Write a Student method get_average() that returns the student’s average score.
#Add an instance variable to Student that is a dictionary called .attendance,
#with dates as keys and booleans as values that indicate whether the student attended
#school that day.