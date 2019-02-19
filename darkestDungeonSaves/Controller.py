import os
import re

class Controller:
    """ 
    Class proposed to controll mechanic of application
    """

    def __init__(self):
        
        self.__pathToSaves = '/home/xeempee/.local/share/Steam/userdata/109096097/262060/remote/'
        self.__profiles = list()
        self.__orderByOptions = [
            "Name",
            "Date ascending",
            "Date descending"
        ]


    def getOrderOptions(self):
        return self.__orderByOptions


    def generateProfilesList(self):
        listOfProfiles = os.listdir(self.__pathToSaves)
        toSave = list()
        
        for i in listOfProfiles:
            if(re.search('^profile_*',i)):
                toSave.append(i)
    
        self.__profiles = toSave
    