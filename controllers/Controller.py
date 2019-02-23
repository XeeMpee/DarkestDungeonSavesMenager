from database.Database import *
import os
import re

from models.Save import *
from models.SaveMapper import *
from controllers.OrderEnum import *

class Controller:
    """ 
    Class proposed to controll mechanic of application.

    Atributes:
    ----------------
    __pathToSaves : str - Desccribes path to "Darkest Dungeon" saves containing directory.
    __profiles : [(id:str, name:str)] - List of saves named like: profile_\d.
    __orderByOptions : [str] - List of ordering options. 
    
    Methods:
    ----------------
    getOrderOptions() : [str] - Return __orderByOption list.
    getProfilesList() : [str, str] - Returns __profiles list.    
    generateProfilesList() : void - Generates list of profiles by analyzing game saves directory.
    """

    def __init__(self):
        
        self.__pathToSaves = '/home/xeempee/.local/share/Steam/userdata/109096097/262060/remote/'
        self.__profiles = list()
        self.__orderByOptions = [
            ("Name",OrderEnum.NAME),
            ("Date ascending",OrderEnum.TIMEASC),
            ("Date descending",OrderEnum.TIMEDESC)
        ]
        self.generateProfilesList()


    def getOrderOptions(self):
        return self.__orderByOptions


    def getProfilesList(self):
        return self.__profiles


    def generateProfilesList(self):
        listOfProfiles = os.listdir(self.__pathToSaves)
        listOfProfiles.reverse()
        saves = list()
        
        for i in listOfProfiles:
            if(re.search('^profile_*',i)):
                
                fd = os.open(str(self.__pathToSaves + i + "/persist.game.json"),os.O_RDONLY)
                text = os.read(fd,10000)
                textTrim1 = re.findall('estatename[\\\\0x1]+[a-zA-Z]+',str(text))[0]
                textTrim2 = textTrim1[10:]
                name = re.findall('[0-15][a-zA-Z]+',textTrim2)[0][1:]
                
                saves.append((i,name))
                self.__profiles = saves

    def saveGame(self, name, description):
        save = Save(name,description)
        saveMapper = SaveMapper()
        saveMapper.insertSave(save)


        
    