import json

with open('prac3.json', 'r') as file:
    data: dict = json.load(file)

####prac1: print each user's name and their age.
# for user, user_info in data.items():
#     print(f"{user}-> name: {user_info['name']}, age: {user_info['age']}")
    
####prac2: print each user's name, age, and city.
# for user, user_info in data.items():
#     city = user_info['details']['city']
#     print(f"{user} -> name: {user_info['name']}, age: {user_info['age']}, city: {city}")

####prac3: print each user's name, age, and the names of their courses along with their grades
for user, user_info in data.items():
    print(f"{user}:")
    print(f"  {user_info['name']} \n  {user_info['age']}\n  'courses':")
    for course in user_info['courses']:
        print(f"    {course['name']}")
        print(f"    {course['grade']}")