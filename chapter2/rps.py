# Chapter 2 discusses and demonstrates creating classes,
# but doesn't assign doing so as an explicit exercise
# I'll refactor my code here for practice


import random

OPTIONS = ("rock", "paper", "scissors")


class RPSSimulator:
    """
    Simulates one round of rock paper scissors
    """

    def __init__(self):
        self.computer_choice: str
        self.human_chioce: str

    def player_choose(self) -> None:
        """
        Display choices and ask human player to pick
        """
        print("(1) Rock\n(2) Paper\n(3) Scissors")
        self.human_choice = OPTIONS[int(input("Enter the number of your choice: ")) - 1]

    def computer_choose(self) -> None:
        """
        Method to randomly choose one option for the computer player
        """
        self.computer_choice = random.choice(OPTIONS)

    def announce_pick(
        self,
    ) -> None:
        """
        Announce player and computer choices
        """
        print(f"You chose {self.human_choice}")
        print(f"The computer chose {self.computer_choice}")

    def score_game(self, human_beats: str, human_loses: str) -> None:
        """
        Print outcome of non-draw games
        """
        if self.computer_choice == human_beats:
            print("Yes,", self.human_choice, "beat", self.computer_choice)
        elif self.computer_choice == human_loses:
            print("Sorry,", self.computer_choice, "beat", self.human_choice)

    def determine_outcome(
        self,
    ) -> None:
        """
        Output results of the game
        """
        if self.human_choice == self.computer_choice:
            print("Draw!")

        if self.human_choice == "rock":
            self.score_game(human_beats="scissors", human_loses="paper")
        elif self.human_choice == "paper":
            self.score_game(human_beats="rock", human_loses="scissors")
        elif self.human_choice == "scissors":
            self.score_game(human_beats="paper", human_loses="rock")

    def simulate(self) -> None:
        """
        Play one round of rock paper scissors
        """
        self.player_choose()
        self.computer_choose()
        self.determine_outcome()


RPS = RPSSimulator()
RPS.simulate()
