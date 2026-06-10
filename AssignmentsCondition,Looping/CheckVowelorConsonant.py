



char = input("Enter a character: ")

# Check input length
if len(char) != 1:
    print("Please enter only one character")

# Check alphabet
elif not char.isalpha():
    print("Please enter an alphabet only")

# Check vowel or consonant
elif char == 'a' or 'e' or 'i' or 'o' or 'u':
    print("Entered character is vowel")

else:
    print("Entered character is consonant")

    

