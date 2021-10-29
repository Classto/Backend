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

        self.cursor.execute(f" INSERT INTO User(id,email,pw,expir_time,session_id) VALUES({id},'{user.email}','{user.pw}',{ex_time},{session_id}) ")
        self.conn.commit()

        return session_id

    def find(self, session_id):
        self.cursor.execute(f" SELECT * FROM User WHERE session_id = '{session_id}' ")
        user = self.cursor.fetchone()

        if not user == () and user[3] > time_stamp():
            return ()
        return user
