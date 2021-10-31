import sqlite3
from key import new_id, to_hash

import json

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database/database.db")
        self.cursor = self.conn.cursor()

        self.SCHEDULE = "Meetings"
        self.CATEGRY = "Category"

    def register(self, user) -> int:
        id = new_id()
        email = to_hash(user.email)
        pw = to_hash(user.pw)
        meetings = json.dumps(
            {
                "example": [
                    {
                        "name": "Example Meeting",
                        "time": "00:00",
                        "link": "meeting link",
                        "nickname": "nickname",
                        "id": 11111111111,
                        "password": 1,
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

    def info(self, id) -> dict:
        self.cursor.execute(f" SELECT * FROM User WHERE id = '{id}'")
        data = self.cursor.fetchone()
        data = {
            "id" : data[3],
            "email" : data[0],
            "current_category" : data[2]
        }
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

    def search(self, id, table: str) -> dict:
        self.cursor.execute(f" SELECT * FROM {table} WHERE id = '{id}'")
        data = self.cursor.fetchone()[1]

        return json.loads(data)

    def edit(self, id, table: str, data: dict) -> str:
        data = json.dumps(data)
        self.cursor.execute(f"UPDATE {table} SET {table.lower()} = '{data}' WHERE id = {id}")
        self.conn.commit()

        return data

if __name__ == "__main__":
    database = Database()
    print("-----------Classto Database-----------")
    database.cursor.execute(''' CREATE TABLE "User" (
	    "email"	TEXT,
	    "pw"	TEXT,
	    "current_category"	TEXT,
	    "id"	INTEGER,
	    PRIMARY KEY("id")
    ) ''')
    print("created User table")
    database.cursor.execute(''' CREATE TABLE "Meetings" (
	    "id"	INTEGER,
	    "meetings"	TEXT,
	    PRIMARY KEY("id")
    ) ''')
    print("created Meetings table")
    database.cursor.execute(''' CREATE TABLE "Category" ( 
    	"id"	INTEGER,
	    "category"	TEXT,
	    PRIMARY KEY("id")
    ) ''')
    print("created Category table")
    database.conn.commit()

    print("initialized main database")
