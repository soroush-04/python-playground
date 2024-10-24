import json

with open('prac7.json', 'r') as file:
    data: dict = json.load(file)

####prac1: print each user's name and their age.
# for user, user_info in data.items():
#     print(f"{user}-> name: {user_info['name']}, age: {user_info['age']}")
    
####prac2: print each user's name, age, and city.
# for user, user_info in data.items():
#     city = user_info['details']['city']
#     print(f"{user} -> name: {user_info['name']}, age: {user_info['age']}, city: {city}")

####prac3: print each user's name, age, and the names of their courses along with their grades
# for user, user_info in data.items():
#     print(f"{user}:")
#     print(f"  {user_info['name']} \n  {user_info['age']}\n  'courses':")
#     for course in user_info['courses']:
#         print(f"    {course['name']}")
#         print(f"    {course['grade']}")

####prac4: print the names of users who have received a grade of "A" in any of their courses.
# answer = []

# for user, user_info in data.items():
#     for course in user_info['courses']:
#         if course['grade'] == 'A':
#             answer.append(user_info['name'])

# print(answer)

####prac5: Print each user's name along with their courses and grades.
# for user, user_info in data.items():
#     print(f"user: {user_info['name']}")
#     for course in user_info['courses']:
#         print(f"  course: {course['name']}, grade: {course['grade']}")

####prac6: print the total credits for each user based on the courses they are taking.
# for user, user_info in data.items():
#     print(f"user: {user_info['name']}")
#     credits = 0
#     for course in user_info['courses']:
#         credits += course['credits']
#     print(f"  credits: {credits}")

####prac7: Print the name of each user.
# For each user, print the names of their courses, their grades, and the titles of assignments along with their due dates.
# Calculate the total number of assignments each user has across all courses.
for user, user_info in data.items():
    print(user_info['name'])
    counter = 0
    for course in user_info['courses']:
        print(f"  {course['name']}, {course['grade']}")
        for assignment in course['assignments']:
            print(f"    {assignment['title']}, {assignment['due_date']}")
            counter += 1
    print(f"total assignments for {user_info['name']}: {counter}")