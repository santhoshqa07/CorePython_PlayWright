
num = int(input("Enter a number: "))
sum = 0

if len(str(num)) > 1:
    while(num>0):
        sum = sum + num%10
        num = num//10
else:
    print("The number should be more than one digit")


print("The sum of entered number is ",sum)



