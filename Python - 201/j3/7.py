with open(r"D:\CLASS\Python - 201\j3\1.txt", "r", encoding="utf-8") as file:
    print(file.tell())
    print(file.read(5))
    file.seek(0)
    print(file.read(5))