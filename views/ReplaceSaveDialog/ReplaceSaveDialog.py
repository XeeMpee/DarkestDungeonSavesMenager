import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from controllers.Controller import *

class ReplaceSaveDialog:
    
    def __init__(self, parentWindow, saveName):
        self.__controller = Controller()
        self.__builder = Gtk.Builder()
        self.__saveName = saveName

        self.__parentWindow = parentWindow

        self.__builder.add_from_file('views/ReplaceSaveDialog/ReplaceSaveDialog.glade')
        self.__window = self.__builder.get_object("replaceSaveWindow")
        self.__builder.get_object("saveNameLabel").set_text(" {} ".format(saveName))

        # Handles:
        self.__builder.get_object("noButton").connect("clicked",self.__noButtonHandle)
 

    def run(self):
        self.__window.show_all()
        print(self.__saveName)


    def __noButtonHandle(self,arg):
        self.__window.destroy()
        pass
    
    def __yesButtonHandle(self,arg):
        pass