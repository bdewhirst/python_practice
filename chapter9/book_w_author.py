import warnings


class Author:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]

    @property
    def for_display(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def for_citation(self):
        return f"{self.last_name} {self.first_name[0]}"


class Book:
    def __init__(self, data):
        self.title = data["title"]
        self.subtitle = data["subtitle"]
        self.author_data = data["author"]
        self.author = Author(self.author_data)

    @property
    def author_for_display(self):
        warnings.warn("In the future, call Book.author.for_display", DeprecationWarning)
        return self.author.for_display

    @property
    def author_for_citation(self):
        warnings.warn(
            "In the future, call Book.author.for_citation", DeprecationWarning
        )
        return self.author.for_citation

    @property
    def display_title(self):
        if self.title and self.subtitle:
            return f"{self.title}: {self.subtitle}"
        elif self.title:
            return self.title
        else:
            return "Untitled"


book = Book(
    {
        "title": "Brillo-iant",
        "subtitle": "The pad that changed everything",
        "author": {
            "first_name": "Rusty",
            "last_name": "Potts",
        },
    }
)
print(book.display_title)
print(book.author_for_display)
print(book.author_for_citation)
print(book.author.for_display)
print(book.author.for_citation)
