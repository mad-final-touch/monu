lst_app=[True]*7
lst_app[4]=False

while True:
    i=0
    while i<=6:
        if lst_app[i]==True:
            print(i+9,'erl app')
            break
        i=i+1
    if i!=7:

        while True: 
            slot=int(input("enter your prefrence"))
            i=slot-9
            if lst_app[i]==True:
                print('booked sucessfully')
                lst_app[i]=False
                break
            else:
                print('try again')
    else:
        print('all slot are booked')
        break