# Print Formatting

print("Hello World",end=" ")
print("Welcome Python")
print("Laptop","Mouse","Keyboard",sep="|")

# Variables

name="Ravi"
age=22
city="Chennai"
print(name,age,city,sep="-")

#Multiple Assignment

name,age,student="Meena",20,True
print(name,age,student)

# Indexing

word="Python"
print("First Letter:",word[0],"Third Letter:",word[2],"Last Letter:",word[5])

#Arithmetic Operators

print(25+10)
print(50-20)
print(8*5)
print(100/10)
print(10%3)
print(2**4)
print(20//3)

#BODMAS Expression

print("Bodmas Expression:",3+2*5**2)

#Assignment Operator

num=50
num+=25
print(num)

num=100
num/=10
print(num)

#Comparison Operator

print(10>5)
print(20<15)
print(5==5)
print(10!=8)
print(7>=7)
print(6<=2)

#String Comparison

a="apple"
b="Apple"
print("String Comparison:",a==b)

# Logical Operators

print(10>5 and 5==5)
print(5>10 or 10==10)
print(not(5>2))

#Membership Operator

numbers=[10,20,30,40,50]
print("Membership Operators:",20 in numbers)
print(60 in numbers)
print(30 not in numbers)

#Swap Variables

a=10
b=20
a,b=b,a
print(a,b)

#Bitwise XOR

a=6
b=3
print("Bitwise XOR:",a^b)
