# Functions definition
def new_game():
    guesses= []
    correct_guesses= 0
    question_num= 1

    for key in questions:
        print("-------")
        print(key)
def check_answer():
    pass
def display_score():
    pass
def play_again():
    pass

questions= {
    "who created python?: " : "A",
    "what year was python created?: " : "B",
    "is the earth round?: ": "A" 
}

options= [
    ["A. Guido van Rossum","B. Ferhi Nour","C. Lionel Messi"],
    ["A. 2020","B. 1991","C. 2011"],
    ["A. True","B. False"]
]


new_game()