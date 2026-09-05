import json

with open(r"D:\CLASS\Python - 201\j3\1.txt", "r", encoding="utf-8") as file:
    user = json.load(file)

    print(user["name"])
    print(user["skills"])