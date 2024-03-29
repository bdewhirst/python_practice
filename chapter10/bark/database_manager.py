import sqlite3


class DatabaseManager:
    def __init__(self, database_filename):
        """
        Creates a SQLite connection at the specified location
        """
        self.connection = sqlite3.connect(database=database_filename)

    def __del__(self):
        """
        Closes the database connection
        """
        self.connection.close()

    def _execute(self, statement, values=None):
        """
        Creates a cursor to run the query specified by statement and returns the result as a list
        """
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, values or [])
            return cursor

    def create_table(self, table_name, columns):
        """
        Programmatically create a table, which returns an empty list
        """
        columns_with_types = [
            f"{column_name} {data_type}" for column_name, data_type in columns.items()
        ]
        self._execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name}
            ({', '.join(columns_with_types)});
            """
        )

    def add(self, table_name, data):
        """
        Programmatically add data to a database table
        """
        placeholders = ", ".join("?" * len(data))
        column_names = ", ".join(data.keys())
        column_values = tuple(data.values())

        self._execute(
            f"""
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders});
            """,
            column_values,
        )

    def delete(self, table_name, criteria):
        """
        Programmatically delete data as specified by critera
        """
        placeholders = [f"{column} = ?" for column in criteria.keys()]
        delete_criteria = " AND ".join(placeholders)
        self._execute(
            f"""
            DELETE FROM {table_name}
            WHERE {delete_criteria};
            """,
            tuple(criteria.values()),
        )

    def select(self, table_name, criteria=None, order_by=None):
        """
        Programmatically retrieve data from database and return it as a list
        """
        criteria = criteria or {}

        query = f"SELECT * FROM {table_name}"

        if criteria:
            placeholders = [f"{column} = ?" for column in criteria.keys()]
            select_criteria = " AND ".join(placeholders)
            query += f" WHERE {select_criteria}"

        if order_by:
            query += f" ORDER BY {order_by}"

        result = self._execute(
            query,
            tuple(criteria.values()),
        )
        return result

    def update(self, table_name, criteria, data):
        update_placeholders = [f"{column} = ?" for column in criteria.keys()]
        update_criteria = " AND ".join(update_placeholders)

        data_placeholders = ", ".join(f"{key} = ?" for key in data.keys())

        values = tuple(data.values()) + tuple(criteria.values())

        self._execute(
            f"""
            UPDATE {table_name}
            SET {data_placeholders}
            WHERE {update_criteria};
            """,
            values,
        )
