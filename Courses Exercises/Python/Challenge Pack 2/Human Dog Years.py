# Function that returns a message featuring a dog name and it's equivalent human years

def dog_years(name, age):
    age_in_human_years = age*7
    return f"{name} is {age_in_human_years} years old in human years."

print(dog_years('Landon', 3))
print(dog_years('Red Bean', 6))
print(dog_years('Cooper', 2))