username = input("Customer ID   : ")
password = input("Password      : ")
if username == "admin" and password == "1234" :
    print("*************************")
    print("***WELCOME TO MY STORE***")
    print("*************************")
    print("You can select product from list by select number :")
    print("No.  Product     Price")
    print("(1)  Pen         10  THB")
    print("(2)  Pencil      5   THB")
    print("(3)  Eraser      2   THB")
    CustomerSelectNo = int(input("Please select No. of Product :"))
    if CustomerSelectNo     == 1:
        product =   "Pen"
        price   =   10
        CustomerSelectQty = int(input("How many you want :"))
        print("Price :", product, price, "THB", "X", CustomerSelectQty, "Total", price * CustomerSelectQty, "THB")
    elif CustomerSelectNo   == 2:
        product = "Pencil"
        price = 5
        CustomerSelectQty = int(input("How many you want :"))
        print("Price :", product, price, "THB", "X", CustomerSelectQty, "Total", price * CustomerSelectQty, "THB")
    elif CustomerSelectNo   == 3:
        product = "Eraser"
        price = 2
        CustomerSelectQty = int(input("How many you want :"))
        print("Price :", product, price, "THB", "X", CustomerSelectQty, "Total", price * CustomerSelectQty, "THB")
    else:
        print("You select wrong. See you again. Thank you :)")
else:
    print("Your customer id is incorrect")