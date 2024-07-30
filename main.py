# Functions definition
def new_game():
    guesses= []
    correct_guesses= 0
    question_num= 1

    for key in questions:
        print("-------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("A,B,C or D: ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num+=1
    display_score(correct_guesses,guesses)

def check_answer(answer,guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Incorrect")
        return 0
def display_score(correct_guesses,guesses):
    print("----------------------------------")
    print("Results")
    print("----------------------------------")
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Answers: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()
    score= int((correct_guesses / len(questions))*100)
    print("Your Score: "+str(score)+"%")
def play_again():
    pass

questions= {
    "who created python?: " : "A",
    "what year was python created?: " : "B",
    "is the earth round?: ": "A" ,
    "Python is ":"D"
}

options= [
    ["A. Guido van Rossum","B. Ferhi Nour","C. Lionel Messi","D.Elon Musk"],
    ["A. 2020","B. 1991","C. 2011","D. 2000"],
    ["A. True","B. False","C. I don't know","D. Sometimes"],
    ["A. CEO","B. Football Player","C. Developer","D. Programming language"]
]


new_game()