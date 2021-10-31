from hashlib import new
import sqlite3
from key import new_id

from calendar import timegm
from time import gmtime

def time_stamp() -> int:
    return timegm(gmtime())


class Session:
    def __init__(self):
        self.conn = sqlite3.connect("database/session.db")
        self.cursor = self.conn.cursor()

    def new_session(self, user, id):
        ex_time = time_stamp() + 3600
        session_id = new_id()

        self.cursor.execute(f" INSERT INTO User(id,expir_time,session_id) VALUES({id},{ex_time},{session_id}) ")
        self.conn.commit()

        return session_id

    def extend(self, session_id):
        expir_time = self.cursor.execute(f" SELECT * FROM User WHERE session_id = {session_id}")[3]
        expir_time += 60 * 30
        self.cursor.execute(f" UPDATE User SET expir_time = {expir_time} WHERE session_id = {session_id}")
        self.conn.commit()

        return expir_time

    def find(self, session_id):
        self.cursor.execute(f" SELECT * FROM User WHERE session_id = '{session_id}' ")
        user = self.cursor.fetchone()

        if user == None:
            return ()
        elif user[1] < time_stamp():
            return ()
        return user

if __name__ == "__main__":
    session = Session()
    print("-----------Classto Session Database-----------")
    session.conn.execute(''' CREATE TABLE "User" (
	    "id"	INTEGER,
	    "expir_time"	INTEGER,
	    "session_id"	INTEGER,
	    PRIMARY KEY("session_id")
    ) ''')
    print("initialized session database")