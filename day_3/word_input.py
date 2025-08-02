word = input("Enter your word: ")

result = ""

for letter in word:
    low_letter = letter.lower()
    if low_letter != "a" and low_letter != "e" and low_letter != "i" and low_letter != "o" and low_letter != "u":
        result += letter

print("Word without vowels:", result)

word = input("Enter your word: ")

result = ""

for letter in word:
    if letter.lower() not in "aeiou":
        result += letter

print("Word without vowels:", result)

# word = input("Enter word : ").upper()
#
# final_word = ""
#
# vowels = "AEIOU"
#
# for letter in vowels:
#