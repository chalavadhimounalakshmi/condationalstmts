#if-else:
#1.Check whether a given number is a 3 digit number or not.
#using "abs"  if we give negative numbers also it tells it is a 3 digit number
n=int(input('enter a number'))
if 100 <= abs(n) <= 999:
    print("it is a 3-digit Number")
else:
    print("It is not a 3-digit Number")
#___________________________________________________________________________________________________________________________________________#
#2.check whether a given number is divisible by both 3 and 5 or not.
n=int(input("Enter a Number"))
if n %  3 == 0  and n %  5 == 0 :
    print("divisible by both 3 and 5")
else:
    print("The given number is not divisible by 3 and 5")
#______________________________________________________________________________________________________________________________________________#
#3.check whether a given triangle is a valid triangle or not.
#logic:the sum of any two sides must be greater than the third side
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if a + b > c and a + c > b and  c + b > a:
    print("It is a valid triangle") 
else:
    print("It is not a valid triangle")
#_________________________________________________________________________________________________________________________________________________#
#4.check whether a given number is a multiple of 10 or not
n=int(input("Enter a Enter: "))
if n % 10 ==0:
    print("multiple of 10")
else:
    print("Not Multiple of 10")
#_____________________________________________________________________________________________________________________________________#
# if-elif-else:
#1.Check the type of triangle based on its sides.
   #Equliteral,Isosceles,or Scalene.
  #logic 1.Equilateral -> all 3 sides are equal EX:5,5,5
  #      2.Isosceles -> any 2 sides are equal EX: 5,5,3
  #      3.Scalene -> all 3 sides are different EX:4,5,6
a=int(input("Enter First Side: "))
b=int(input("Enter Second Side: "))
c=int(input("Enter third side: "))
if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or c == a:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
#______________________________________________________________________________________________________________________________________#
#4.calculate the discount based on shooping amount.
   #1.below amt 1,000 at no discount,
   #2.a 1000 to 4999 at 10% discount,
   #3.amt 5,000 to 9,999 at 20% discount,
   #4.amt 10,000 and above at 30% discount.
amt=int(input("Enter amount"))
if amt < 1000:
    print("No Discount")
elif amt < 5000:
    print("10% Discount")
elif amt < 10000:
    print("20% Discount")
else:
    print("30% Discount")
#_______________________________________________________________________________________________________________________________________________#
#6.Check whether a given year is a leap year or not .
   #logic1.Year % 400 ==0
   #     2.year % 4 == 0 and year % 100 != 0
year=int(input("Enter year"))
if year % 400 == 0:
    print(" leap Year")
elif year % 4 == 0 and year % 100 !=0:
    print("leap year") #ex:2024,2026 etc
else:
    print("Not a leap year ") #1900 etc
#_____________________________________________________________________________________________________________________________________________#
#3.Display the age category
#  below 13 at child 
# 13 to 19 at teenager
# 20 to 59 at adult
# above 60 at senior citizen.

age=int(input("Enter your age"))
if age < 13:
    print("You are Child")
elif age < 19 and age > 13:
    print("Your are teenager")
elif age < 60 and age > 20:
    print("You are Adult")
else:
    print("Senior Citizen")
#____________________________________________________________________________________________________________________________________________#
#5.Display the season based on the month.
#We take a month number as input.
#If the month is 3, 4, or 5 → Spring
#Else if the month is 6, 7, or 8 → Summer
#Else if the month is 9, 10, or 11 → Autumn
#Else if the month is 12, 1, or 2 → Winter
#Otherwise → Invalid month

month = int(input("Enter month number: "))
if month >= 3 and month <= 5:
    print("Spring")
elif month >= 6 and month <= 8:
    print("Summer")
elif month >= 9 and month <= 11:
    print("Autumn")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
else:
    print("Invalid month")
#______________________________________________________________________________________________________________________________________________#
#Calculate the electricity bill based on units consumed.
#0–100 units → ₹2/unit
#101–200 units → ₹3/unit
#201–300 units → ₹5/unit
#Above 300 → ₹7/unit
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
elif units <= 300:
    bill = units * 5
else:
    bill = units * 7

print("Electricity bill =", bill)
#_________________________________________________________________________________________________________________________________________#
#Nested if :
#1.Check whether a person is eligible to donate blood.
# age should be between 18 and 60.if eligible by age,weight should be above 50kgs.
age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))
if age >= 18 and age <= 60:
    if weight > 50:
        print("Eligible to donate blood")
    else:
        print("Not eligible: Weight should be above 50 kg")
else:
    print("Not eligible: Age should be between 18 and 60")
#____________________________________________________________________________________________________________________________________________#
#2.Display the grade based on average only if the student has passed in all 4 subjects.
#Take marks for 4 subjects.
#Check whether the student passed all 4 subjects.
#If yes, calculate the average and display the grade.
#If even one subject is failed → No grade / Fail.
sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))
sub4 = int(input("Enter marks for subject 4: "))
if sub1 >= 35 and sub2 >= 35 and sub3 >= 35 and sub4 >= 35:
    average = (sub1 + sub2 + sub3 + sub4) / 4

    if average >= 90:
        print("Grade A")
    elif average >= 75:
        print("Grade B")
    elif average >= 60:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Fail")
#______________________________________________________________________________________________________________________________________#
#3.Check whether a student is eligible for a scholarship.
#Age should be above 18. If eligible by age, score should be above 86.
#The important part is: first check age, then check score.
age = int(input("Enter your age: "))
score = int(input("Enter your score: "))

if age > 18:
    if score > 86:
        print("Eligible for scholarship")
    else:
        print("Not eligible")
else:
    print("Not eligible")
#________________________________________________________________________________________________________________________________________#




