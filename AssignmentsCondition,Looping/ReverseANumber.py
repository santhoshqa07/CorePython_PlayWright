


num = int(input("Enter a number: "))
reverse = 0

if len(str(num)) > 1:
    while(num>0):
        digit = num%10  #get last digit
        reverse = reverse*10 + digit
        num = num//10 #Removes last digit
else:
    print("Enter the number with more than one digit")

print("The number after reversal:", reverse)



