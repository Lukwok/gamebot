from os import system
import sqlite3
from sqlite3.dbapi2 import Cursor

#using mongodb
from pymongo import MongoClient
from pprint import pprint
import certifi

class MongoDBHelper:
    def __init__(self):
        self.client = MongoClient("YOUR_MONGO_DB_URL", tlsCAFile=certifi.where())
        self.db = self.client.todo

    def setup(self):
        print ("done")

    def add_user(self, updater, gameName,id):
        query = {"updater":str(updater),"gameName":str(gameName),"id":str(id)}
        self.db.joinList.insert(query)
    
    def delete_user(self,gameName):
        query = {"gameName":str(gameName)}
        self.db.joinList.delete_one(query)

    def delete_by_id(self,gameName,id):
        query = {"gameName":str(gameName),"id":str(id)}
        self.db.joinList.delete_one(query)

    def show_user(self):
        data = list(self.db.joinList.find())
        return data

    def remove_db(self):
        self.db.joinList.remove()

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

    def delete_user(self, gameName):
        query = "DELETE FROM joinList WHERE gameName = (?) "
        args = (gameName,)
        self.conn.execute(query,args)
        self.conn.commit()

    def delete_user_by_id(self, gameName,id):
        query = "DELETE FROM joinList WHERE gameName = (?) AND id = (?)"
        args = (gameName,id,)
        self.conn.execute(query, args)
        self.conn.commit()

    def show_user(self):
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
