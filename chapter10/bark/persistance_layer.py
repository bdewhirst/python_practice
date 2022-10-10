from abc import ABC, abstractmethod

from database_manager import DatabaseManager


class PersistanceLayer(ABC):
    @abstractmethod
    def create(self, data):
        raise NotImplementedError("Persistence layers must implement a create method")

    @abstractmethod
    def list(self, order_by):
        raise NotImplementedError("Persistence layers must implement a list method")

    @abstractmethod
    def edit(self, bookmark_id, bookmark_data):
        raise NotImplementedError("Persistence layers must implement an edit method")

    @abstractmethod
    def delete(self, bookmark_id):
        raise NotImplementedError("Persistence layers must implement a delete method")


class BookmarkDatabase(PersistanceLayer):
    def __init__(self):
        """
        Create database table with loose coupling and separation of concerns

        Database is a specific implementation of what might otherwise be a web API using POST/GET/PUSH/DELETE
        """
        self.table_name = "bookmarks"
        self.cols = {
                "id": "integer primary key autoincrement",
                "title": "text not null",
                "url": "text not null",
                "notes": "text",
                "date_added": "text not null",
            }

        self.db = DatabaseManager("bookmarks.db")
        self.db.create_table(self.table_name, self.cols)

    def create(self, data):
        self.db.add(self.table_name, data)

    def list(self, order_by):
        self.db.select(self.table_name, order_by=order_by)

    def edit(self, bookmark_id, bookmark_data):
        self.db.update(self.table_name, bookmark_id, bookmark_data)

    def delete(self, bookmark_id):
        self.db.delete(self.table_name, bookmark_id)
