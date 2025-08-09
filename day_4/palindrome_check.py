# word = input("Enter Your Word: ")
#
# reversed_word = ''.join(reversed(word))
#
# print("Reversed word:", reversed_word)
#
# # Compare
# if reversed_word == word:
#     print("It’s a palindrome!")
# else:
#     print("Not a palindrome.")


word =  input("Enter Your Word :  ")
letters_copy =[]
letters = []
for letter in word:
    letters.append(letter)

letter_copy = letters[:]
letters.reverse()

if letter_copy == letters:
    print("Match")
else:
    print("Not Match")