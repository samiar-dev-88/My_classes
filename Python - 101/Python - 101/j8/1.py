mojodi = 200

print("1.Mojodi")
print("2.Bardasht")
print("3.Variz")
print("4.Payan")

user = input("Enter a number: ")

while user != "4":

    if user == "1":
        print("Your Mojodi:",mojodi)

    elif user == "2":
        print("Your Mojodi:",mojodi)
        user2 = int(input("Enter a number: "))
        print("Your Mojodi:",mojodi - user2)
        mojodi -= user2

    elif user == "3":
        print("Your Mojodi:",mojodi)
        user2 = int(input("Enter a number: "))
        print("Your Mojodi:",mojodi + user2)
        mojodi += user2
        

    print("1.Mojodi")
    print("2.Bardasht")
    print("3.Variz")
    print("4.Payan")

    user = input("Enter a number: ")