#1
a=3
b=str(3)
print(type(b))
print()

#2 unicode of m
a="m"
print(ord(a))

#3
a="d"
print(ord(a))
print()

#4 to print octal of any number
a=64
print(oct(a))

#5 to print hexadecimal of any number
a=45
print(hex(a))

#6
x=0b1100101
print(x)

#7 to store hexadecimal in a variable and print in octal format
x=0x2F
print(oct(x))

#8 to store an octal no in a variable and print in a binary format
x=0o125
print(bin(x))

#10 to add two numbers in a hexa and oct and result in binary
print(bin(0o25)+bin(0x39))