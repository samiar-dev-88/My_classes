with open(r"D:\CLASS\Python - 201\j3\1.jpeg", "rb") as file:
    data = file.read() #میخوانیم

with open("copy.jpg", "wb") as file:
    file.write(data) #مینویسیم