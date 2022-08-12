def calvat(price):
    result = price + price*7/100
    return result
totalprice = int(input("enter price:"))
print(calvat(totalprice))