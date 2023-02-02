Dish = []

count = 0


def add_dish():
    global count
    confirm = "y"
    while confirm == "y":
        count = count+1
        Dish.append(input("Enter Dish name : "))
        Dish.append(input("Enter Dish ID : "))
        Dish.append(input("Enter Dish type : "))
        Dish.append(eval(input("Enter Dish Price : ")))
        confirm = input("Enter 'y' if you want to continue to add another dish : ")


def search_dish():
    if count > 0:
        dish_1_id = input("Please enter ID of dish you want to search: ")
        for i in range(0, len(Dish), 4):
            if dish_1_id == Dish[i+1]:
                print("Name\t\tID\t\t\tType\t\tPrice")
                print("-------------------------------------------")
                print(Dish[i], "\t\t", Dish[i + 1], "\t\t", Dish[i + 2], "\t\t", Dish[i + 3])
            if dish_1_id not in Dish:
                print("Dish ID not found")
                break
    else:
        print("No record has been added yet, Add record first then you can search for it")


def update_dish():
    if count > 0:
        dish_1_id = input("Please enter ID of dish to update it: ")
        for i in range(0, len(Dish), 4):
            if dish_1_id == Dish[i+1]:
                Dish[i+3] = eval(input("update price of dish :"))
                print("Price updated")
            if dish_1_id not in Dish:
                print("Dish ID not found")
                break
    else:
        print("No record has been added yet, Add record first then you can update it")


def views():
    if count > 0:
        print("Name\t\t\tID\t\t\tType\t\tPrice")
        print("-------------------------------------------")
        for i in range(0, len(Dish), 4):
            print(Dish[i], "\t\t", Dish[i + 1], "\t\t", Dish[i + 2], "\t\t", Dish[i + 3])
    else:
        print("No Dish record has been Added yet, Please add first then you can view")
