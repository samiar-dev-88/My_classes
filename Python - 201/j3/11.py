import json

user = {
    "name": "Ali",
    "age": 14,
    "skills": ["Python", "HTML", "CSS"]
}

with open(r"D:\CLASS\Python - 201\j3\1.txt", "w", encoding="utf-8") as file:
    json.dump(user, file)