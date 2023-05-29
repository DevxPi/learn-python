# Exercises - Day 3

age = 24
height = 1.85 # 1.85 mtrs
complex_number = 3 + 3j

# prompts user to enter base and height of triangle
base = input("Enter base: ")
height = input("Enter height: ")
area = 0.5 * int(base) * int(height)
print(f"The area of the triangle is {int(area)}")

print("\n")

# prompts user to enter side a, side b and side c of the triangle
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")

perimeter = int(side_a) + int(side_b) + int(side_c)
print(f"The perimeter of the triangle is {perimeter}")

print("\n")

# prompts user to enter length and width of a rectangle
length = input("Enter a length: ")
width = input("Enter a width: ")
area = int(length) * int(width)
perimeter = 2 * (int(length) + int(width))
print(f"The area of rectangle is {area}")
print(f"The perimeter of rectangle is {perimeter}")

print("\n")

# prompts user to enter the radius of circle
radius = input("Please enter a radius: ")
pi = 3.14
area = pi * int(radius) * int(radius)
circumferences = 2 * pi * int(radius)
print(f"The area of circle is {area}")
print(f"The circumferences of circle is {circumferences}")

print("\n")

# Equation = y = 2x - 2
# An equation of the form y=mx+b, where m is the slope and b is the y-intercept.

# slope(m)
slope = 2

# x-intercept
x_intercept = 2 / slope

# y-intercept
y_intercept = -2

print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

print("\n")

programming_language = 'python'
animal = 'dragon'

print(len(programming_language))
print(len(animal))
print(programming_language == animal)
print(programming_language > animal)

print('on' in programming_language)
print('on' in animal)

phase = 'I hope this course is not full of jargon'
print('jargon' in phase)

length_word = len(programming_language)
float(length_word)
print(type(length_word))
str(length_word)
print(type(length_word))

print("\n")

hours = input("Enter hours: ")
rate_per_hour = input("Enter rate per hour: ")
weekly_earnings = int(hours)  *int(rate_per_hour)
print(f"Your weekly earnings is {weekly_earnings}")

print("\n")

years_lived = input("Enter number of years you have lived: ")
seconds_per_minutes = 60
seconds_per_hour = 60 * seconds_per_minutes
seconds_per_day = 24 * seconds_per_hour
seconds_per_year = 365 * seconds_per_day

seconds = int(years_lived) * seconds_per_year
print(f"You have lived for {seconds} seconds.")

print("\n")

for i in range(1, 6):
    print(i, 1, i**1, i**2, i**3)