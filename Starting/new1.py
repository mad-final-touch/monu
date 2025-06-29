ab=300
cash=400
while True:
    productprice=int(input("Enter product price"))
    payment_type=input("Enter u for UPI and c for cash")
    if payment_type=='u':
        print(ab+productprice)
        ab=ab+productprice
    else:
        print(cash+productprice)
        cash=cash+productprice