from module1 import *
from module2 import *

d_assign = []

count1 = 0


def dish_assign():
    global count1
    dish_id = input("Enter ID of Dish you want to assign to customer: ")
    if dish_id in Dish:
        customer_id = input("Enter ID of customer whom you want to assign that Dish: ")
        if customer_id in customer:
            count1 = count1 + 1
            d_assign.append(dish_id)
            d_assign.append(customer_id)
            print("Dish Assigned to customer")
        else:
            print("Customer ID does not exist")
            print("Please try again")
    else:
        print("Dish ID does not exist")
        print("Please try again")


def view_dishes_assigned():
    print()
    if count1 > 0:
        print("Dishes assigned")
        print("-------------------------------------------")
        for i in range(0, len(d_assign), 2):
            print("Dish ID: ", d_assign[i], " Assigned to ", "\tCustomer ID:", d_assign[i+1])
    else:
        print("No dish has been assigned to customer yet, Please assign first then you can view.")
