class Save:
    
    def __init__(self, name=None, description=None, date=None, time=None, id=None):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__date = date
        self.__time = time

    
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    # def getProfile(self):
    #     return self.__profile

    def getDescription(self):
        return self.__description

    def getDate(self):
        return self.__date

    def getTime(self):
        return self.__time


    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    # def setProfile(self, profileNumber):
    #     self.__profile = profileNumber

    def setDescription(self, description):
        self.__description = description

    def setDate(self, date):
        self.__date = date  

    def setTime(self, time):
        self.__time = time

    def print(self):
        print('id:{},name:"{}",description:"{}",date:"{}",time:"{}"'.format(self.__id,self.__name,self.__description,self.__date,self.__time))
