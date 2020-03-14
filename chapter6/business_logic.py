import sys

import datetime as dt

import database_manager


db = database_manager.DatabaseManager(database_filename="bookmarks.db")


class CreateBookmarksTableCommand:
    """
    Create database table with loose coupling and separation of concerns
    """
    def execute(self) -> None:
        cols = {
            "id": "integer primary key autoincrement",
            "title": "text not null",
            "url": "text not null",
            "notes": "text",
            "date_added": "text not null",
        }
        db.create_table(table_name="bookmarks", columns=cols,)


class AddBookmarkCommand(self, bookmark_data):
    """
    Update database table with loose coupling and separation of concerns
    """
    def execute(self, bookmark_data=bookmark_data) -> str:
        bookmark_data['date_added'] = dt.datetime.utcnow().isoformat()
        db.add(table_name='bookmarks', data=bookmark_data)
        return 'Bookmark added!'


class ListBookmarksCommand:
    """
    Retrieve stored bookmarks
    """
    def __init__(self, order_by='date_added'):
        self.order_by = order_by

    def execute(self):
        return db.select('bookmarks', order_by=self.order_by).fetchall()


class DeleteBookmarkCommand:
    """
    Remove bookmark
    """
    def execute(self, id_to_remove) -> str:
        db.delete('bookmarks', {'id': id_to_remove})
        return 'Bookmark deleted!'

class QuitCommand:
    """
    Quit out of the program
    """
    def execute(self):
        sys.exit()