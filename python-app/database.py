import sqlite3
from typing import Any, Dict, List, Optional


class DatabaseConnection:
    def __init__(self, db_path: str = ':memory:'):
        self.db_path = db_path
        self.connection: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None

    def connect(self) -> bool:
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            return True
        except sqlite3.Error:
            return False

    def disconnect(self) -> bool:
        try:
            if self.connection:
                self.connection.close()
                self.connection = None
                self.cursor = None
                return True
            return False
        except sqlite3.Error:
            return False

    def is_connected(self) -> bool:
        if not self.connection or not self.cursor:
            return False
        try:
            self.cursor.execute('SELECT 1')
            return True
        except sqlite3.Error:
            return False

    def create_table(self, table_name: str, columns: Dict[str, str]) -> bool:
        if not self.is_connected():
            return False
        columns_sql = ', '.join([f'{name} {type_}' for name, type_ in columns.items()])
        try:
            self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})')
            self.connection.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_data(self, table_name: str, data: Dict[str, Any]) -> bool:
        if not self.is_connected():
            return False
        columns = ', '.join(data.keys())
        placeholders = ', '.join('?' for _ in data)
        try:
            self.cursor.execute(f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})', tuple(data.values()))
            self.connection.commit()
            return True
        except sqlite3.Error:
            return False

    def query(self, sql: str, params: tuple = ()) -> Optional[List[Dict[str, Any]]]:
        if not self.is_connected():
            return None
        try:
            self.cursor.execute(sql, params)
            rows = self.cursor.fetchall()
            columns = [description[0] for description in self.cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        except sqlite3.Error:
            return None
