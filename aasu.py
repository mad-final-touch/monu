lst= list(chr(x) for x in range(ord('a'),ord('z')+1))
print(lst)

print("\033[32mThis text is green.\033[0m")
def print_colored_list(lst,ic,ij):
    strr=""
    i=0
    while i<len(lst):
        if i<ic:
            strr+=lst[i]+" "
        elif i==ic:
            strr+="\033[91m" + lst[ic] + "\033[0m"+" "
        elif i<ij:
            strr+=lst[i]+" "
        elif i==ij:
            strr+="\033[32m" +lst[ij]+ "\033[0m"+" "
        else:
            strr+=lst[i]+" "
        i+=1
    print(strr)

i=23
while i>=0:
    print_colored_list(lst,i,i+2)
    a=lst[i]
    b=lst[i+2]
    c=a
    lst[i]=b
    lst[i+2]=c
    i=i-1
    
print(lst)

lst=list(range(1,100))
i=95
while i>0:
    a=lst[i]
    b=lst[i+2]
    c=a
    lst[i]=b
    lst[i+2]=c
    i=i-1
    print(lst)
