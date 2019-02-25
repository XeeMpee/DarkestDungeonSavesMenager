from database.Database import *
from models.Save import *
from controllers.OrderEnum import *

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

    
    def getAllSaves(self, orderoption=OrderEnum.TIMEDESC):
        
        if(orderoption == OrderEnum.TIMEDESC):
            sql = '''SELECT * FROM Saves ORDER BY date DESC, time DESC, name;'''
        elif(orderoption == OrderEnum.TIMEASC):
            sql = '''SELECT * FROM Saves ORDER BY date ASC, time ASC, name;'''
        elif(orderoption == OrderEnum.NAME):
            sql = '''SELECT * FROM Saves ORDER BY name;'''
        
        cur = self.__connection.cursor()
        cur.execute(sql)
        self.__connection.commit()
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

    def deleteSave(self, save):
        
        sql = '''DELETE FROM Saves WHERE id={}'''.format(save.getId())
        
        cur = self.__connection.cursor()
        cur.execute(sql)
        self.__connection.commit()

    def modifySave(self, save, name, description):
 
        sql = '''UPDATE Saves SET name="{}",description="{}" WHERE id={}'''.format(name, description, save.getId())
        
        cur = self.__connection.cursor()
        cur.execute(sql)
        self.__connection.commit()

    def getIdentCurrent(self):
        sql = """SELECT last_insert_rowid(); """
        cur = self.__connection.cursor()
        cur.execute(sql)
        self.__connection.commit()
        all = cur.fetchall()
        identCurrent = all[0][0]
        return (identCurrent)


