# species = "Cat"
# age = 6

# if species == "Dog" and age < 2:
#     food = "Puppy Food"
# elif species == "Cat" and age > 5:
#     food = "Senior Cat Food"
# else:
#     food = "Regular Pet Food"

# print(food)

# --------------------------------------

# Areas for Improvement
# 1. Incomplete Coverage
# Your code only handles two specific cases. What about:

# Dogs aged 2+ years (adult dog food)
# Cats under 5 years (kitten food for <1 year, adult cat food for 1-5 years)
# Senior dogs (typically 7+ years)

# 2. Case Sensitivity
# species == "Dog" won't work if someone enters "dog" or "DOG"
# 3. Limited Flexibility
# The values are hardcoded rather than accepting user input

species = "Cat"
age = 5

if species == "Dog":
    if age < 2:
        food = "Puppy Food"
    elif age < 7:
        food = "Adult Dog Food"
    else: 
        food = "Senior Dog Food"
elif species == "Cat":
    if age < 1:
        food = "Kitten Food"
    elif age <= 5:
        food = "Adult Cat Food"
    else:
        food = "Senior Cat Food"
else:
    food = "Unknown species - please consult a vet"

print(f"Recommended food: {food}")