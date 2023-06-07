
car = list()

another_car = []

print(car)
print(another_car)

brand_car = ['PROTON', 'PRODUA', 'HONDA', 'NISSAN', 'TOYOTA', 'MAZDA']
print(brand_car)
print(len(brand_car))

print(brand_car[0]) # first item
print(brand_car[6-1]) # last item

mixed_data_types = [
    "Devxpi",
    25,
    185,
    "single",
    "Malaysia"
]

print(mixed_data_types)

it_companies = [
    "Facebook", "GOOGLE", "MICROSOFT", "APPLE", "IBM", "ORACLE", "AMAZON"
]
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[len(it_companies)-1])

it_companies[0] = "yahoo"
print(it_companies)

it_companies.append("REDHAT")
print(it_companies)
print(it_companies[0].capitalize())

print("#; ".join(it_companies))

print("GOOGLE" in it_companies)
it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)