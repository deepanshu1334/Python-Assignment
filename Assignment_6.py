#1

'''a=int(input("enter the number"))
if a>0:
    print("no is posotive")
if a<=0:
    print("no is non posotive")   '''

#2

'''n=int(input("enter the number"))
if n>0:
    print("no is posotive") 
else:
    print("non is non posotive")   
'''

'''x=("no is divisible by 5" if int(input())%5 else "no is not divisible by 5")
print(x)
print()'''

#3

'''n=int(input("enter the number"))
if n%2==0:
    print("no is even",n)
else:
    print("odd")  '''

#4

'''a=int(input("Enter the number"))
b=int(input("Enter the number"))
if a>b:
    print("a is greatest")
else:
    print("b is greatesst")    '''


#5

'''x=("odd" if int(input("enter a number"))%2 else "Even")
print(x)'''

#6

'''print("enter a number")
a,b=int(input()),int(input())
print(a if a>b else b)'''

#7
'''print("odd" if int(input("enter a number"))%2 else "even")'''


#5 dicatonary order

'''print("Enter two words")
a,b=input(),input() #jo bada hai woh baad ma aage
print(b,a if a>b else a,b)'''

#6 three digit no 

'''x=int(input("enter a number"))
if 99<x<1000:
    print("no is three digit no")
else:
    print("not a three digit number")'''


#7

'''n=int(input("Enter a number"))
if n>0:
    print("posotive")
elif n==0:
    print("no is zero ")
else:
    print("no is nagative")      '''

#8 real and imagionary roots

'''print("enter value of a and b")
a,b,c=int(input()),int(input()),int(input())
if b*b-4*a*c>0:
    print("roots are real and unequal")
elif b*b-4*a*c<0:
    print("roots are imagionary")
else:
    print("roots are real and equal")    '''


#8 year is leap year or not 

'''print("enter year number")
year=int(input())
if year%400==0 or year%100!=0 and year%4==0:
    print("leap year")
else:
    print("non leap year")  '''  


#10

'''print("enter three number")
a,b,c=int(input()),int(input()),int(input())
print((a if a>c else c) if a>b else(b if b>c else c))   '''

#11 month value in numeeric format 

'''month=int(input("enter month number"))
if month in (1,3,5,7,8,10,12):
    print("31 days")
elif month in (4,6,9,11):
    print("30 days")
elif month==2:
    print("28 or 29 days")   
else:
    print("invalid month number") '''

#13 complex 

x=complex(input("enter a complex number"))
print(x.real) if x.real>x.imag else print(x.imag)
         

