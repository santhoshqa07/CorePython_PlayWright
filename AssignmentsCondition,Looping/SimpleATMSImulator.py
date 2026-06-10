
balance = 0

while True:
     print("ATM Menu:")
     print("1. Deposit")
     print("2. Withdraw")
     print("3. Exit")

     Choice = int(input("Enter your choice: "))
     if Choice == 1:
         amount = float(input("Enter the deposit amount: "))
         balance += amount
         print("The Balance after deposit is:", balance)
     elif Choice == 2:
         amount = float(input("Enter the withdraw amount: "))
         if balance > amount:
             balance -= amount
             print("The Balance after withdrew is:", balance)
         else:
             print(balance,": Insufficient Balance! You cannot withdraw more money")

     elif Choice == 3:
            print("Exiting ATM..Goodbye ")
            break
     else:
         print("Invalid Choice")




