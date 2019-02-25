import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from controllers.Controller import *

class ReplaceSaveDialog:
    
    def __init__(self, parentWindow, controller, save, profileNumber):
        self.__controller = controller
        self.__builder = Gtk.Builder()
        self.__save = save
        self.__parentWindow = parentWindow
        self.__profileNumber = profileNumber

        self.__builder.add_from_file('views/ReplaceSaveDialog/ReplaceSaveDialog.glade')
        self.__window = self.__builder.get_object("replaceSaveWindow")
        self.__builder.get_object("saveNameLabel").set_text(' " {} " '.format(save.getName()))

        # Handles:
        self.__builder.get_object("noButton").connect("clicked",self.__noButtonHandle)
        self.__builder.get_object("yesButton").connect("clicked",self.__yesButtonHandle)
 

    def run(self):
        self.__window.show_all()


    def __noButtonHandle(self,arg):
        self.__window.destroy()
        pass
    
    def __yesButtonHandle(self,arg):
        self.__builder.get_object("progressBar").pulse()
        self.__controller.saveGame(self.__save.getName(), self.__save.getDescription(),self.__profileNumber)
        self.__window.destroy()
        pass