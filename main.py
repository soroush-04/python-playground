import json

json_string = '{"name": "Alice", "age": 25, "courses": ["math", "science"]}'
data = json.loads(json_string)

print(data)
print(data['name'])
