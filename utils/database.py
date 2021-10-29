import sqlite3
from key import new_id, to_hash

import json

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database/database.db")
        self.cursor = self.conn.cursor()

    def register(self, user) -> int:
        id = new_id()
        email = to_hash(user.email)
        pw = to_hash(user.pw)
        meetings = json.dumps(
            {
                "sample": [
                    { 
                        "name": "sample meeting",
                        "time": "12:59",
                        "link": "meeting link",
                        "id": 1234,
                        "password": 1234,
                        "repeating-days" : [] 
                    }, 
                    {
                        "name": "meet",
                        "time": "00:00", 
                        "link": "link", 
                        "id":1, 
                        "password": 1234, 
                        "repeating-days" : [] 
                    } 
                ] 
            }
        )

        self.cursor.execute(f" INSERT INTO User(id,email,pw,current_category) VALUES({id},'{email}','{pw}','sample') ")
        self.cursor.execute(f''' INSERT INTO Category(id,category) VALUES({id}, '["category"]') ''')
        self.cursor.execute(f''' INSERT INTO Meetings(id,meetings) VALUES({id}, '{meetings}') ''')
        self.conn.commit()

        return id

    def info(self, id) -> tuple:
        self.cursor.execute(f" SELECT * FROM User WHERE id = '{id}'")
        data  = self.cursor.fetchone()

        return data

    def get_id(self, email) -> int:
        email = to_hash(email)

        self.cursor.execute(f" SELECT * FROM User WHERE email = '{email}'")
        id = self.cursor.fetchone()[3]

        return id

    def exits(self, email) -> bool:
        email = to_hash(email)
        self.cursor.execute(f" SELECT count(*) FROM User WHERE email = '{email}' ")

        if self.cursor.fetchone()[0] == 0:
            return False
        return True

    def category(self, id) -> dict:
        self.cursor.execute(f" SELECT * FROM Category WHERE id = '{id}'")
        data = self.cursor.fetchone()[1]

        return json.loads(data)


if __name__ == "__main__":
    database = Database()
    database.exits("asdf")
