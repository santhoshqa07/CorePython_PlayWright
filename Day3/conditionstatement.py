#if

#Example 1: age>=18 eligible
# age=15
# if age>=18:
#    print("eligible for vote")

#Example 2: check the amount value after discount

# amount = 1001
# discount = 0
#
# if amount > 1000:
#     discount = amount*10/100
#
# print("The actual amount after reducing discount:", amount-discount)
#
# #if else
# #Example 1:
# age= 15
#
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("You are not old enough to vote")

#Example 2: check the number is even or odd

# num = 10
#
# if num % 2 == 0:
#     print("Even Number :", num)
# else:
#     print("Odd Number :", num)

#if elif else
#Example 1
# suppose there are 3 different slabs of discount on a purchase-
# 20% on amount exceeding 10000,
# 10% for amount between 5000 -10000
# 5% if it is between 1000-5000
# No discount if the amount is less than 1000

# amount = 15000
# print("The actual amount:",amount)
#
# if amount > 10000:
#     discount = amount*20/100
# elif amount >= 5000:
#     discount = amount * 10/ 100
# elif amount >=1000:
#     discount = amount * 5 / 100
# else:
#     discount = 0
#
# print("The discount amount:",amount-discount)

#Example 2: print day based on week no

# Weekno =5
#
# if Weekno==1:
#     print("sunday")
# elif Weekno==2:
#     print("monday")
# elif Weekno==3:
#     print("tuesday")
# elif Weekno==4:
#     print("wednesday")
# elif Weekno==5:
#     print("thursday")
# elif Weekno==6:
#     print("friday")
# elif Weekno==7:
#     print("saturday")
# else:
#     print("Invalid Weekno")



#nested if_else:

#num--> divisible by both the 2 & 3
#num --> divisible by 2 & but not 3
#num --> divisible by 3 & but not 2
#num --> Not divisible by 2 & 3

#num=9

# if num%2==0:
#     if num%3==0:
#         print("The number is divisible by 2 and 3")
#     else:
#         print("The number is divisible only by 2")
# else:
#     if num%3==0:
#         print("The number is divisible only by 3")
#     else:
#         print("The number is not divisible only by 2 and also 3")



##short hand if

# a,b = 10,20
#
# if a>b:print("a is greater than b")

##short hand if else

# print("a is greater") if a>b else print("b is greater")

# and (Logical Operator) with if elif else
# Find Largest of 3 numbers
# a, b, c
# a>b and a>c a is largest
# b>a and b>c b is largest
# c is largest

# a=30
# b=20
# c=40
#
# if a>b and a>c:
#     print("a is Largest")
# elif b>a and b>c:
#     print("b is Largest")
# else:
#     print("C is Largest")


#pass

a=20
b=30

if a>b:
    pass

print("something")















