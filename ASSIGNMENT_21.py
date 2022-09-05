#1 write a recrusive function to print n natural nu

'''def f1(n):
    if n>0:
        (f1(n-1)) #f1 ko call kar liye 9 tak aur print kara diya 10
        print(n)

m=int(input("Enter the number"))
f1(m)'''        

#2 to print first n natural no in reverse order

'''def f1(n):
    if n>0:
        print(n)
        f1(n-1)

m=int(input("enter the number"))
f1(m)'''

#3 to print even natural no

'''def f1(n):
    if n>0:
        f1(n-2)
        print(n)

m=int(input("Enter the number"))
f1(m)'''


#6 to print even natural no in reverse order

'''def f1(n):
    if n>0:
        print(n)
        f1(n-2)
m=int(input("enter the number"))
f1(m)       '''

#4 to print first n odd natural no

'''def f1(n):
    if n>0:
        f1(n-1)  #f1(n-2)
        print((2*n)-1)

m=int(input("enter the number"))
f1(m)'''

#5  to print odd natural no in reverse order

'''def f1(n):
    if n>0:
        print((2*n)-1)
        f1(n-1)

m=int(input("enter the number"))        
f1(m)'''

#7 to print square of first natural no

'''def f1(n):
    if n>0:
        f1(n-1)
        print(n*n)

m=int(input("enter the number"))
f1(m)        '''

#8

'''def f1(n):
    if n>0:
        f1(n-1)
        print(n*n*n)

m=int(input("enter the number"))
f1(m)'''

#9

'''def f1(n):
    i=1

    while i<=n: 
        f1(n-1)
        print(n*i)
        i+=1

print()        

m=int(input("enter the number"))
i=1
f1(m)'''

#10

'''def f1(n):
    if n>0:
        print(n)
        f1(n-1)

m=int(input("enter the number"))
f1(m)'''