#1 all programming language
s1={"java","python","c++","c","rust"}
print(s1)
print()

#2 to store your own information
s1={"deepanshu","20","male","6 feet"}
print(s1)
print()

#3
s1={2,3,4,4,4,"Deepanhsu kumar"}
print(type(s1))
print(s1)
s1.add(23)
print(s1)
print()

#4
s1={"java","python","django"}
for e in s1:
    if e=="python":
        print("python is present")
print()

#4
s1={"java","python","sql"}
s2=set(s1)
print(s2)
s2.add("c")
s2.add("cpp")
s2.add("nosql")
print(s2)
print()

#7
s1={"python","javascript","django","sql"}
s1.remove("sql")
print(s1)
print()

#8
for e in s1:
    del e
print(s1)
print()    

#9 
#jo characacter baad ma aa rahe,woh bada hai#
print(max(s1))
print()
print(min(s1))
print()