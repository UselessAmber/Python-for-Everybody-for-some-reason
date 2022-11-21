import math

def max(*args):
    output = args[0]
    for arg in args:
        if output < arg:
            output = arg
    return output

def min(*args):
    output = args[0]
    for arg in args:
        if output > arg:
            output = arg
    return output

#Exercise 1 and 2:
try:
    hour = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter a numeric input")
else:
    print(f"Pay: {min(hour, 40) * rate + max(hour - 40, 0) * rate * 1.5}")

#Exercise 3:
try:
    score = float(input("Enter score: "))
    if score < 0.0 or 1.0 < score:
        raise Exception("Bad score")
    output = 'F'
    if score >= 0.6:
        output = 'D'
    if score >= 0.7:
        output = 'C'
    if score >= 0.8:
        output = 'B'
    if score >= 0.9:
        output = 'A'
    print(output)
except:
    print("Bad score")