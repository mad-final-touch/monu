def exec(lst,i,j):
    c=lst[i]
    lst[i]=lst[j]
    lst[j]=c


lst=list(range(5,100))
l=len(lst)

print(lst)
i=len(lst)-2
while i>=0:
    # exec(lst,i,i+1)
    c=lst[i]
    lst[i]=lst[i+1]
    lst[i+1]=c
    i=i-1
print(lst)
