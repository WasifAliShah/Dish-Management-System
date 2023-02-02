from module1 import *
from module2 import *
from module3 import *

confirm = "y"
while confirm == "y":
    print("Enter your choice")
    check = eval(input("(1) Dish Management  (2) Customer Management  (3) Dish Registration (4) Exit: "))
    if check == 1:
        print()
        print("You have Selected Dish Management")
        confirm = "y"
        while confirm == "y":
            print("Enter your choice")
            choice = eval(input("(1) To View Dishes. (2) To search  (3) To update (4) To Add: "))
            if choice == 1:
                views()
            elif choice == 2:
                search_dish()
            elif choice == 3:
                update_dish()
            elif choice == 4:
                add_dish()
            else:
                print("Invalid Input !, Try Again")
            print()
            confirm = input("If you want to view Dish Management menu again. Enter 'y': ")
    elif check == 2:
        print()
        print("You have Selected Customer Management")
        confirm = "y"
        while confirm == "y":
            print("Enter your choice")
            choice = eval(input("(1) To View Customers. (2) To search  (3) To update (4) To Add: "))
            if choice == 1:
                view()
            elif choice == 2:
                search_customer()
            elif choice == 3:
                update_customer()
            elif choice == 4:
                add_customer()
            else:
                print("Invalid Input!, Try again")
            print()
            confirm = input("If you want to view Customer Management menu again. Enter 'y': ")
    elif check == 3:
        print()
        print("You have Selected Dish Registration")
        confirm = "y"
        while confirm == "y":
            print("Enter your choice")
            choice = eval(input("(1) To Assign Dish.  (2) To View Dishes assigned: "))
            if choice == 1:
                dish_assign()
            elif choice == 2:
                view_dishes_assigned()
            else:
                print("Invalid Input, Try again")
            print()
            confirm = input("If you want to view Dish Registration menu again. Enter 'y': ")
    elif check == 4:
        print("Programme Exited")
        break
    else:
        print("Invalid choice")
    print()
    confirm = "y"
