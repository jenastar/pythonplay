##file for iteration python
# Get user input
user_word = input("Please enter a word: ").lower()  # Convert to lowercase for consistency

# Create alphabet string
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# First phase: print letters until we reach the first character
for letter in alphabet:
    print(letter)
    if letter == user_word[0]:
        break

# Second phase: build the string progressively
current_string = user_word[0]  # Start with first character
target_length = len(user_word)
current_position = 1  # Start checking from second character

while len(current_string) < target_length:
    for letter in alphabet:
        test_string = current_string + letter
        print(test_string)
        if test_string == user_word[:len(test_string)]:
            current_string = test_string
            break

print(f"\nFinal matched string: {current_string}")
