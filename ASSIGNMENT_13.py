#ASSIGNMENT13
#1

l1=["java","python","sql","c"]
print(l1)
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[0],l1[1],l1[2],l1[3],end=" ")
print()

#2 to get the data type of a list
print(type(l1))
print(type(l1[0]))
print(type(l1[1]))

#3 to get last item of a list

print(l1[3])#to get last item of a list
print()        

#4 to change value of sql with no sql and  
l2=["java","sql","Reactnative","javascript","python"]
l2[1]="No sql"
l2[2]="flutter"

print(l2)
print()

#5to add an item at the end of a list
l3=["java","Sql","c","reactnative"]
l3.append("python")
print(l3)
print()

#6 to append an item from the list
l1=["java","python","sql"]
l2=["c","cpp","nosql"]
l1.append(l2)
print(l1)
print()

# 7 to print all items by reffering their index number
l4=["java","sql","c","reactnative","javascript","python"]
print(l4[0],l4[1],l4[2],l4[3],l4[4],l4[5])
print()

l4.sort()
print(l4)
print()

#9 to create a list of city names taken from user

'''a=input("enter city name")
b=input("enter city name")
c=input("enter your name")
l1=[a,b,c]
print(l1)
print(l1[0])
print(l1[1])
print(l1[2])
print()'''

#to create list of a given no where each element of a list 

n=int(input("enter the number"))
a=n//10
b=a//10
c=b//10
print(a,b,c)
l1=[a,b,c]
print(l1)
l1.sort()
print(l1)
print()