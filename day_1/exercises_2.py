# Exercise: Level 2

a = 3 
b = 4

print(
    a + b, a - b, a * b, a % b, a / b, a ** b, a // b
) # 7 -1 12 3 0.75 81 0

name = "DevPi"
family_name = "Pi"
country = "Malaysia"
string_phase = "I am enjoying 30 days of python"

print(
    f"I'm {name}, and my family name is {family_name}.\n"
    f"I live at {country} and {string_phase}"
)

a_input = (
    10,
    9.8,
    3.14,
    4-4j,
    ['Asabeneh', 'Python', 'Finland'],
    name,
    family_name,
    country
)

for i in a_input:
    """ for i in a_input: This loop iterates directly over the elements in a_input.
        In each iteration, the variable i is assigned the value of the current element
        in a_input. For example, in the first iteration, i would be assigned the value 10,
        in the second iteration, i would be assigned the value 9.8, and so on.
        This form of loop is suitable when you want to directly access and work
        with the elements of the tuple."""
    print(type(i))

# Exercise: Level 3

b_input = (
    100,
    4.4,
    3-4j,
    True,
    "Github",
    ["A", "B", "C"],
    (1, 2 , 3),
    {'Apple', 'Banana', 'Cucumber'},
    {
        'name': 'Devxpi',
        'country': 'Malaysia'
    }
)

for item in b_input:
    print(f"\"{item}\" type is -> {type(item)}")