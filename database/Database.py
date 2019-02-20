import sqlite3

class Database():

    """
    Class responisble for connection with SQLite database.

    Atributes:
    --------------
    __databaseFile : str - path to file with database.

    Methods:
    --------------
    connect() - connects with database
    """

    def __init__(self):
        self.__databaseFile = 'database/database.db'

    def connect(self):
        try:
            return sqlite3.connect(self.__databaseFile)
        except sqlite3.Error as e:
            print("Database connection problem!")
            print(e)
            exit(-1)