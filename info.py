import sqlite3

if __name__ == "__main__":
    database = sqlite3.connect("database/database.db")
    cursor = database.cursor()
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    print(f"we have {len(users)-3} users")
