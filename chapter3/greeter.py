import datetime


class Greeter:
    """
    Hypothetical encapsulated e-commerce software greeting class
    """
    def __init__(self):
        self.now: datetime.datetime= datetime.datetime.now()

    def _day(self):
        """
        Returns the current day

            e.g., 'Sunday'
        """
        pass

    def _part_of_day(self):
        """
        Returns 'morning' if it is before Noon, 'afternoon' 1201-1659, and 'evening' at other times
        """
        pass

    def greet(self, store: str):
        """
        Given the name of the store, print a certain greeting using private methods
        """

        '''
        Hi, welcome to <store>!
        How's your <day> <part of day>?
        Here's a cupon for 20% off!
        '''

STORE_NAME = 'Mallmart'
a_greeter = Greeter()
a_greeter.greet(store=STORE_NAME)