import sqlite3
import time

def db_datetime() -> str:
    return time.strftime('%m/%d/%Y, %H:%M:%S')

class DataBase:

    def __init__(self,db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

        self.startup = [
        '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id INTEGER,
                name TEXT NULL,
                surname TEXT NULL,
                phone TEXT NULL,
                level TEXT NULL,
                is_fully_joined BOOLEAN,
                joined_datetime TEXT)
        '''
        ]

        for i in self.startup:
            self.cursor.execute(i)

    def add_user(self, tg_id):
        with self.connection:
            sql = '''
                INSERT INTO users (tg_id, is_fully_joined, joined_datetime)
                VALUES ({}, {}, "{}")'''.format(tg_id, False, db_datetime())
            return self.cursor.execute(sql)

    def user_exists(self, tg_id):
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM users WHERE tg_id = {tg_id}").fetchall()

            return bool(len(result))

    def set_name(self, tg_id, name):
        with self.connection:
            return self.cursor.execute(f'UPDATE users SET name="{name}" WHERE tg_id={tg_id}')

    def set_surname(self, tg_id, surname):
        with self.connection:
            return self.cursor.execute(f'UPDATE users SET surname="{surname}" WHERE tg_id={tg_id}')

    def set_phone(self, tg_id, phone):
        with self.connection:
            return self.cursor.execute(f'UPDATE users SET phone="{phone}" WHERE tg_id={tg_id}')

    def set_level(self, tg_id, lvl):
        with self.connection:
            return self.cursor.execute(f'UPDATE users SET level="{lvl}" WHERE tg_id={tg_id}')

    def joined(self, tg_id):
        with self.connection:
            return self.cursor.execute(f"UPDATE users SET is_fully_joined=True WHERE tg_id={tg_id}")

    def is_joined(self, tg_id):
        with self.connection:
            result = self.cursor.execute(f"SELECT is_fully_joined FROM users WHERE tg_id={tg_id} ").fetchall()
            if result[0] == True:
                return True
            else:
                return False

    def get_name(self, tg_id):
        with self.connection:
            result = self.cursor.execute(f'SELECT name FROM users WHERE tg_id={tg_id}').fetchall()
            return result[0][0]

    def get_surname(self, tg_id):
        with self.connection:
            result = self.cursor.execute(f'SELECT surname FROM users WHERE tg_id={tg_id}').fetchall()
            return result[0][0]

    def get_phone(self,tg_id):
        with self.connection:
            result = self.cursor.execute(f"SELECT phone FROM users WHERE tg_id = {tg_id}" ).fetchall()
            return result[0][0]

    def get_level(self,tg_id):
        with self.connection:
            result = self.cursor.execute(f"SELECT level FROM users WHERE tg_id = {tg_id}").fetchall()
            return result[0][0]

    def get_all_users(self):
        with self.connection:
            result = self.cursor.execute('SELECT tg_id FROM users').fetchall()
            return result
