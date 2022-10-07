import sys
import datetime as dt
from abc import ABC, abstractmethod

import requests

import database_manager


db = database_manager.DatabaseManager(database_filename="bookmarks.db")


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError()


class CreateBookmarksTableCommand(Command):
    """
    Create database table with loose coupling and separation of concerns
    """

    def execute(self, data=None):
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


class AddBookmarkCommand(Command):
    """
    Update database table with loose coupling and separation of concerns
    """

    def execute(self, data, timestamp=None):
        data["date_added"] = timestamp or dt.datetime.utcnow().isoformat()
        db.add(table_name="bookmarks", data=data)
        return True, "Bookmark added!"


class ListBookmarksCommand(Command):
    """
    Retrieve stored bookmarks
    """

    def __init__(self, order_by="date_added"):
        self.order_by = order_by

    def execute(self, data=None):
        return True, db.select("bookmarks", order_by=self.order_by).fetchall()


class DeleteBookmarkCommand(Command):
    """
    Remove bookmark
    """

    def execute(self, data):
        db.delete("bookmarks", {"id": data})
        return True, "Bookmark deleted!"


class GetGithubStarsCommand(Command):
    """
    Retrieve information from github API and save as a bookmark
    """

    def _extract_bookmark_info(self, repo):
        return {
            "title": repo["name"],
            "url": repo["html_url"],
            "notes": repo["description"],
        }

    def execute(
        self,
        data,
    ):

        github_username = data["github_username"]
        target_url = f"https://api.github.com/users/{github_username}/starred"
        # passing the header changes more behavior than just adding a value
        headers = {
            "Accept": "application/vnd.github.v3.star+json",
        }
        responses = requests.get(target_url, headers=headers).json()

        for repo_info in responses:
            # necessary to both follow my implementation and to use above header
            star = repo_info["repo"]
            if data["preserve_gh_ts"].upper() == "Y":
                timestamp = dt.datetime.strptime(
                    repo_info["starred_at"], "%Y-%m-%dT%H:%M:%SZ"
                )
            else:
                timestamp = None

            AddBookmarkCommand.execute(
                self,
                data=self._extract_bookmark_info(repo=star),
                timestamp=timestamp,
            )
        return True, "Imported github bookmarks!"


class QuitCommand(Command):
    """
    Quit out of the program
    """

    def execute(self, data=None):
        sys.exit()
