#1 to store multiple items in a tuple

'''t1=("java","python","sql","c")
print(t1)
print()
print(t1[0],t1[1])
print()'''

#2

'''t2=(34)
print(t2)
print()'''

#to reverse a tuple

t1=(1,2,3,4,5)
print(t1[::-1]) #beging value first element se start hogi aur end value last value bhi include hoga aur step 1 hoga
print()

#4 to swap two tuple

t1=(1,3,4)
t2=(2,5,6)
print("the value of t1 is",t1)
print("the value of t2 is",t2)
t2,t1=t1,t2
print("the value of t1",t1)
print("The value of t2 is",t2)
print()

#5 to check all items are same in a tuple
t1=(2,4,5,6,12,4)
t2=(2,3,4,5,6)
print(t1==t2)
print()

#6 divide tuple in four variable
t1=(100,200,300,400)
l1=list(t1) #pass tuple into a list
print(l1)
a,b,c,d=l1
print(a,b,c,d,end=" ")
print()
#7 copy elements in a tuple

t1=(1,2,3,4,5,6,7,8)
t2=()
print(t2)
t2=tuple(t1[4:6:1])
print(t2,end=" ")
print()

#8 to sort a tuple
t1=(('a',21),('b',37),('c',11),('d',29))
t2=tuple(list(t1))
print(t2)
print()
l1=list(t1)
l1.sort()
print(l1)
print()
print(t1[::-1])
print()
#or
#t1=input("Enter the string")
t1=(3,4,5,6)
l1=list(t1)
l1.sort()
print(l1)
t2=tuple(l1)
print(t2) #tuple is sort due to this
print()

#9

t1=("python",[10,20,30],(2,4,16))
for e in t1:
    print(e)
print() 

#10

t1=(22,3,4,5,6,7)
l1=list(t1)
print(l1)
l1.insert(0,222) #0 index pa 222 aa gaya
print(l1)
print()
t2=tuple(l1)
print(t2)
print()

