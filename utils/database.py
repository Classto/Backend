from hashlib import new
import sqlite3
from utils import new_id, to_hash

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database/database.db")
        self.cursor = self.conn.cursor()

    def register(self, user):
        id = new_id()
        email = to_hash(user.email)
        pw = to_hash(user.pw)

        self.cursor.execute(f" INSERT INTO User(id,email,pw,current_category) VALUES({id},{email},{pw},{user.current_category}) ")
        self.conn.commit()

    def exits(self, email):
        email = to_hash(email)
        self.cursor.execute(f" SELECT count(*) FROM User WHERE email = '{email}' ")

        if self.cursor.fetchone()[0] == 0:
            return False
        return True

if __name__ == "__main__":
    database = Database()
    database.exits("asdf")
