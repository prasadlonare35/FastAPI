import json

dict = {"name":"Prasad", "age":21, "skills": ["Python", "Java", "SQL"]}

print(dict)

str = json.dumps(dict)     # object to json
print(str)

print(dict["age"])
print(str[2])

p_dict = json.loads(str)    # json to object

print(p_dict)
print(p_dict["name"])


with open('patients.json', 'r') as f:
    data = json.load(f)
print(data)

with open('patients.json', 'a') as f:
    json.dump(dict,f)
# print(data)
