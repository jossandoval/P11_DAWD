import os
import tempfile
import unittest
from database import DatabaseConnection


class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        self.temp_file.close()
        self.db = DatabaseConnection(self.temp_file.name)

    def tearDown(self):
        if self.db.connection:
            self.db.disconnect()
        try:
            os.unlink(self.temp_file.name)
        except FileNotFoundError:
            pass

    def test_connect_successful(self):
        connected = self.db.connect()
        self.assertTrue(connected)
        self.assertTrue(self.db.is_connected())

    def test_disconnect_successful(self):
        self.db.connect()
        disconnected = self.db.disconnect()
        self.assertTrue(disconnected)
        self.assertFalse(self.db.is_connected())

    def test_create_table(self):
        self.db.connect()
        created = self.db.create_table('users', {
            'id': 'INTEGER PRIMARY KEY',
            'name': 'TEXT NOT NULL',
            'email': 'TEXT UNIQUE'
        })
        self.assertTrue(created)

    def test_insert_data(self):
        self.db.connect()
        self.db.create_table('users', {
            'id': 'INTEGER PRIMARY KEY',
            'name': 'TEXT NOT NULL'
        })
        inserted = self.db.insert_data('users', {'name': 'Juan'})
        self.assertTrue(inserted)

    def test_query_data(self):
        self.db.connect()
        self.db.create_table('users', {
            'id': 'INTEGER PRIMARY KEY',
            'name': 'TEXT NOT NULL'
        })
        self.db.insert_data('users', {'name': 'Juan'})
        results = self.db.query('SELECT * FROM users WHERE name = ?', ('Juan',))
        self.assertIsNotNone(results)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], 'Juan')

    def test_query_without_connection_returns_none(self):
        results = self.db.query('SELECT * FROM users')
        self.assertIsNone(results)

    def test_insert_without_connection_returns_false(self):
        inserted = self.db.insert_data('users', {'name': 'Juan'})
        self.assertFalse(inserted)


if __name__ == '__main__':
    unittest.main(verbosity=2)
