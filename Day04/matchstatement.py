
#The match statement is used to perform different actions based on different conditions
#Instead of writing the many if..else statements, you can use the match statements.

#example 1:

day=5

match day:
    case 1: print("Sunday")
    case 2: print("Monday")
    case 3: print("Tuesday")
    case 4: print("Wednesday")
    case 5: print("Thursday")
    case 6: print("Friday")
    case 7: print("Saturday")
    case _: print("Invalid")


day=7
match day:
    case 2 | 3 | 4 | 5 | 6: print("Week Days")
    case 1| 7: print("Week end")
    case _: print("Invalid")



