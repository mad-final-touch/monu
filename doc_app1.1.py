lst_app=[True]*7
lst_app[4]=False

while True in lst_app:
    print(lst_app.index(True)+9, 'earlies appointment')
    while True:
        slot=int(input("enter your prefrence"))
        i=slot-9
        if  lst_app[i] is True:
            print('Booked Successfuly')
            lst_app[i]=False
            break
        else:
            print('try again')
print("all slots are booked")