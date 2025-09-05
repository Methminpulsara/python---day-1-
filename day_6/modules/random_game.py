import random

quizies = {
    1 : {"ques" : "Who is the president of Sri Lanka" , "anwser" : "ADK"},
    2: {"ques" : "Who is You " , "anwser": "metha"}
}


while True:
    q_ids = [x for x in quizies.keys()]

    choise = random.choice(q_ids)

    print(quizies[choise]["ques"])
    user_input = input("Enter Your anwser : ")

    if user_input in quizies[choise]["anwser"]:
        print(f"\nYour Anwser is correct {quizies[choise]['anwser']}")
    else:
        print("\nyour anwser in incorrect")
        break