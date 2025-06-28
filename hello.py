# age1=17
# age2=22
# g1='male'
# g2='male'

# if age1>18 and age2>18:
#     print('both are adults')
#     if g1=='male' and g2=='female':
#         print('happy marriage')
#     if g2=='male' and g1=='female':
#         print('happy marriage')
#     if g1=='male' and g2=='male':
#         print('same gender')
#     if g2=='female' and g1=='female':
#         print('same gender')
# else:
#     print('minors')

# if age1<18 or age2 <18 or g1==g2:
#     print('not a happy marriage')
#     if age1<18 or age2<18:
#         print("minors")
#     if g1==g2:
#         print("same gender")
# else:
#     print('happy marriage')
# m=30
# if  m>=90 and m<100:
#     print("a")
# if m>=70 and m<90:
#     print("b")
# if m>=40 and m<70:
#     print("c")
# if m<40:
#     print("fail")

# if m>=90:
#     print("A")
# elif m>=70:
#     print("B")
# elif m >=40:
#     print("c")
# else:
#     print("fail")



# condition1=False
# condition2=False
# if condition1 and condition2:
#     print('both conditions are true') #block 1
# elif condition1:
#     print('condition2 is False and condition1 is True' ) #block2
# elif condition2:
#     print('condition1 is false and condition2 is True') #block3
# else:
#     print('both are false') #block4

# x=3
# y=2
# if x==0 and y==0:
#     print("origin")
# elif x==0:
#     print("y axis")
# elif y==0:
#     print("x axis")
# else:
#     print("not on axis or origin")
# a=float(input())
# b=float(input())
# c=float(input())
# def max_of_two(x,y):
#     return x if x>y else y

# m = max_of_two(a,c) if max_of_two(a,b)==a else max_of_two(b,c)

# if a>b:
#     m = max_of_two(a,c)
# else:
#     m = max_of_two(b,c)

# if a+b+c-m>m:
#     print("triangle is valid")
# else:
#     print("triangle is not valid")

# print("triangle is valid") if a+b+c-m>m else print("triangle is not valid")
# s="triangle is valid" if a+b+c-m>m else "triangle is not valid"
# print(s)
# i=5
# while i>=-5

# #print('+'*abs(i))
    
#     if i != 0:
#         print('+'*abs(i))



#     i=i-1
    # j=j+1
# i=1

# while i<=5:
#     print('+'*i)
#     i=i+1
# a=int(input())
# i=a
# while i>=-a:
#     print("*"," "*abs(i),"*" ,sep="")
#     i=i-1

# for i in range(a,-a-1,-1):
#     # print("*"," "*abs(i),"*" ,sep="")
#     print(i)

 
# for i in range(5,0,-1):
#     print("+"*(i-1)," ","-"*(5-i),sep="")

# a=int(input())
# rn=0
# while a!=0:
#     # print(a%10)
#     ld=a%10
#     rn=rn*10+ld
#     a=a//10
#     print(rn)