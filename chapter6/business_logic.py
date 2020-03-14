import datetime as dt

import database_manager


db = database_manager.DatabaseManager(database_filename="bookmarks.db")


class CreateBookmarksTableCommand:
    """
    Creates database table with loose coupling and separation of concerns
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
    def execute(self, bookmark_data: dict) -> str:
        """
        Update database table with loose coupling and separation of concerns
        """
        bookmark_data['date_added'] = dt.datetime.utcnow().isoformat()
        db.add(table_name='bookmarks', data=bookmark_data)
        return 'Bookmark added!'
