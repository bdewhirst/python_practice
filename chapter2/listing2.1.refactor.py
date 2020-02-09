# this is my work on the exercise.
# Listing 2.1 (cleaning up) Shoddy procedural code
import random

OPTIONS = ("rock", "paper", "scissors")


def player_choose() -> str:
    """
    Display choices and ask human player to pick
    """
    print("(1) Rock\n(2) Paper\n(3) Scissors")
    choice: int = OPTIONS[int(input("Enter the number of your choice: ")) - 1]
    return choice


def choose(player: str,) -> str:
    """
    If player is 'human', solicit input, otherwise pick randomly
    """
    if player == "human":
        choice: str = player_choose()
    else:
        OPTIONS = ["rock", "paper", "scissors"]
        choice = random.choice(OPTIONS)
    return choice


def play_rock_paper_scissors() -> None:
    """
    Play one round of rock paper scissors
    """
    human_choice = choose(player="human")
    # refactor this printing bit
    print(f"You chose {human_choice}")
    computer_choice = choose(player="ai")
    print(f"The computer chose {computer_choice}")

    # next section to refactor
    if human_choice == "rock":
        if computer_choice == "paper":
            print("Sorry, paper beat rock")
        elif computer_choice == "scissors":
            print("Yes, rock beat scissors!")
        else:
            print("Draw!")
    elif human_choice == "paper":
        if computer_choice == "scissors":
            print("Sorry, scissors beat paper")
        elif computer_choice == "rock":
            print("Yes, paper beat rock!")
        else:
            print("Draw!")
    elif human_choice == "scissors":
        if computer_choice == "rock":
            print("Sorry, rock beat scissors")
        elif computer_choice == "paper":
            print("Yes, scissors beat paper!")
        else:
            print("Draw!")


play_rock_paper_scissors()
