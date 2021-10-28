name = input("Hello there! What is your name? ")
print(f"Hello {name}! Welcome to the Magic-8 ball")
question = input("what do you what to ask me \n")
print(f"{name} ask: {question}")

import random

random_number = random.randint(1, 12)
if (random_number == 1):
    print("Yes - definetely.")
elif (random_number == 2):
    print("It is decidedly so.")
elif (random_number == 3):
    print("without a doubt.")
elif (random_number == 4):
    print("Reply hazy, tray again.")
elif (random_number == 5):
    print("Ask Again later.")
elif (random_number == 6):
    print("Better not tell you now")
elif (random_number == 7):
    print("My sources say NO.")
elif (random_number == 8):
    print("Outlook not so good.")
elif (random_number == 9):
    print("Very doubtful.")
elif (random_number == 10):
    print("something better will happen in the future")
elif (random_number == 11):
    print("you are imagining")
elif (random_number == 12):
    print("It will happen if you are lucky")
else:
    print ("something went wrong")

