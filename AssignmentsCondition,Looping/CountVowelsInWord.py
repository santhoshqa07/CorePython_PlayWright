
word = input("Enter a word: ").lower()
count = 0

for ch in word:
    if ch in 'aeiou':
        count += 1

print("Number of vowels:", count)