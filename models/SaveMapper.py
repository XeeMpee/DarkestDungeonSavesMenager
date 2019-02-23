from database.Database import *
from models.Save import *

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

    
    def getAllSaves(self):
        sql = '''SELECT * FROM Saves ORDER BY date DESC, time DESC;'''
        
        cur = self.__connection.cursor()
        cur.execute(sql)
        all = cur.fetchall()

        savesList = list()
        for i in all:
            id = i[0]
            name = i[1]
            description = i[2]
            date = i[3]
            time = i[4]
            save = Save(name,description,date,time,id)
            savesList.append(save)
        
        return savesList



