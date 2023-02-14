good_credit = False
x = 10/100*1000000
y = 20/100*1000000
if good_credit:
    print("You need to put down 10%")
    print("$ ",x)
else:
    print("You need to put 20%")
    print("$ ",y)

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}") #f is the format specifier