def menu_app():
    """
        A simple digital food ordering menu...
    """
    total = 0
    price = 0

    while True:
        print("== MENU ==")
        print("1. Pizza : 30")
        print("2. Burger : 25")
        print("3. Chips : 10")
        print("4. Drinks : 5")

        choice = input("Order from menu: ")

        if choice == "1":
            price = 30
        elif choice == "2":
            price = 25
        elif choice == "3":
            price = 10
        elif choice == "4":
            price = 5
        else:
            print("Please enter a true number!")
            continue

        quantity = int(input("How many do you want? "))

        if 1 <= quantity <= 10:
            total += price * quantity
        else:
            print("Please enter from 1 to 10!")
            continue

        yes_no = input("Do you want to order again?(yes/no) ").lower()

        if yes_no == "no":
            if total > 50:
                print(total - 10)
            else:
                print(total)
            break
        elif yes_no == "yes":
            continue
        else:
            print("Please Enter yes or no!")
            
menu_app()