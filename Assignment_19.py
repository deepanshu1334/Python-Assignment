#1 to create a simple function which print mysirg
 
'''def f1():
    print("mysirg") 
print()

f1()'''

#2

'''def f1(a,b):
    c=a+b
    print("the sum of a and b is ",c)

a=int(input("enter the number"))
b=int(input("enter the number"))
f1(a,b)'''

#3

'''def f1(*t):
    A=sum(t)/len(t)
    return A

print("the average of the number is",f1(2,4,5,6,6)) '''

#5

'''def f1(d1):
    for e in d1:
        print(d1)

f1([2,3,4,5,6])

def f2(d1):
    print(d1)
print()
f2([2,4,5,6])'''

#6

'''def f1(d1):
    print(max(d1))
    print()

f1([3,5,6,7])    '''

#7

'''def f1(d1):
    print(sum(d1))
print()

f1([2,6,2,4,5,67,5])'''

#8

'''def f1(d1):
    t=1
    for e in d1:
        t=t*e
        print(t)

print()        

f1([2,4,1,3,4,5])'''

#10

'''def f1(n):
    if n%2==0:
        print("no is even")
    else:
        print("no is odd")    

n=int(input("enter the number"))
f1(n)'''


#9

def f1(r1):
    for e in r1:
        if e==1:
            print("no in the given range")
        elif e==2: 
            print("no in the range")
        elif e==3:
            print("no in the given range")
        elif e==4:
            print("no in the given range")    
f1(range(1,10,1))                