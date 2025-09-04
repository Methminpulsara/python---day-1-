def get_words(number_of_times):
    words = []
    for count in range(number_of_times):
        word = input("Enter your Words : ")
        words.append(word)
    return words

def count_length(words , min_length):
    return [word for word in words if len(word) > min_length]

def get_first_letter(words):
    return [word[0] for word in words]

def muiliply_first_letter(words , count ):
    return [word[0] * count for word in words]

user_input = get_words(2)
print(get_first_letter(user_input))
print(count_length(words=user_input, min_length=3))
print(muiliply_first_letter(user_input,3))
