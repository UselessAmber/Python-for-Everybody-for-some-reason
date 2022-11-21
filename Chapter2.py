import math

#Exercise 1:
print(5)
x = 5
print(x + 1)

#Exercise 2:
name = input("Enter your name: ")
print(f"Hello {name}")

#Exercise 3:
hour = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
print(f"Pay: {hour * rate}")

#Exercise 4:
width = 17
height = 12.0
print(f"{width // 2} - Type: {type(width // 2)}\n{width / 2.0} - Type: {type(width / 2.0)}\n{height / 3} - Type: {type(height / 3)}\n{1 + 2 * 5} - Type: {type(1 + 2 * 5)}")

#Exercise 5:
celcius = float(input("Enter the temperature (in Celcius): "))
farenheit = celcius * 9 / 5 + 32
print(f"Temperature in Farenheit is: {farenheit}*F")