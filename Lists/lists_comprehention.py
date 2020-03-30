#COMPREHENTION
single_digits = range(10)
cubes = [i**3 for i in single_digits]



#WHILE
students_age = [7, 8, 9, 11, 9, 8]
summation = 0
index = 0
while index < 4:
  summation += students_age[index] #slice
  index += 1

print(summation)



scores = {
  'mary': [19, 17, 18],
  'john': [15, 20, 16],
  'mark': [14, 19, 19],
}

for name in scores.keys():
  sum = 0
  for score in scores[name]:
    sum += score
  print("{}'s average is {:0.2f}".format(
    name, sum / 3
  ))
