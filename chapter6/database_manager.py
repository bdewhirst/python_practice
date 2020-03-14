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

    def add(self, table_name: str, data: dict):
        """
        Programmatically add data to a database table
        """
        placeholders: list = ", ".join("?" * len(data))
        column_names: list = ", ".join(data.keys())
        column_values: list = tuple(data.values())

        self._execute(
            statement=f"""
            INSERT INTO {table_name}
            {(column_names)}
            VALUES ({placeholders});
            """,
            values=column_values,
        )

    def delete(self, table_name: str, criteria: dict):
        """
        Programmatically delete data as specified by critera
        """
        placeholders: list = [f"{column} = ?" for column in criteria.keys()]
        delete_criteria = " AND ".join(placeholders)
        self._execute(
            statement=f"""
            DELETE FROM {table_name}
            WHERE {delete_criteria};
            """,
        )

    def select(self, table_name: str, criteria: dict = {}, order_by: dict = {}) -> list:
        """
        Programmatically retrieve data from database and return it as a list
        """
        query: str = f"SELECT * FROM {table_name}"

        if criteria:
            placeholders: list = [f"{column} = ?" for column in criteria.keys()]
            select_criteria: str = " AND ".join(placeholders)
            query += f" WHERE {select_criteria}"

        if order_by:
            query += f" ORDER BY {order_by}"

        result = self._execute(statement=query, value=tuple(criteria.values()),)
        return result

# Persistence layer
