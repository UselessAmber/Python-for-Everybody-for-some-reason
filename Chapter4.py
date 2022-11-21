import math
import random

#Exercise 1
for i in range(10):
    print(random.random())

#Exercise 2
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

#Exception has occurred: NameError | name 'repeat_lyrics' is not defined

#Exercise 3: Nothing changes.
#Exercise 4: D
#Exercise 5: D
#Exercise 6: 
def compute_pay(hour, rate):
    return (min([hour, 40]) + max([hour - 40, 0]) * 1.5) * rate

try:
    hour = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter a numeric input")
else:
    print(f"Pay: {compute_pay(hour, rate)}")

#Exercise 7:
def compute_grade(grade):
    output = "Bad score"
    try:
        grade = float(grade)
        if 0.0 <= grade and grade <= 1.0:
            output = 'F'
            if grade >= 0.6:
                output = 'D'
            if grade >= 0.7:
                output = 'C'
            if grade >= 0.8:
                output = 'B'
            if grade >= 0.9:
                output = 'A'
    except:
        pass
    return output

score = input("Enter score: ")
print(compute_grade(score))