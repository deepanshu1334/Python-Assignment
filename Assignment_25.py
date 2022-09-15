#1 Inheritance

'''class user:
    a="deepanshu"
    b=33
    c=True
    d=12
    def __init__(self):
        self.name="deepanshu kuamr"
        self.age=12
        self.email="dk1078451@gmail.com"

    def show(self):
        print(self.name)
        print(self.age)
        print(self.email)

    def show1(self):
        return self.name,self.age,self.email   

    @classmethod
    def show2(cls):
        return cls.a,cls.b,cls.c
    @classmethod    
    def show3(cls):
        return cls.b+cls.d         
         

class student(user):
    def disp(self):
        print("this is a deepanshu kumar")

s1=student()
s1.disp()
s1.show()
print()        

s2=s1.show1()
print(s2)

print(s1.show1())
print()
print(student.show2())
print()
print(student.show3())
print()'''


#2

'''class father:
    money=2000
    def show(self):
        print(" i am deepanshu kuamr")

    @classmethod
    def show1(cls):
        print(cls.money)
        print("parent class method")

    @staticmethod
    def stat():
        a=10
        print("parent class instance method")

class son(father):
    def show2(self):
        print("this is student class mehtod")

s1=son()
s1.show2()
s1.show1()
s1.stat()'''

#3

'''class father:
    def __init__(self,n):
        self.money=n
        #self.money=2999
        print("father class constryctior")

    def show(self):
        print(self.money)    

    def show1(self):
        print("deepanshu kumar is a champion")    

class son(father):
    def __init__(self):
        print("your boy deepanshu kumar")
    def disp(self):
        print(self.money)

s1=son()
#s1=son(2333)
#s1.disp()
s1.show()
'''
print()
#4

'''class father:
    def __init__(self,n):
        self.m=n
    #def __init__(self):
        #self.m=1222
        print("father class contstructor")

    def show(self):
        print(self.m)

class son(father):
    def __init__(self,r):
        self.m=r
        self.car="BMW"
        print("son class constrytcor")
    
    ''#'def __init__(self):
      #  self.m=22
      #  self.car=12
     #   print("son class constructor")
    def disp(self):
        print("son class instacnce method")'''    
    

'''s1=son(3)
#s1=son()
s1.disp()
s1.show()  '''      
#5

'''class father:
    def __init__(self):
        print("father class constructor")

    def show(self):
        print("father class instance method")
    
class son(father):
    def __init__(self):
        super().__init__()
        print("son class constructoe")

s1=son()
s1.show()'''


#4

class father:
    def __init__(self,a,b):
        self.age=a
        self.money=b
    #def __init__(self,m):
    #   self.money=m
        print("father class constructor")

    def show(self):
        print("father class instance method")
    def add(self):
        return self.age+self.money,self.age-self.money,self.age*self.money    

class son(father):
    def __init__(self,a,b):
        super().__init__(a,b)

    #def __init__(self,m):
    #    super().__init__(m)
        print("son class construcitor")
        #print(self.money)
        print(self.age)
        print(self.money)

#s1=son(23)
s1=son(1,3)
s1.show()
print(s1.add())                   
        
        