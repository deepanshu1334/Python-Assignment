#reverse a number
'''n=int(input("enter the number"))
i=1
r=0
while i<=n:
    m=n%10
    r=r*10+m
    n=n//10
print("the reverse of a number is ",r)'''

#to check wheather a given no is prime or not

'''n=int(input("enter the number"))
i=1
c=0
while i<=n:
    if n%i==0:
        c+=1
    i+=1
if(c==2):
    print("no is prime",n)    
else:
    print("no is not prime")'''

#to print all prime number between 100

'''n=int(input("enter the number"))
i=1
c=0
while i<=n:
    if n%i==0:
        c+=1
    i+=1

if(c==2):
    print("the prime no is",i) '''

#prime no betweem two given no
'''n=int(input("enter the number"))
m=int(input("enter the number"))
i=1
c=0
for e in range(n,m):
    if n%e==0:
        c+=1

if(c==2):
    print(e)'''

#program practice::

'''x=input("enter the name")
for e in x:
    print(e)'''

#python practice
#agar range ma ek value denge toh woh end value mane jaege , begining value 0 hogi aur step size 1 hoga
'''
for e in range(10):
    print(e+1) '''    
#range function ko call karke range object banta hai

#2

'''for e in range(1,10,1):#beginning value zero end value 10 and step size 1 hai
    print(2*e)'''

#3

'''n=int(input("enter the number"))
for e in range(n):
    if e%5==0:
        break

print("no is divisible by 5",e)'''

#4
'''x=(input("enter your name"))

for e in x:#one by one hum element ko access kar paenge
    print(e,end=" ")'''

#5
'''n=int(input("Enter the number"))
r1=range(n)
sum=0
for e in r1: #e ma sabse pahle 0 aage, uske baad 1 agge ,uske baad one by one value aate jayenge
    sum=sum+e
    
printf("sum",sum)'''

#range object main keval integer value aate hain

#
