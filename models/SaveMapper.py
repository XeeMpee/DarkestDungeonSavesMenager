from database.Database import *

class SaveMapper:

    def __init__(self):
        database = Database() 
        self.__connection = database.connect()

    def insertSave(self, save):
        name = save.getName()
        description = save.getDescription()
    

        sql = '''INSERT INTO Saves (name, description, date, time)
        VALUES (?,?,date('now'), time('now'));
        '''
        task = (name,description)

        cur = self.__connection.cursor()
        cur.execute(sql,task)
        self.__connection.commit()
        return cur.lastrowid


