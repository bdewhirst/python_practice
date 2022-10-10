import os
from collections import OrderedDict

import commands


def print_bookmarks(bookmarks):
    for bookmark in bookmarks:
        print("\t".join(str(field) if field else "" for field in bookmark))


class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name
        self.command = command
        self.prep_call = prep_call

    def _handle_message(self, message):
        if isinstance(message, list):
            print_bookmarks(message)
        else:
            print(message)

    def choose(self):
        data = self.prep_call() if self.prep_call else None
        status, result = self.command.execute(data)
        self._handle_message(result)

    def __str__(self):
        return self.name


def print_options(options):
    """
    Displays the supported options and the shortcut
    """
    for shortcut, option in options.items():
        print(f"({shortcut}) {option}")
    print()


def option_choice_is_valid(choice, options):
    """
    Checks if selected choice is a valid option
    """
    return choice in options or choice.upper() in options


def get_option_choice(options):
    """
    Prompt user to make a choice until they quit out
    """
    choice = input("Choose an option: ")
    while not option_choice_is_valid(choice=choice, options=options):
        print("Invalid choice")
        choice = input("Choose an option: ")
    return options[choice.upper()]


def get_user_input(label, required=True):
    value = input(f"{label}: ") or None
    while required and not value:
        value = input(f"{label}: ") or None
    return value


def get_new_bookmark_data():
    return {
        "title": get_user_input(label="Title"),
        "url": get_user_input(label="URL"),
        "notes": get_user_input(label="Notes", required=False),
    }


def get_bookmark_id_for_deletion():
    return get_user_input("Enter a bookmark ID to delete")


def get_github_data():
    return {
        "github_username": get_user_input(label="Github User"),
        "preserve_gh_ts": get_user_input(
            label="Preserve Github Timestamp? (Y/N)",
            required=False,
        ),
    }


def clear_screen():
    """
    Clear the screen before re-printing the menu
    """
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)


def loop():
    clear_screen()
    print("Welcome to Bark, the bookmarking widget!")

    options = OrderedDict(
        {
            "A": Option(
                name="Add a bookmark",
                command=commands.AddBookmarkCommand(),
                prep_call=get_new_bookmark_data,
            ),
            "B": Option(
                name="List bookmarks by date",
                command=commands.ListBookmarksCommand(),
            ),
            "T": Option(
                name="List bookmarks by title",
                command=commands.ListBookmarksCommand(order_by="title"),
            ),
            "D": Option(
                name="Delete a bookmark",
                command=commands.DeleteBookmarkCommand(),
                prep_call=get_bookmark_id_for_deletion,
            ),
            "G": Option(
                name="Import github stars",
                command=commands.GetGithubStarsCommand(),
                prep_call=get_github_data,
            ),
            "Q": Option(name="Quit", command=commands.QuitCommand()),
        }
    )
    print_options(options)
    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()

    _ = input("Press Enter to return to menu")


if __name__ == "__main__":
    while True:
        loop()
