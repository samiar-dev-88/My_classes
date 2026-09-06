score = int(input())

if 0 <= score <= 20:
    if score == 20:
        print("Perfect!")
    elif score > 18:
        print("Nice!")
    elif score > 15:
        print("Very Good!")
    elif score > 10:
        print("Good!")
    elif score > 1:
        print("Bad!")
    else:
        print("Error!")
else:
    print("Enter 0 to 20 please!")
    