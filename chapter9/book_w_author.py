class Book:
    def __init__(self, data):
        self.title = data["title"]
        self.subtitle = data["subtitle"]
        self.author_data = data["author"]

    @property
    def author_for_display(self):
        return f"{self.author_data['first_name']} {self.author_data['last_name']}"

    @property
    def author_for_citation(self):
        return f"{self.author_data['last_name']} {self.author_data['first_name'][0]}."

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
