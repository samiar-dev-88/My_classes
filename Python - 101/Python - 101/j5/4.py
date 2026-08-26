num = 2 #numer
user = int(input("Enter a number 1 to 10: ")) #user value

if user < 10: #if user input true
    if user == num: #if user guess true
        print("True") #print true
    else: #if user guess false
        print("False") #print false
else: #if user input more than 10
    print("Enter number 1 to 10!!")