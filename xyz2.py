
lst=list(range(1,101))
i=97
while i>=0:
    a=lst[i+2]
    b=lst[i]
    c=a
    lst[i+2]=b
    lst[i]=c
    i=i-1
    print(lst)
print(lst)