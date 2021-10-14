import random
def main():
    print("Welcome to Rock, Paper, Scissors Game!!!!")
    rps = ["rock", "paper", "scissors"]
    play_again = "y"

    while (play_again == "y"):
        playerChoice = input("lets play. Choose one: rock, paper, or scissors.\n")
        computerChoice = random.choice(rps)

        print(f"Computer selected: {computerChoice}")
        print(f"Player selected:  {playerChoice}")


        if(playerChoice == computerChoice):
            print("You tied :/ ")
        elif(playerChoice == "rock" and computerChoice == "paper"):
            print("PAPERS covers Rock. You lost!!!! :( ")
        elif(playerChoice == "scissors" and computerChoice == "paper"):
             print("SCISSORS cut PAPER. You win!!!! :) ")
        elif(playerChoice == "scissors" and computerChoice == "rock"):
             print("Rock break SCISSORS. You lost!!!! :( ")
        elif(playerChoice == "paper" and computerChoice == "rock"):
             print("PAPERS covers Rock. You win!!!! :) ")
        elif(playerChoice == "paper" and computerChoice == "scissors"):
             print("Scissors cut PAPER. You lost!!!! :( ")
        elif(playerChoice == "rock" and computerChoice == "scissors"):
            print("Rock break SCISSORS. You lost!!!! :( ")
        else:
            print("Something ins't right. Maybe try again")
        play_again = input("Play again? Enter 'y' for yes or 'n' for no.")
    print("Game over")
main()