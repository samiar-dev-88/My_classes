import csv

with open(r"D:\CLASS\Python - 201\j5\1.csv", "r") as file:
    data = csv.reader(file)

    for row in data:
        print(row)
        
with open(r"D:\CLASS\Python - 201\j5\1.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age", "score"])
    writer.writerow(["Ali", 15, 18])
    writer.writerow(["Sara", 16, 20])