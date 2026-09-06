user_1 = ""
user_2 = ""

while (user_1 != "r" and user_1 != "p" and user_1 != "s") or (user_2 != "r" and user_2 != "p" and user_2 != "s"):
    user_1 = input("User 1 (r, p, s): ")
    user_2 = input("User 2 (r, p, s): ")

    if (user_1 != "r" and user_1 != "p" and user_1 != "s") or (user_2 != "r" and user_2 != "p" and user_2 != "s"):
        print("Enter only (r, p, s)")

if user_1 == user_2:
    print("Draw!")

elif user_1 == "r" and user_2 == "s":
    print("User 1 is winner!")

elif user_1 == "s" and user_2 == "p":
    print("User 1 is winner!")

elif user_1 == "p" and user_2 == "r":
    print("User 1 is winner!")

elif user_2 == "r" and user_1 == "s":
    print("User 2 is winner!")

elif user_2 == "s" and user_1 == "p":
    print("User 2 is winner!")

elif user_2 == "p" and user_1 == "r":
    print("User 2 is winner!")