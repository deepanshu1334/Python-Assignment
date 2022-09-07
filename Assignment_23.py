#1

'''s1={"deepanshu","deep",1,33,42}
s2=iter(s1)
while True:
    try:
        print(next(s2),end=" ")
    except StopIteration:
        pass'''


#2 to print first odd natural no

'''def f1(n):
    x=1 
    while n:
        yield x
        x+=2
        n-=1

for e in f1(int(input())):
    print(e,end=" ")''' 

#3

'''def f1(n):
    x=2
    while n:
        yield x
        x+=2
        n-=1

for e in f1(int(input())):
    print(e)'''

#4

'''def f1(n):
    x=1
    while n:
        yield x*x
        x+=1    
        n-=1

for e in f1(int(input("enter the number"))):
    print(e)       '''

#5
def f1(n):
    a=0,b=1
    while n:



    
   