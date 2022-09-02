#1 to create list of n natural no
#l1=[]


'''n=int(input("enter the number"))
l1=list(range(1,10))
print(l1)
print(l1[0])
print(l1[1])
print()'''

#to crete a list of n odd natural no

'''n=int(input("enter the number"))
l1=list(range(1,2*n-1,2)) #list ka aage parenrthsis lagao toh wo object ban jaega
print(l1)
print()'''        

#to create list of even natural no::

'''n=int(input("enter the number"))
l1=list(range(2,n,2))
print(l1)
print()'''

#to find max no in a list


'''n=int(input("enter the number"))
l1=list(range(1,n,1))
print(l1)
print()
print(max(l1))
print(min(l1))
print(sum(l1))
print(l1.count(l1))'''

#to print all distinct element 

'''print("enter a list")
l4=eval(input("enter the number")) #eval function convert kar dega list main ise
print(l4)
print()
print(l4.index(2))#print function ma jo function kuch value return karenge woh value print hogi
'''

#index of the given number
'''n=int(input("enter the number"))
l1=list(range(1,n,1))
l2=l1.index(4)
print(l2)
print()'''

#to sort a list 
'''l1=[2,22,5,63,7,8]
l1.append(12)
print(l1)
l1.sort()
print(l1)
print()'''


#practice problem
l1=[2,3,5,2,23,43,89]
l2=[]
print(l1)
print()
l1.sort()
print(l1)
print()
l1.append(45)
print(l1)
print()
l1.insert(2,4) #2dn index pa 4 aajega 
print(l1)
print()
print(l1.index(5))
print()
print(l1.count(3))
print()
print(l1)
print()
l1.reverse()
print(l1)
#l2.copy(l1)
print(l2)
print(l1.pop(2))#2 index pa 43 hai 
print(l1)