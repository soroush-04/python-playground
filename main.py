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