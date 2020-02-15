import os

import datetime


class Greeter:
    """
    Hypothetical encapsulated e-commerce software greeting class
    """

    def __init__(self):
        self.now: datetime.datetime = datetime.datetime.now()
        self.ls: str = os.linesep  # correct line separator (ls) for OS

    def _day(self) -> str:
        """
        Returns the current day

            e.g., 'Sunday'
        """
        day: str = self.now.strftime("%A")
        return day

    def _part_of_day(self) -> str:
        """
        Returns 'morning' if it is before Noon, 'afternoon' 1201-1659, and 'evening' at other times
        """
        hour: int = int(self.now.strftime("%H"))
        time_of_day: str
        if hour < 12:
            time_of_day = "morning"
        elif (hour >= 12) and (hour < 17):
            time_of_day = "afternoon"
        else:
            time_of_day = "evening"
        return time_of_day

    def greet(self, store: str) -> None:
        """
        Given the name of the store, print a certain greeting using private methods
        """
        message = f"""Hi, welcome to {store}!{self.ls}How's your {self._day()} {self._part_of_day()}?{self.ls}Here's a coupon for 20% off!"""
        print(message)


STORE_NAME = "Mallmart"
a_greeter = Greeter()
a_greeter.greet(store=STORE_NAME)
