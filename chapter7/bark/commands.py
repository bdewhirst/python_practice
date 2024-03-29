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

    def _extract_bookmark_info(self, repo):
        return {
            "title": repo["name"],
            "url": repo["html_url"],
            "notes": repo["description"],
        }

    def execute(
        self,
        github_data,
    ):

        github_username = github_data["github_username"]
        target_url = f"https://api.github.com/users/{github_username}/starred"
        headers = {
            "Accept": "application/vnd.github.v3.star+json",
        }  # passing the header changes more behavior than just adding a value
        responses = requests.get(target_url, headers=headers).json()

        for repo_info in responses:
            star = repo_info[
                "repo"
            ]  # necessary to both follow my implementation and to use above header
            if github_data["preserve_gh_ts"].upper() == "Y":
                timestamp = dt.datetime.strptime(
                    repo_info["starred_at"], "%Y-%m-%dT%H:%M:%SZ"
                )
            else:
                timestamp = None

            AddBookmarkCommand.execute(
                self,
                bookmark_data=self._extract_bookmark_info(repo=star),
                timestamp=timestamp,
            )


class QuitCommand:
    """
    Quit out of the program
    """

    def execute(self):
        sys.exit()


# Business logic layer
