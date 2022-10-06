class Book:
    def __init__(self, data):
        self.title = data["title"]
        self.subtitle = data["subtitle"]

        if self.title and self.subtitle:
            self.display_title = f"{self.title}: {self.subtitle}"
        elif self.title:
            self.display_title = self.title
        else:
            self.display_title = "Untitled"
