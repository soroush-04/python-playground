import json

json_string = '{"name": "Alice", "age": 25, "courses": ["math", "science"]}'
data = json.loads(json_string)

print(data)
print(data['name'])


with open('data.json', 'r') as file:
    data2 = json.load(file)

print(data2)

data3 = {
    "name": "Joe",
    "age": 25,
    "courses": ["math", "science"]
}
json_string = json.dumps(data3, indent=4)
print(json_string)

with open('data3.json', 'w') as json_file:
    json.dump(data3, json_file, indent=2)

with open('data3.json', 'r') as file3:
    file3 = json.load(file3)
print(json.dumps(file3, indent=2))

#### nested json
import json

with open('students.json', 'r') as students:
    students_file = json.load(students)

print(json.dumps(students_file, indent=2))

bob_electives = students_file['students'][1]['courses']['electives']
print("Bob's Elective Courses:", bob_electives)

students_file['students'][0]['courses']['core'].append("Computer Science")

with open('students.json', 'w') as file:
    json.dump(students_file, file, indent=2)
    
####
with open('students.json', 'r') as file:
    data = json.load(file)

student_name = 'Bob'
bob_electives = None

for student in data['students']:
    if student['name'] == student_name:
        bob_electives = student['courses']['electives']
        break
    
if bob_electives:
    print("2. Bob's Elective Courses:", bob_electives)
else:
    print(f"{student_name} not found.")
    
#### 1 iterate users.json
# selected_users = []

# with open('users.json', 'r') as file:
#     data = json.load(file)

# for user, data in data.items():
#     if data['age'] == 20:
#         for course in data['courses']:
#             if course['name'] == 'Math':
#                 selected_users.append(data)
#                 break

# print("Users with age 20 and course 'Math':")
# for user in selected_users:
#     print(user['name'])

#### 2 iterate users.json
selected_users = []

with open('users.json', 'r') as file:
    data = json.load(file)

for user, data in data.items():
    if data['age'] == 20:
        for faculty, courses in data['courses'].items():
            for course in courses:
                if course['name'] == 'Math':
                    selected_users.append(data)
                    break
            if data in selected_users:
                break


print("Users with age 20 and course 'Math':")
for user in selected_users:
    print(user['name'])
    
##### iterate over dictionaries and lists
with open('nested.json', 'r') as file:
    data4: dict = json.load(file)

for user, user_info in data4.items():
    print(f"user: {user}")
    for key, value in user_info.items():
        if isinstance(value, list):
            print(f"  {key}:")
            for course in value:
                course_name = course['name']
                course_grade = course['grade']
                course_credits = course['credits']
                print(f"    Course: {course_name}, Grade: {course_grade}, Credits: {course_credits}")
                
                assignments = course.get('assignments', [])
                if assignments:
                    print(f"      Assignments:")
                    for assignment in assignments:
                        assignment_title = assignment['title']
                        assignment_due_date = assignment['due_date']
                        print(f"        - {assignment_title}, Due: {assignment_due_date}")
                else:
                    print("      No assignments.")
        else:
            print(f"  {key}: {value}")
    