import mysql.connector

def sqlManager():
    mydb = None
    cursor = None

    def __init__(self,user,passwd,database):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user=user,
            passwd=passwd,
            database=database
        )
        self.cursor = self.mydb.cursor()

    def returnCurrency(self,user,server):
        query = "SELECT money FROM players WHERE name = '{user}' AND server = '{server}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()[0]
