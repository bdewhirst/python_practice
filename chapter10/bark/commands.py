import sys
import datetime as dt
from abc import ABC, abstractmethod

import requests

import persistance_layer


p_layer = persistance_layer.BookmarkDatabase()


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError()


class AddBookmarkCommand(Command):
    """
    Update database table with loose coupling and separation of concerns
    """

    def execute(self, data, timestamp=None):
        data["date_added"] = timestamp or dt.datetime.utcnow().isoformat()
        p_layer.create(data=data)
        return True, "Bookmark added!"


class ListBookmarksCommand(Command):
    """
    Retrieve stored bookmarks
    """

    def __init__(self, order_by="date_added"):
        self.order_by = order_by

    def execute(self, data=None):
        return True, p_layer.list(order_by=self.order_by)


class DeleteBookmarkCommand(Command):
    """
    Remove bookmark
    """

    def execute(self, data):
        p_layer.delete({"id": data})
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
