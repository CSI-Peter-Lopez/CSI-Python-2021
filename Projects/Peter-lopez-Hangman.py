import random
word_list = ["Río grande de Manatí", "Río grande de Arecibo", "Río Espíritu Santo", "Río Inabón", "Río Bucaná", "Río grande de Loíza", "Río Jacaguas", "Río Guanajibo", "Río Fajardo", "Río Cibuco" ]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6 
    print("Let's play Hand Hangman")
    print("Theme: Rivers of Puerto Rico")
    print(display_hangman(tries))
    print(word_completion)
    [print("\n")]
    while not guessed and tries > 0:
        guess = input("Guess a letter or word").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already tried", guess, "!")
            elif guess not in word:
                print("R.I.P")
                tries -= 1
                guessed_letters.append(guess)

def display_hangman(tries): 
    stages = [ """
                 --------
                 |   | 
                 |   O
                 |  /|\\ 
                 |   |
                 |  / \\ 
                 -
                 """,
                 """
                
                 --------
                 |   | 
                 |   O
                 |  /|\\ 
                 |   | 
                 |  /
                 -
                 """,
                 """
                 --------
                 |   | 
                 |   O
                 |  /|\\ 
                 |   |
                 |
                 -
                 """, 
                 """

                 --------
                 |   | 
                 |   O 
                 |  /| 
                 |   | 
                 |
                 -
                 """, 
                 """
                
                 --------
                 |   | 
                 |   O 
                 |   | 
                 |   | 
                 |
                 -
                 """, 
                 """
                
                 --------
                 |   | 
                 |   O 
                 |
                 |
                 |
                 - 
                 """, 
                 """

                 --------
                 |   | 
                 |
                 |
                 |
                 |
                 - 
                 """,
]

