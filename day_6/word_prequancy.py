words = []
frequincies = {}
while True:
    word = input("Enter Word or press 1 to exit :  ")

    if word == "1":
        break
    words.append(word)


for word in words:
    if word not in frequincies:
        frequincies[word] = 1
    else:
        frequincies[word] +=1
print(frequincies)