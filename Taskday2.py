# Bitwise Operator
'''
#B1
a=10
b=6
print(a&b)

#B2
x=12
y=5
print(x|y)

#B3
num=8
print(~num)

#B4
a=15
b=9
print(a^b)

#B5
num=7
print(num<<2)

#B6
num=20
print(num>>1)

#B7

g=int(input())
h=int(input())
print("AND USER:",g&h)

#B8
m=int(input())
n=int(input())
print("XOR User:",m^n)


#STRING TASKS
#S9
c="hi"
print(c*4)

#S10

a="python"
print(a*3)

#S11

a="super"
b="man"
print(a+b)

#S12

a="hello"
b=" "
c="world"
print(a+b+c)

#S13

a=input()
print(a*5)

#S14

a=input()
b=input()
print(a+b)

#TypeCasting
#s15
a=input()
print(type(a))


#s16

age=int(input())

#S17

a=int(input())
b=int(input())
print("sum:",a+b)

#S18

mark1=int(input())
mark2=int(input())
avg=(mark1+mark2)/2
print("average:",avg)

#S19

a=int(input())
b=int(input())
print(3*a*2+b-2)


#S20

a=input()
print(type(a))
k=int(a)
print(type(k))

#IF Statement Tasks

#S26

if (10>=5):
   print("It is greater")

#S27

a=int(input())
if(a>=50):
 print("Greaterthan 50")

#S28

age=int(input())
if(age>=18):
 print("Yes age is eligible")

#S29

 a=int(input())
 if(a>=0):
  print("Its equal")

#IFELSE Tasks

#S30

a=int(input())
if((a%2)==0):
    print("Even")
else:
    print("Odd")

#S31
mark1=int(input())
if(mark1>=35):
 print("Student got pass mark")
else:
   print("Student got Failed")

#S32

a=int(input())
if(a>=0):
 print("THE NUMBER IS Positive")
else:
   print("The Number is Negative")

#S33

a=int(input())
if(a>=10):
   print("The number is greater than 10")
else:
   print("The number is not greater than 10")
 
#NestdIF

#S34

age=int(input())
height=int(input())
weight=int(input())
if(age>=18):
   if(height>=160):
      if(weight>=60):
         print("candidate is selcted")
      else:
         print("candidate is rejected")

#S35

age=int(input())
mark=int(input())
if(mark>=60):
 if(age>=17):
   print("Candidate is eligible")
else:
   print("Candidate is not eligible")

#S37

age=int(input())
height=int(input())
weight=int(input())
if(age>=16):
   if(height>=150):
      if(weight>=50):
         print("candidate is selcted")
      else:
         print("candidate is rejected")


#Matching Statements

#s38

day=int(input())
match day:
 case 1:
  print("Sunday")
 case 2:
  print("Monday")
 case 3:
  print("Tuesday")
 case 4:
  print("Wednesday")
 case 5:
  print("Thursday")
 case 6:
  print("Friday")
 case 7:
  print("Saturday")

#S39

colour=int(input())
match colour:
 case 1:
  print("Red")
 case 2:
  print("Blue")
 case 3:
  print("Green")  

 #S40

Fruits=int(input())
match Fruits:
 case 1:
  print("Apple")
 case 2:
  print("Mango")
 case 3:
  print("Orange")
 case 4:
  print("Banana5")  
'''

#Unit Digit

#S21

s=input()
print("Unit digit",s[len(s)-1])

#s22

n=int(input())
print(n%10)

#S23
n=int(input())
print(n//10)

#s24

sec=input()
print("Second last digit",sec[len(sec)-2])

#s25

Num=56789
print(Num%10)








