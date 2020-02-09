# this is my solution to the exercise
# Listing 2.1 (cleaning up) Shoddy procedural code
import random

OPTIONS = ("rock", "paper", "scissors")


def player_choose() -> str:
    """
    Display choices and ask human player to pick
    """
    print("(1) Rock\n(2) Paper\n(3) Scissors")
    choice: str = OPTIONS[int(input("Enter the number of your choice: ")) - 1]
    return choice


def choose(player: str,) -> str:
    """
    If player is 'human', solicit input, otherwise pick randomly
    """
    if player == "human":
        choice: str = player_choose()
    else:
        choice = random.choice(OPTIONS)
    return choice


def announce_pick(player: str, choice: str) -> None:
    """
    Announce player or computer's choice
    """
    if player == "human":
        print(f"You chose {choice}")
    else:
        print(f"The computer chose {choice}")


def score_game(human_choice: str, computer_choice: str, human_beats: str, human_loses: str) -> None:
    """
    Print outcome of non-draw games
    """
    if computer_choice == human_beats:
        print("Yes,", human_choice, "beat", computer_choice)
    elif computer_choice == human_loses:
        print("Sorry,", computer_choice, "beat", human_choice)


def determine_outcome(human_choice: str, computer_choice: str) -> None:
    """
    Output results of the game
    """
    if human_choice == computer_choice:
        print("Draw!")

    if human_choice == "rock":
        score_game(
            human_choice=human_choice, computer_choice=computer_choice, human_beats="scissors", human_loses="paper"
        )
    elif human_choice == "paper":
        score_game(
            human_choice=human_choice, computer_choice=computer_choice, human_beats="rock", human_loses="scissors"
        )
    elif human_choice == "scissors":
        score_game(human_choice=human_choice, computer_choice=computer_choice, human_beats="paper", human_loses="rock")


def play_rock_paper_scissors() -> None:
    """
    Play one round of rock paper scissors
    """
    human_choice = choose(player="human")
    computer_choice = choose(player="ai")
    for player, choice in {"human": human_choice, "computer": computer_choice}.items():
        announce_pick(player, choice)
    determine_outcome(human_choice=human_choice, computer_choice=computer_choice)


play_rock_paper_scissors()
