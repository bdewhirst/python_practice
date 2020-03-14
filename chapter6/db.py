import sqlite3
import pathlib


class DatabaseManager:
    def __init__(self, database_filename: pathlib.Path()):
        """
        Creates a SQLite connection at the specified location
        """
        self.connection = sqlite3.connect(database=database_filename)

    def __del__(self):
        """
        Closes the database connection
        """
        self.connection.close()

    def _execute(self, statement: str, values: list = []) -> list:
        """
        Creates a cursor to run the query specified by statement and returns the result as a list
        """
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, values)
            return cursor

    def create_table(self, table_name: str, columns: list) -> dict:
        """
        Programmatically create a table, which returns an empty list
        """
        columns_with_types = [f"{column_name} {data_type}" for column_name, data_type in columns.items()]
        self._execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name}
            ({', '.join(columns_with_types)});
            """
        )
