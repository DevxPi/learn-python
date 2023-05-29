# Day 2:30 Days of python programming

first_name = "DevPi"
last_name = "Pi"
full_name = "DevxPi Pi"
country = "Malaysia"
city = "Some City"
age = 24
year = 2023
is_married = False
is_true = True
is_light_on = False

cat_name, cat_color = 'Oyen', 'orange'

# Exercises: level 2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(cat_name))
print(type(cat_color))

print(len(first_name)) # 5

print(len(first_name) == len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
print(total)

diff = num_one - num_two
print(diff)

product = num_one * num_two
print(product)

division = num_one / num_two
print(division)

remainder = num_one % num_two
print(remainder)

exp = num_one ** num_two
print(exp)

floor_division = num_one // num_two
print(floor_division)

r_cicle = 30 # radius of circle = 30meter

pi = 3.14159

area_of_circle = pi * r_cicle * r_cicle
print(area_of_circle)

circum_of_circle = 2 * pi * r_cicle
print(circum_of_circle)

area = input("Please insert value of radius: ")
area = int(area) #casting the string to int
the_area = pi * area * area
print(the_area)


first_name = input("Your first name: ")
last_name = input("Your last name: ")
country = input("Your country: ")
age = input("Your age ")

print(help('keywords'))