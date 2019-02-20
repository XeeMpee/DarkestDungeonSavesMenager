class Save:
    
    def __init__(self, id=None, name=None, description=None, datetime=None):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__datetime = datetime

    
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getDatetime(self):
        return self.__datetime


    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setDescription(self, description):
        self.__description = description

    def setDatetime(self, str):
        #TODO        
        pass

