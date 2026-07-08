import mysql.connector

class Database:

    def connect(self):

        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tanyasingh@1234",
            database="garage_db1"
        )
        return con 

