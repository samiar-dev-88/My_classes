speed = int(input("Enter speed: "))

if speed < 300:
    if speed > 80:
        print(speed - 80)
    else:
        print("Your speed is ok")
else:
    print("You are so high")