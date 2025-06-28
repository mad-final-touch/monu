total_cash=0
total_ballance=0
while True:
    print("Enter the price of product sold")
    product_price=int(input())
    print("Enter upi payment")
    upi_recieved=int(input())
    cash_recieved=product_price-upi_recieved
    total_cash=total_cash+cash_recieved
    total_ballance=total_ballance+upi_recieved
    print(total_cash)
    print(total_ballance)
