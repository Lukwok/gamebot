from os import system
import sqlite3
from sqlite3.dbapi2 import Cursor


class DBHelper:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname,check_same_thread=False)

    def setup(self):
        query = "CREATE TABLE IF NOT EXISTS joinList (updater text, gameName text, id text)"
        self.conn.execute(query)
        self.conn.commit()
        print("done")

    def add_user(self, updater, gameName, id):
        query = "INSERT INTO joinList VALUES (?,?,?)"
        args = (updater, gameName, id)
        self.conn.execute(query, args)
        self.conn.commit()

    def delete_item(self, gameName):
        query = "DELETE FROM joinList WHERE gameName = (?) "
        args = (gameName,)
        self.conn.execute(query,args)
        self.conn.commit()

    def delete_user_by_id(self, gameName,id):
        query = "DELETE FROM joinList WHERE gameName = (?) AND id = (?)"
        args = (gameName,id,)
        self.conn.execute(query, args)
        self.conn.commit()

    def get_items(self):
        cusor = self.conn.cursor()
        query = "SELECT * FROM joinList"
        cusor.execute(query)
        data = cusor.fetchall()
        cusor.close()
        self.conn.commit()
        return data

    def remove_db(self):
        query = "DROP TABLE IF EXISTS joinList"
        self.conn.execute(query)
        self.conn.commit() 
        print ("done")