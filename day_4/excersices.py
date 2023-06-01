print("Thirty" + " Days" + " Of" + " Python")

company = "Coding For All"
print(company)

print(len(company))

print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

word = company[6:]
print(word)

company.replace('Coding For All', 'python')

company = "Coding For All"

print(company.split(' '))

social = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(social.split(', '))

print(company[0])
print(company[-1])
print(company[10])

words = "Python For Everyone"
coding = "Coding For All"
print("".join(w[0] for w in words.split(' ')))
print("".join(w[0] for w in coding.split(' ')))