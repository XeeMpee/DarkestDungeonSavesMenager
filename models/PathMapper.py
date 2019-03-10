from database.Database import *

class PathMapper:

    def __init__(self):
        database = Database() 
        self.__connection = database.connect()


    def getPath(self) -> str:
        sql = '''SELECT path FROM Path LIMIT 1'''
        cur = self.__connection.cursor()
        cur.execute(sql)
        self.__connection.commit()
        path = cur.fetchone()
        print(path[0])
        return path[0]


    def setPath(self, path):
        sql = '''UPDATE Path SET path="{}" WHERE id=(SELECT id FROM Path LIMIT 1);''' .format(path)
        cur = self.__connection.cursor()
        cur.execute(sql)
        self.__connection.commit()
