import json

json_string = '{"name": "Alice", "age": 25, "courses": ["math", "science"]}'
data = json.loads(json_string)

print(data)
print(data['name'])


with open('data.json', 'r') as file:
    data2 = json.load(file)

print(data2)