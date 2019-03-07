from database.Database import *
import os
import re
import shutil

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
    saveGame(name:str, description:str, profileNumber:int) : void - Saves game as new save using params.
    saveGameByReplacing(save:Save, profileNumber:int) : void - Saves game by replacing save passed as param.
    deleteSave(save:Save) : void - Delete save passed as param.
    uploadSave(save:Save, profileNumber:int) : Uploads saved game into game files to profile of number passed as param.
    modifySave(save:Save, name:str, description:str) : Changes name and description of save passed as param.
    __copySaveFiles(profileNumber:int, saveId:int) : Copies files of save from game files into new or existing folder in application files.
    __deleteSaveFiles(saveId:int) : Deletes files of passed id save in application files.
    __uploadSaveFiles(saveId:int, profileNumber:int) : Uploads files of passed id save into save game files of passed profile.
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
        print(listOfProfiles)
        listOfProfiles.sort()
        saves = list()
        
        for i in listOfProfiles:
            if(re.search('^profile_*',i)):
                text = str(open(str(self.__pathToSaves + i + "/persist.game.json"),encoding='utf-8', errors='ignore').read())
                toTrim = re.findall('estatename.....[a-zA-Z]+.game',(str)(text))
                name = toTrim[0][15:-5]
                print(name)                 
                saves.append((i, name))
                self.__profiles = saves

    def saveGame(self, name, description, profileNumber):
        save = Save(name,description)
        saveMapper = SaveMapper()
        saveMapper.insertSave(save)
        id = saveMapper.getIdentCurrent()
        self.__copySaveFiles(profileNumber, id)


    def saveGameByReplacing(self, save, profileNumber):
        id = save.getId()
        self.__copySaveFiles(profileNumber, id)        


    def deleteSave(self,save):
        saveMapper = SaveMapper()
        saveMapper.deleteSave(save)
        self.__deleteSaveFiles(save.getId())
    

    def uploadSave(self, save, profileNumber):
        self.__uploadSaveFiles(save.getId(), profileNumber)


    def modifySave(self, save, name, description):
        saveMapper = SaveMapper()
        saveMapper.modifySave(save, name, description)

        
    def __copySaveFiles(self, profileNumber, saveId):
        
        srcPath = self.__pathToSaves + "/" + self.__profiles[profileNumber][0]
        destinyPath = "saves/" + (str)(saveId)

        if(not os.path.isdir(srcPath)):
            print("No source file found!")
            return
        
        if(os.path.isdir(destinyPath)):
            print('Destiny file alredy exists... deleting and copying!')
            shutil.rmtree(destinyPath)
        shutil.copytree(srcPath,destinyPath)
    

    def __deleteSaveFiles(self, saveId):
        path = "saves/"+(str)(saveId)
        shutil.rmtree(path)

    
    def __uploadSaveFiles(self, saveId, profileNumber):
        destinyPath = self.__pathToSaves + self.__profiles[profileNumber][0]
        srcPath = "saves/" + (str)(saveId)

        if(not os.path.isdir(srcPath)):
            print("No source file found!")
            return
        
        shutil.rmtree(destinyPath)
        shutil.copytree(srcPath,destinyPath)
