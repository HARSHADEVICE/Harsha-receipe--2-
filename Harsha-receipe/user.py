import sqlite3 as sql


username = "Vish101"
password = "SanDiego"
con = sql.connect("users.db")
cur = con.cursor()
statement = f"SELECT LoginId from users WHERE LoginID='{username}' AND Password = '{password}';"
cur.execute(statement)
if not cur.fetchone():  # An empty result evaluates to False.
    print("Login failed")
else:
    print("Welcome")