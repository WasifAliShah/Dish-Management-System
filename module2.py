customer = []

count3 = 0


def add_customer():
    global count3
    confirm = "y"
    while confirm == "y":
        count3 = count3+1
        customer.append(input("Enter Customer Name: "))
        customer.append(input("Enter Customer ID: "))
        customer.append(input("Enter Customer CNIC: "))
        customer.append(input("Enter Customer contact no: "))
        confirm = input("Enter 'y' if you want to continue to add another Customer : ")


def search_customer():
    if count3 > 0:
        customer_1_id = input("Please enter ID of customer you want to search: ")
        for i in range(0, len(customer), 4):
            if customer_1_id == customer[i+1]:
                print("Name\t\tID\t\t\tCNIC\t\tContact no")
                print("------------------------------------------------")
                print(customer[i], "\t\t", customer[i + 1], "\t\t", customer[i + 2], "\t\t", customer[i + 3])
            if customer_1_id not in customer:
                print("Customer ID not found")
                break
    else:
        print("No record has been added yet, Add record first then you can search for it")


def update_customer():
    if count3 > 0:
        customer_1_id = input("Please enter ID of customer to update his record : ")
        for i in range(0, len(customer), 4):
            if customer[i+1] == customer_1_id:
                customer[i+3] = input("update contact number of customer :")
                print("Contact number updated")
            if customer_1_id not in customer:
                print("Customer ID not found")
                break
    else:
        print("No record has been added yet, Add record first then you can update it")


def view():
    if count3 > 0:
        print("Name\t\t\tID\t\t\tCNIC\t\tContact no")
        print("------------------------------------------------")
        for i in range(0, len(customer), 4):
            print(customer[i], "\t\t", customer[i + 1], "\t\t", customer[i + 2], "\t\t", customer[i + 3])
    else:
        print("No Customer record has been Added yet, Please add first then you can view")
