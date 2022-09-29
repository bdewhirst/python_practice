import sys
import datetime as dt

import requests

import database_manager


db = database_manager.DatabaseManager(database_filename="bookmarks.db")


class CreateBookmarksTableCommand:
    """
    Create database table with loose coupling and separation of concerns
    """

    def execute(self):
        cols = {
            "id": "integer primary key autoincrement",
            "title": "text not null",
            "url": "text not null",
            "notes": "text",
            "date_added": "text not null",
        }
        db.create_table(
            table_name="bookmarks",
            columns=cols,
        )


class AddBookmarkCommand:
    """
    Update database table with loose coupling and separation of concerns
    """

    def execute(self, bookmark_data, timestamp=None):
        bookmark_data["date_added"] = timestamp or dt.datetime.utcnow().isoformat()
        db.add(table_name="bookmarks", data=bookmark_data)
        return "Bookmark added!"


class ListBookmarksCommand:
    """
    Retrieve stored bookmarks
    """

    def __init__(self, order_by="date_added"):
        self.order_by = order_by

    def execute(self):
        return db.select("bookmarks", order_by=self.order_by).fetchall()


class DeleteBookmarkCommand:
    """
    Remove bookmark
    """

    def execute(self, id_to_remove):
        db.delete("bookmarks", {"id": id_to_remove})
        return "Bookmark deleted!"


class GetGithubStarsCommand:
    """
    Retrieve information from github API and save as a bookmark
    """

    def execute(self, github_data):
        github_username = github_data["github_username"]
        target_url = f"https://api.github.com/users/{github_username}/starred"
        responses = requests.get(target_url).json()
        # starred_urls = []
        for star in responses:
            print(star["full_name"])
            # starred_urls.append(star)
        print(responses)

        # notes:
        """
        1. get initial page of star results f'https://api.github.com/users/{github_username}/starred'
        2. parse data from response and use to execute AddBookmarkCommand for each starred repository
        3. get the link: <...>; rel=next header, if present
        4. repeat for the next page if there is one, otherwise stop

        n.b.: to get timestamps, you have to pass 'Accept: application/vnd.github.v3.star+json' header
        """


class QuitCommand:
    """
    Quit out of the program
    """

    def execute(self):
        sys.exit()


# Business logic layer
