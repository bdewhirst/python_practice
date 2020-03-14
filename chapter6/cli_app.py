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


if __name__ == "__main__":
    print("Welcome to bookmarking widget!")
    commands.CreateBookmarksTableCommand().execute()

    options = {
        "A": Option("Add a bookmark", commands.AddBookmarkCommand()),
        "B": Option("List bookmars by date", commands.ListBookmarksCommand()),
        "T": Option("List bookmarks by title", commands.ListBookmarksCommand(order_by="title")),
        "D": Option("Delete a bookmark", commands.DeleteBookmarkCommand()),
        "Q": Option("Quit", commands.QuitCommand()),
    }
    print_options(options)

# This is the presentation layer
