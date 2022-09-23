import os

import commands


class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name
        self.command = command
        self.prep_call = prep_call

        def choose(self):
            data = self.prep_call() if self.prep_call else None
            message = self.command.execute(data) if data else self.command.execute()
            print(message)

        def __str__(self):
            return self.name


def print_options(options):
    """
    Displays the supported options and the shortcut
    """
    for shortcut, option in options.items():
        print(f"({shortcut}) {option}")
        print()


def option_choice_is_valid(choice, options: str):
    """
    Checks if selected choice is a valid option
    """
    return choice in options or choice.upper() in options


def get_option_choice(options: str):
    """
    Prompt user to make a choice until they quit out
    """
    choice = input("Choose an option: ")
    while not option_choice_is_valid(choice=choice, options=options):
        print("Invalid choice")
        choice = input("Choose an option: ")
    return options[choice.upper()]


def get_user_input(label, required: bool = True):
    value = input(f"{label}: ") or None
    while required and not value:
        value = input(f"{label}: ") or None
    return value


def get_new_bookmark_data() -> dict:
    return {
        "title": get_user_input(label="Title"),
        "url": get_user_input(label="URL"),
        "notes": get_user_input(label="Notes", required=False),
    }


def get_bookmark_id_for_deletion():
    return get_user_input("Enter a bookmark ID to delete")


def clear_screen():
    """
    Clear the screen before re-printing the menu
    """
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)


def loop():
    main()
    _ = input("Press Enter to return to menu")


def main():
    """ """
    print("Welcome to bookmarking widget!")
    commands.CreateBookmarksTableCommand().execute()

    options = {
        "A": Option("Add a bookmark", commands.AddBookmarkCommand()),
        "B": Option("List bookmars by date", commands.ListBookmarksCommand()),
        "T": Option(
            "List bookmarks by title", commands.ListBookmarksCommand(order_by="title")
        ),
        "D": Option("Delete a bookmark", commands.DeleteBookmarkCommand()),
        "Q": Option("Quit", commands.QuitCommand()),
    }
    clear_screen()
    print_options(options)
    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()


if __name__ == "__main__":

    # This is the presentation layer
    while True:
        loop()
