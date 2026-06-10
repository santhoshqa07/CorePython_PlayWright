from itertools import count

word = input("Enter a word: ").lower()

countA = 0
countB = 0

for i in word:
    if i == 'a':
        countA += 1
    elif i == 'b':
        countB += 1
    else:
        continue


print("The count of A is:",countA)
print("The count of B is:",countB)

#Ex 2

