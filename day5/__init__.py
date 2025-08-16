
def get_word(number_of_time):
    words = []
    for count in range(number_of_time):
        word = input("Enter Word : ")
        words.append(word)
    return words

def by_length(words , min_length):
    return [word for word in words if len(word) >  min_length]

def get_first_letter(words):
    return [word [0] for word in words]

def get_first_letter_multiplied(words , count):
    return [word [0] * count for word in words]

words = get_word(2)
print(by_length(words, 3 ))
print(get_first_letter(words))
print(get_first_letter_multiplied(words , 3))