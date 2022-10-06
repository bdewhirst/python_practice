class Book:
    def __init__(self, data):
        self.title = data["title"]
        self.subtitle = data["subtitle"]

    @property
    def display_title(self):
        if self.title and self.subtitle:
            return f"{self.title}: {self.subtitle}"
        elif self.title:
            return self.title
        else:
            return "Untitled"


d_tests = [
    {"title": "Dune", "subtitle": None},
    {
        "title": "Doctor Strangelove",
        "subtitle": "How I learned to stop worrying and love the Bomb",
    },
    {"title": None, "subtitle": None},
]

for d_test in d_tests:
    book = Book(data=d_test)
    print(book.display_title)
